(() => {
  if (customElements.get('mc-happy-customers')) return;

class MCHappyCustomers extends HTMLElement {
  connectedCallback() {
    this.revealStep = Math.max(1, Number(this.dataset.revealStep) || 4);
    this.addEventListener('click', this.handleClick);
    document.addEventListener('shopify:block:select', this.handleBlockSelect);
  }

  disconnectedCallback() {
    this.removeEventListener('click', this.handleClick);
    document.removeEventListener('shopify:block:select', this.handleBlockSelect);
  }

  handleClick = (event) => {
    const button = event.target.closest('[data-mc-customer-more]');
    if (!button || !this.contains(button)) return;

    const hiddenItems = Array.from(this.querySelectorAll('[data-mc-extra-customer][hidden]'));
    hiddenItems.slice(0, this.revealStep).forEach((item) => {
      item.hidden = false;
    });

    if (this.querySelectorAll('[data-mc-extra-customer][hidden]').length === 0) {
      button.closest('.mc-happy-customers__more')?.remove();
    }
  };

  handleBlockSelect = (event) => {
    if (!this.contains(event.target)) return;
    const blockId = event.detail?.blockId || event.target.dataset?.blockId;
    const item = this.querySelector(`[data-block-id="${CSS.escape(blockId || '')}"]`);
    if (item) item.hidden = false;
  };
}

customElements.define('mc-happy-customers', MCHappyCustomers);
})();
