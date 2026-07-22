(() => {
  const initialized = new WeakSet();
  const focusableSelector = [
    'a[href]',
    'button:not([disabled])',
    'input:not([disabled])',
    'select:not([disabled])',
    'textarea:not([disabled])',
    '[tabindex]:not([tabindex="-1"])',
  ].join(',');

  function initHeader(root) {
    if (!root || initialized.has(root)) return;
    initialized.add(root);

    const drawers = Array.from(root.querySelectorAll('[data-mc-drawer]'));
    const openButtons = Array.from(root.querySelectorAll('[data-mc-open]'));
    const closeButtons = root.querySelectorAll('[data-mc-close]');
    const megaMenus = Array.from(root.querySelectorAll('[data-mc-mega]'));
    const placeholderLinks = root.dataset.placeholderLinks === 'true';
    const currencyCode = root.dataset.currencyCode || 'USD';
    const locale = root.dataset.locale || document.documentElement.lang || 'en-US';
    const messages = {
      searching: root.dataset.searchingText || 'Searching…',
      empty: root.dataset.emptyText || 'No matching products found.',
      error: root.dataset.errorText || 'Search is temporarily unavailable.',
    };

    let activeDrawer = null;
    let previousFocus = null;

    const getOpenButtons = (name) => openButtons.filter((button) => button.dataset.mcOpen === name);

    const updateTriggerState = (name, expanded) => {
      getOpenButtons(name).forEach((button) => button.setAttribute('aria-expanded', String(expanded)));
    };

    const resetMobileNavigation = () => {
      const mobileNav = root.querySelector('[data-mc-mobile-nav]');
      if (!mobileNav) return;
      mobileNav.querySelectorAll('[data-mc-mobile-panel]').forEach((panel) => {
        const active = panel.dataset.mcMobilePanel === 'root';
        panel.hidden = !active;
        panel.classList.toggle('is-active', active);
      });
    };

    const closeDrawer = (drawer, restoreFocus = true) => {
      if (!drawer) return;
      const name = drawer.dataset.mcDrawer;
      drawer.dataset.open = 'false';
      drawer.setAttribute('aria-hidden', 'true');
      updateTriggerState(name, false);
      document.documentElement.classList.remove('mc-lock');
      document.body.classList.remove('mc-lock');

      if (activeDrawer === drawer) activeDrawer = null;
      if (restoreFocus && previousFocus instanceof HTMLElement && previousFocus.isConnected) {
        previousFocus.focus({ preventScroll: true });
      }
    };

    const openDrawer = (name, trigger) => {
      const drawer = root.querySelector(`[data-mc-drawer="${CSS.escape(name)}"]`);
      if (!drawer) return;

      drawers.forEach((item) => closeDrawer(item, false));
      previousFocus = trigger;
      activeDrawer = drawer;
      drawer.dataset.open = 'true';
      drawer.setAttribute('aria-hidden', 'false');
      updateTriggerState(name, true);
      document.documentElement.classList.add('mc-lock');
      document.body.classList.add('mc-lock');

      if (name === 'menu') resetMobileNavigation();

      requestAnimationFrame(() => {
        const focusTarget = drawer.querySelector('[data-mc-autofocus], [data-mc-close], button, input, a');
        if (focusTarget instanceof HTMLElement) focusTarget.focus({ preventScroll: true });
      });
    };

    openButtons.forEach((button) => {
      button.addEventListener('click', () => openDrawer(button.dataset.mcOpen, button));
    });

    closeButtons.forEach((button) => {
      button.addEventListener('click', () => closeDrawer(button.closest('[data-mc-drawer]')));
    });

    drawers.forEach((drawer) => {
      drawer.addEventListener('click', (event) => {
        if (event.target instanceof Element && event.target.matches('[data-mc-backdrop]')) closeDrawer(drawer);
      });
    });

    document.addEventListener('keydown', (event) => {
      if (!activeDrawer) return;

      if (event.key === 'Escape') {
        event.preventDefault();
        closeDrawer(activeDrawer);
        return;
      }

      if (event.key !== 'Tab') return;
      const panel = activeDrawer.querySelector('.mc-drawer__panel');
      if (!panel) return;
      const focusable = Array.from(panel.querySelectorAll(focusableSelector)).filter(
        (element) => element instanceof HTMLElement && !element.hidden && element.offsetParent !== null
      );
      if (!focusable.length) {
        event.preventDefault();
        panel.focus();
        return;
      }

      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    });

    megaMenus.forEach((details) => {
      details.addEventListener('toggle', () => {
        if (!details.open) return;
        megaMenus.forEach((other) => {
          if (other !== details) other.removeAttribute('open');
        });
      });
    });

    document.addEventListener('click', (event) => {
      if (!root.contains(event.target)) {
        megaMenus.forEach((details) => details.removeAttribute('open'));
      }
    });

    root.querySelectorAll('[data-mc-mobile-open]').forEach((button) => {
      button.addEventListener('click', () => showMobilePanel(button.dataset.mcMobileOpen, button));
    });

    root.querySelectorAll('[data-mc-mobile-back]').forEach((button) => {
      button.addEventListener('click', () => showMobilePanel(button.dataset.mcMobileBack, button));
    });

    function showMobilePanel(name, trigger) {
      const mobileNav = trigger.closest('[data-mc-mobile-nav]');
      if (!mobileNav) return;
      const target = mobileNav.querySelector(`[data-mc-mobile-panel="${CSS.escape(name)}"]`);
      if (!target) return;

      mobileNav.querySelectorAll('[data-mc-mobile-panel]').forEach((panel) => {
        const active = panel === target;
        panel.hidden = !active;
        panel.classList.toggle('is-active', active);
      });

      requestAnimationFrame(() => {
        const focusTarget = target.querySelector('[data-mc-mobile-back], .mc-mobile-nav__row, a, button');
        if (focusTarget instanceof HTMLElement) focusTarget.focus({ preventScroll: true });
      });
    }

    if (placeholderLinks) {
      root.querySelectorAll('a[href="#"]').forEach((link) => {
        link.addEventListener('click', (event) => event.preventDefault());
      });
    }

    const searchDrawer = root.querySelector('[data-mc-drawer="search"]');
    const searchInput = searchDrawer?.querySelector('[data-mc-search-input]');
    const searchForm = searchDrawer?.querySelector('[data-mc-search-form]');
    const resultContainer = searchDrawer?.querySelector('[data-mc-search-results]');
    const suggestUrl = searchDrawer?.dataset.suggestUrl;
    let searchTimer;
    let requestController;

    const setSearchExpanded = (expanded) => {
      searchInput?.setAttribute('aria-expanded', String(expanded));
    };

    const formatPrice = (value) => {
      const number = Number.parseFloat(String(value ?? '').replace(/[^0-9.-]/g, ''));
      if (!Number.isFinite(number)) return '';
      try {
        return new Intl.NumberFormat(locale, {
          style: 'currency',
          currency: currencyCode,
          currencyDisplay: 'symbol',
        }).format(number);
      } catch {
        return `${currencyCode} ${number.toFixed(2)}`;
      }
    };

    const createMessage = (text) => {
      const message = document.createElement('p');
      message.className = 'mc-search__empty';
      message.textContent = text;
      return message;
    };

    const renderProducts = (products) => {
      if (!resultContainer) return;
      resultContainer.replaceChildren();

      if (!products.length) {
        resultContainer.append(createMessage(messages.empty));
        setSearchExpanded(false);
        return;
      }

      products.forEach((product, index) => {
        const link = document.createElement('a');
        link.className = 'mc-search__result';
        link.href = placeholderLinks ? '#' : product.url;
        link.setAttribute('role', 'option');
        link.id = `${resultContainer.id}-option-${index}`;

        if (placeholderLinks) {
          link.addEventListener('click', (event) => event.preventDefault());
        }

        if (product.featured_image?.url) {
          const image = document.createElement('img');
          image.className = 'mc-search__result-image';
          image.loading = 'lazy';
          image.alt = product.featured_image?.alt || '';
          image.src = product.featured_image.url;
          link.append(image);
        } else {
          const placeholder = document.createElement('span');
          placeholder.className = 'mc-search__result-image mc-search__result-image--placeholder';
          placeholder.setAttribute('aria-hidden', 'true');
          link.append(placeholder);
        }

        const copy = document.createElement('div');
        const title = document.createElement('p');
        title.className = 'mc-search__result-title';
        title.textContent = product.title;

        const price = document.createElement('div');
        price.className = 'mc-search__result-price';
        price.textContent = formatPrice(product.price);

        copy.append(title, price);
        link.append(copy);
        resultContainer.append(link);
      });

      setSearchExpanded(true);
    };

    const search = async (query) => {
      if (!suggestUrl || !resultContainer) return;
      requestController?.abort();
      requestController = new AbortController();

      resultContainer.replaceChildren(createMessage(messages.searching));
      setSearchExpanded(true);

      try {
        const url = new URL(suggestUrl, window.location.origin);
        url.searchParams.set('q', query);
        url.searchParams.set('resources[type]', 'product');
        url.searchParams.set('resources[limit]', '6');
        url.searchParams.set('resources[options][unavailable_products]', 'last');

        const response = await fetch(url, {
          headers: { Accept: 'application/json' },
          signal: requestController.signal,
        });

        if (!response.ok) throw new Error(`Search failed: ${response.status}`);
        const data = await response.json();
        renderProducts(data?.resources?.results?.products || []);
      } catch (error) {
        if (error.name === 'AbortError') return;
        resultContainer.replaceChildren(createMessage(messages.error));
        setSearchExpanded(false);
      }
    };

    searchForm?.addEventListener('submit', (event) => {
      if (placeholderLinks) event.preventDefault();
    });

    searchInput?.addEventListener('input', () => {
      window.clearTimeout(searchTimer);
      const query = searchInput.value.trim();

      if (query.length < 2) {
        resultContainer?.replaceChildren();
        setSearchExpanded(false);
        return;
      }

      searchTimer = window.setTimeout(() => search(query), 180);
    });

    searchInput?.addEventListener('keydown', (event) => {
      if (!resultContainer) return;
      const options = Array.from(resultContainer.querySelectorAll('[role="option"]'));
      if (!options.length) return;

      if (event.key === 'ArrowDown') {
        event.preventDefault();
        options[0].focus();
      } else if (event.key === 'Escape') {
        setSearchExpanded(false);
      }
    });

    resultContainer?.addEventListener('keydown', (event) => {
      const options = Array.from(resultContainer.querySelectorAll('[role="option"]'));
      const currentIndex = options.indexOf(document.activeElement);
      if (currentIndex < 0) return;

      if (event.key === 'ArrowDown') {
        event.preventDefault();
        options[(currentIndex + 1) % options.length].focus();
      } else if (event.key === 'ArrowUp') {
        event.preventDefault();
        if (currentIndex === 0) searchInput?.focus();
        else options[currentIndex - 1].focus();
      } else if (event.key === 'Escape') {
        event.preventDefault();
        searchInput?.focus();
      }
    });

    const updateHeaderHeight = () => {
      document.body.style.setProperty('--mc-header-height', `${root.offsetHeight}px`);
      document.body.style.setProperty('--header-height', `${root.offsetHeight}px`);
    };

    if ('ResizeObserver' in window) {
      const resizeObserver = new ResizeObserver(updateHeaderHeight);
      resizeObserver.observe(root);
    } else {
      window.addEventListener('resize', updateHeaderHeight);
    }
    updateHeaderHeight();
  }

  function boot(scope = document) {
    scope.querySelectorAll('[data-mc-header]').forEach(initHeader);
  }

  boot();
  document.addEventListener('shopify:section:load', (event) => boot(event.target));
})();
