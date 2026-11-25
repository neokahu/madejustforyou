import cv2, numpy as np, sys
V, R, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
cap = cv2.VideoCapture(V); frames=[]
while True:
    ok,f=cap.read()
    if not ok or len(frames)>=60: break
    frames.append(f)
rend = cv2.imread(R, cv2.IMREAD_UNCHANGED)              # BGRA 3185x3000
a = rend[:,:,3]; ys,xs = np.where(a>10); rb=(xs.min(),ys.min(),xs.max(),ys.max())
x0,y0,x1,y1 = 232,455,562,832                            # ornament bbox in frame 0 (manual)
src = np.float32([[rb[0],rb[1]],[rb[2],rb[1]],[rb[2],rb[3]],[rb[0],rb[3]]])
dst0 = np.float32([[x0,y0],[x1,y0],[x1,y1],[x0,y1]])
H0 = cv2.getPerspectiveTransform(src,dst0)
g0 = cv2.cvtColor(frames[0],cv2.COLOR_BGR2GRAY)
mask = np.zeros_like(g0); mask[y0+60:y1-20, x0+10:x1-10] = 255   # face area, avoid hand/cord
p0 = cv2.goodFeaturesToTrack(g0,400,0.01,5,mask=mask)
prev, pprev = g0, p0; Hacc = np.eye(3); out=[]; inl=[]
for i,f in enumerate(frames):
    g = cv2.cvtColor(f,cv2.COLOR_BGR2GRAY)
    if i>0:
        p1,st,err = cv2.calcOpticalFlowPyrLK(prev,g,pprev,None,winSize=(21,21),maxLevel=3)
        good0, good1 = pprev[st==1], p1[st==1]
        Hs,m = cv2.findHomography(good0,good1,cv2.RANSAC,3.0)
        Hacc = Hs @ Hacc; inl.append(int(m.sum()))
        pprev = good1.reshape(-1,1,2)
        if len(pprev)<80:   # replenish inside the warped face area
            q = cv2.perspectiveTransform(dst0.reshape(-1,1,2),Hacc).reshape(-1,2).astype(np.int32)
            mk=np.zeros_like(g); cv2.fillConvexPoly(mk,q,255); mk[:int(q[:,1].min()+60)]=0
            new=cv2.goodFeaturesToTrack(g,400,0.01,5,mask=mk)
            if new is not None: pprev=np.vstack([pprev,new]).astype(np.float32)
        prev = g
    Hf = Hacc @ H0
    w = cv2.warpPerspective(rend, Hf, (f.shape[1], f.shape[0]))
    al = w[:,:,3:4].astype(np.float32)/255
    comp = (f*(1-al) + w[:,:,:3]*al).astype(np.uint8)
    out.append(comp)
h,wd = out[0].shape[:2]
vw = cv2.VideoWriter(OUT, cv2.VideoWriter_fourcc(*'mp4v'), 24, (wd*2,h))
for f,c in zip(frames,out): vw.write(np.hstack([f,c]))
vw.release()
for i in (0,20,40,59): cv2.imwrite(OUT.replace('.mp4',f'-{i}.jpg'), np.hstack([frames[i],out[i]]))
print('frames',len(frames),'inliers min/med',min(inl),int(np.median(inl)))
