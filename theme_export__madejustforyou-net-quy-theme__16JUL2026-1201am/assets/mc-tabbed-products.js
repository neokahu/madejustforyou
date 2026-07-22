(() => {
  if (customElements.get('mc-tabbed-products')) return;

class MCTabbedProducts extends HTMLElement {
  connectedCallback() {
    this.tabs = Array.from(this.querySelectorAll('[data-mc-tab]'));
    this.panels = Array.from(this.querySelectorAll('[data-mc-panel]'));
    this.revealStep = Math.max(1, Number(this.dataset.revealStep) || 4);

    this.addEventListener('click', this.handleClick);
    this.addEventListener('keydown', this.handleKeydown);
    document.addEventListener('shopify:block:select', this.handleBlockSelect);
  }

  disconnectedCallback() {
    this.removeEventListener('click', this.handleClick);
    this.removeEventListener('keydown', this.handleKeydown);
    document.removeEventListener('shopify:block:select', this.handleBlockSelect);
  }

  handleClick = (event) => {
    const tab = event.target.closest('[data-mc-tab]');
    if (tab && this.contains(tab)) {
      this.activateTab(tab, true);
      return;
    }

    const showMore = event.target.closest('[data-mc-show-more]');
    if (showMore && this.contains(showMore)) {
      const panel = showMore.closest('[data-mc-panel]');
      this.revealMore(panel, showMore);
    }
  };

  handleKeydown = (event) => {
    const currentTab = event.target.closest('[data-mc-tab]');
    if (!currentTab || !this.contains(currentTab)) return;

    const index = this.tabs.indexOf(currentTab);
    let nextIndex = null;

    if (event.key === 'ArrowRight') nextIndex = (index + 1) % this.tabs.length;
    if (event.key === 'ArrowLeft') nextIndex = (index - 1 + this.tabs.length) % this.tabs.length;
    if (event.key === 'Home') nextIndex = 0;
    if (event.key === 'End') nextIndex = this.tabs.length - 1;

    if (nextIndex === null) return;
    event.preventDefault();
    this.tabs[nextIndex].focus();
    this.activateTab(this.tabs[nextIndex], false);
  };

  handleBlockSelect = (event) => {
    if (!this.contains(event.target)) return;
    const blockId = event.detail?.blockId || event.target.dataset?.blockId;
    const tab = this.tabs.find((item) => item.dataset.blockId === blockId);
    if (tab) this.activateTab(tab, true);
  };

  activateTab(tab, scrollIntoView) {
    const targetId = tab.getAttribute('aria-controls');
    const targetPanel = this.panels.find((panel) => panel.id === targetId);
    if (!targetPanel) return;

    this.tabs.forEach((item) => {
      const active = item === tab;
      item.classList.toggle('is-active', active);
      item.setAttribute('aria-selected', String(active));
      item.tabIndex = active ? 0 : -1;
    });

    this.panels.forEach((panel) => {
      panel.hidden = panel !== targetPanel;
    });

    this.mountPanel(targetPanel);
    const grid = targetPanel.querySelector('[data-mc-tabbed-grid]');
    if (grid) grid.scrollLeft = 0;

    if (scrollIntoView) {
      tab.scrollIntoView({ behavior: 'smooth', block: 'nearest', inline: 'center' });
    }
  }

  mountPanel(panel) {
    const mount = panel.querySelector('[data-mc-panel-mount]');
    const template = panel.querySelector('[data-mc-panel-template]');
    if (!mount || !template || mount.childElementCount > 0) return;
    mount.appendChild(template.content.cloneNode(true));
    template.remove();
  }

  revealMore(panel, button) {
    if (!panel) return;
    const hiddenProducts = Array.from(panel.querySelectorAll('[data-mc-extra-product][hidden]'));
    hiddenProducts.slice(0, this.revealStep).forEach((item) => {
      item.hidden = false;
    });

    if (panel.querySelectorAll('[data-mc-extra-product][hidden]').length === 0) {
      const wrapper = button.closest('.mc-tabbed-products__more');
      if (wrapper) wrapper.hidden = true;
    }
  }
}

customElements.define('mc-tabbed-products', MCTabbedProducts);
})();
