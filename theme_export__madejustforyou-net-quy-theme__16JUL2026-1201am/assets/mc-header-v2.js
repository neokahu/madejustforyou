(() => {
const initialized = new WeakSet();
const desktopMedia = window.matchMedia('(min-width: 990px)');
const flagEmoji = (countryCode) => {
const code = String(countryCode || '').trim().toUpperCase();
if (!/^[A-Z]{2}$/.test(code)) return '';
return [...code].map((char) => String.fromCodePoint(127397 + char.charCodeAt(0))).join('');
};
const cleanCountryName = (text) => String(text || '').replace(/\s*\([^)]*\)\s*$/, '').trim();
function init(root) {
if (!root || initialized.has(root)) return;
initialized.add(root);
const placeholderLinks = root.dataset.placeholderLinks === 'true';
const currencyCode = root.dataset.currencyCode || 'USD';
const locale = root.dataset.locale || document.documentElement.lang || 'en-US';
const messages = {
searching: root.dataset.searchingText || 'Searching…',
empty: root.dataset.emptyText || 'No matching products found.',
error: root.dataset.errorText || 'Search is temporarily unavailable.',
};
enhanceUtilities(root);
enhanceNavigation(root, placeholderLinks);
enhanceDesktopSearch(root, { placeholderLinks, currencyCode, locale, messages });
const updateHeaderState = () => {
root.dataset.scrolled = String(window.scrollY > 8);
};
window.addEventListener('scroll', updateHeaderState, { passive: true });
updateHeaderState();
}
function enhanceUtilities(root) {
const utilities = root.querySelector('.mc-header__utilities');
if (!utilities) return;
const searchButton = utilities.querySelector('[data-mc-open="search"]');
const account = utilities.querySelector('.mc-header__utility--account');
const localization = utilities.querySelector('.mc-header__localization');
const localizationSummary = localization?.querySelector('summary');
const cart = utilities.querySelector('.mc-header__cart');
const textLinks = Array.from(utilities.querySelectorAll('a.mc-header__utility:not(.mc-header__cart)'));
const tracking = textLinks.find((link) => /track/i.test(link.getAttribute('aria-label') || ''));
const wishlist = textLinks.find((link) => /wish/i.test(link.getAttribute('aria-label') || ''));
if (account) account.classList.add('mc-header__utility--account');
if (tracking) tracking.classList.add('mc-header__utility--tracking', 'mc-header__utility--desktop');
if (wishlist) wishlist.classList.add('mc-header__utility--wishlist', 'mc-header__utility--desktop');
[account, wishlist, tracking].forEach((utility) => {
if (!utility) return;
utility.querySelectorAll('.mc-header__utility-label').forEach((node) => node.remove());
const label = document.createElement('span');
label.className = 'mc-header__utility-label';
label.textContent = utility.getAttribute('aria-label') || '';
utility.append(label);
});
if (localizationSummary) {
const selectedCountry = localization.querySelector('select[name="country_code"] option:checked');
const selectedCode = selectedCountry?.value || '';
const selectedName = cleanCountryName(selectedCountry?.textContent) || selectedCode;
localizationSummary.replaceChildren();
const flag = document.createElement('span');
flag.className = 'mc-header__country-flag';
flag.setAttribute('aria-hidden', 'true');
flag.textContent = flagEmoji(selectedCode);
const divider = document.createElement('span');
divider.className = 'mc-header__country-divider';
divider.setAttribute('aria-hidden', 'true');
const name = document.createElement('span');
name.className = 'mc-header__country-name';
name.textContent = selectedName;
localizationSummary.append(flag, divider, name);
}
[searchButton, account, wishlist, tracking, localization, cart].forEach((item) => {
if (item) utilities.append(item);
});
}
function enhanceNavigation(root, placeholderLinks) {
const megaMenus = Array.from(root.querySelectorAll('[data-mc-mega]'));
const navItems = Array.from(root.querySelectorAll('.mc-nav__item'));
const mobileNav = root.querySelector('[data-mc-mobile-nav]');
let openTimer = 0;
let closeTimer = 0;
navItems.forEach((item) => {
const label = item.querySelector('.mc-nav__summary, .mc-nav__plain-link')?.textContent?.trim() || '';
item.classList.toggle('is-featured', /anniversary/i.test(label));
});
const closeMegaMenus = (except = null) => {
megaMenus.forEach((details) => {
if (details !== except) details.removeAttribute('open');
});
};
const createMegaColumn = (title, href, links = []) => {
const column = document.createElement('div');
column.className = 'mc-mega__column';
const heading = document.createElement('a');
heading.className = 'mc-mega__column-title mc-focus-ring';
heading.href = href || '#';
heading.textContent = title;
column.append(heading);
if (links.length) {
const list = document.createElement('ul');
list.className = 'mc-mega__links';
links.forEach((sourceLink) => {
const item = document.createElement('li');
const link = sourceLink.cloneNode(true);
link.removeAttribute('class');
item.append(link);
list.append(item);
});
column.append(list);
}
if (placeholderLinks) {
column.querySelectorAll('a[href="#"]').forEach((link) => {
link.addEventListener('click', (event) => event.preventDefault());
});
}
return column;
};
if (mobileNav) {
megaMenus.forEach((details) => {
const item = details.closest('.mc-nav__item');
const itemIndex = navItems.indexOf(item) + 1;
const levelOne = mobileNav.querySelector(`[data-mc-mobile-panel="level-1-${itemIndex}"]`);
const grid = details.querySelector('.mc-mega__grid');
const oldColumns = details.querySelector('.mc-mega__columns');
if (!levelOne || !grid || !oldColumns) return;
const content = document.createElement('div');
content.className = 'mc-mega__content';
const header = document.createElement('div');
header.className = 'mc-mega__header';
const title = document.createElement('h3');
title.className = 'mc-mega__title';
title.textContent = details.querySelector('.mc-nav__summary')?.textContent?.trim() || '';
header.append(title);
const parentLink = levelOne.querySelector(':scope > .mc-mobile-nav__shop-all');
if (parentLink) {
const shopAll = parentLink.cloneNode(true);
shopAll.className = 'mc-mega__shop-all mc-focus-ring';
header.append(shopAll);
}
const columns = document.createElement('div');
columns.className = 'mc-mega__columns';
levelOne.querySelectorAll(':scope > .mc-mobile-nav__row').forEach((row) => {
if (row instanceof HTMLButtonElement && row.dataset.mcMobileOpen) {
const childPanel = mobileNav.querySelector(
`[data-mc-mobile-panel="${CSS.escape(row.dataset.mcMobileOpen)}"]`
);
if (!childPanel) return;
const childTitle = childPanel.querySelector('.mc-mobile-nav__panel-title')?.textContent?.trim();
const childAll = childPanel.querySelector(':scope > .mc-mobile-nav__shop-all');
const childLinks = Array.from(childPanel.querySelectorAll(':scope > a.mc-mobile-nav__row'));
if (childTitle) columns.append(createMegaColumn(childTitle, childAll?.href || '#', childLinks));
} else if (row instanceof HTMLAnchorElement) {
columns.append(createMegaColumn(row.textContent.trim(), row.href));
}
});
content.append(header, columns);
oldColumns.remove();
grid.insertBefore(content, grid.firstChild);
});
}
megaMenus.forEach((details) => {
const item = details.closest('.mc-nav__item');
if (!item) return;
item.addEventListener('pointerenter', (event) => {
if (!desktopMedia.matches || event.pointerType === 'touch') return;
window.clearTimeout(closeTimer);
openTimer = window.setTimeout(() => {
closeMegaMenus(details);
details.setAttribute('open', '');
}, 80);
});
item.addEventListener('pointerleave', (event) => {
if (!desktopMedia.matches || event.pointerType === 'touch') return;
window.clearTimeout(openTimer);
closeTimer = window.setTimeout(() => details.removeAttribute('open'), 170);
});
item.addEventListener('focusin', () => {
if (!desktopMedia.matches) return;
closeMegaMenus(details);
details.setAttribute('open', '');
});
item.addEventListener('focusout', () => {
requestAnimationFrame(() => {
if (!item.contains(document.activeElement)) details.removeAttribute('open');
});
});
});
}
function enhanceDesktopSearch(root, context) {
const host = root.querySelector('.mc-header__desktop-search');
const drawer = root.querySelector('[data-mc-drawer="search"]');
const sourceForm = drawer?.querySelector('[data-mc-search-form]');
const sourceInput = drawer?.querySelector('[data-mc-search-input]');
const sourceTrends = drawer?.querySelector('.mc-search__trends');
const suggestUrl = drawer?.dataset.suggestUrl;
if (!host || !sourceForm || !sourceInput) return;
const form = document.createElement('form');
form.className = 'mc-header-search';
form.action = sourceForm.action;
form.method = 'get';
form.setAttribute('role', 'search');
const input = document.createElement('input');
input.className = 'mc-header-search__input';
input.type = 'search';
input.name = 'q';
input.placeholder = sourceInput.placeholder || '';
input.autocomplete = 'off';
input.setAttribute('aria-label', sourceInput.getAttribute('aria-label') || sourceInput.placeholder || 'Search');
input.setAttribute('aria-autocomplete', 'list');
input.setAttribute('aria-expanded', 'false');
const submit = document.createElement('button');
submit.className = 'mc-header-search__submit';
submit.type = 'submit';
submit.setAttribute('aria-label', sourceForm.querySelector('[type="submit"]')?.getAttribute('aria-label') || 'Submit search');
submit.innerHTML = '<svg class="mc-icon" viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"></circle><path d="m20 20-3.8-3.8"></path></svg>';
form.append(input, submit);
const panel = document.createElement('div');
panel.className = 'mc-header-search__panel';
panel.dataset.open = 'false';
if (sourceTrends?.children.length) {
const heading = document.createElement('p');
heading.className = 'mc-header-search__heading';
heading.textContent = drawer.querySelector('.mc-search__label')?.textContent?.trim() || 'Trending searches';
const trends = document.createElement('div');
trends.className = 'mc-header-search__trends';
Array.from(sourceTrends.children).forEach((source) => {
const trend = source.cloneNode(true);
trend.className = 'mc-header-search__trend';
trends.append(trend);
});
panel.append(heading, trends);
}
const results = document.createElement('div');
results.className = 'mc-header-search__results';
results.id = `McHeaderSearchResults-${Math.random().toString(36).slice(2)}`;
results.setAttribute('role', 'listbox');
results.setAttribute('aria-live', 'polite');
input.setAttribute('aria-controls', results.id);
panel.append(results);
host.replaceChildren(form, panel);
let timer = 0;
let controller = null;
const setPanelOpen = (open) => {
panel.dataset.open = String(open);
input.setAttribute('aria-expanded', String(open));
};
const message = (text) => {
const node = document.createElement('p');
node.className = 'mc-header-search__message';
node.textContent = text;
return node;
};
const formatPrice = (value) => {
const number = Number.parseFloat(String(value ?? '').replace(/[^0-9.-]/g, ''));
if (!Number.isFinite(number)) return '';
try {
return new Intl.NumberFormat(context.locale, {
style: 'currency',
currency: context.currencyCode,
currencyDisplay: 'symbol',
}).format(number);
} catch {
return `${context.currencyCode} ${number.toFixed(2)}`;
}
};
const render = (products) => {
results.replaceChildren();
if (!products.length) {
results.append(message(context.messages.empty));
setPanelOpen(true);
return;
}
products.forEach((product, index) => {
const link = document.createElement('a');
link.className = 'mc-header-search__result';
link.href = context.placeholderLinks ? '#' : product.url;
link.setAttribute('role', 'option');
link.id = `${results.id}-option-${index}`;
if (context.placeholderLinks) link.addEventListener('click', (event) => event.preventDefault());
if (product.featured_image?.url) {
const image = document.createElement('img');
image.className = 'mc-header-search__image';
image.loading = 'lazy';
image.alt = product.featured_image?.alt || '';
image.src = product.featured_image.url;
link.append(image);
} else {
const image = document.createElement('span');
image.className = 'mc-header-search__image';
image.setAttribute('aria-hidden', 'true');
link.append(image);
}
const copy = document.createElement('div');
const title = document.createElement('p');
title.className = 'mc-header-search__title';
title.textContent = product.title;
const price = document.createElement('p');
price.className = 'mc-header-search__price';
price.textContent = formatPrice(product.price);
copy.append(title, price);
link.append(copy);
results.append(link);
});
setPanelOpen(true);
};
const search = async (query) => {
if (!suggestUrl) return;
controller?.abort();
controller = new AbortController();
results.replaceChildren(message(context.messages.searching));
setPanelOpen(true);
try {
const url = new URL(suggestUrl, window.location.origin);
url.searchParams.set('q', query);
url.searchParams.set('resources[type]', 'product');
url.searchParams.set('resources[limit]', '6');
url.searchParams.set('resources[options][unavailable_products]', 'last');
const response = await fetch(url, { headers: { Accept: 'application/json' }, signal: controller.signal });
if (!response.ok) throw new Error(`Search failed: ${response.status}`);
const data = await response.json();
render(data?.resources?.results?.products || []);
} catch (error) {
if (error.name === 'AbortError') return;
results.replaceChildren(message(context.messages.error));
setPanelOpen(true);
}
};
input.addEventListener('focus', () => setPanelOpen(true));
input.addEventListener('input', () => {
window.clearTimeout(timer);
const query = input.value.trim();
if (query.length < 2) {
results.replaceChildren();
setPanelOpen(true);
return;
}
timer = window.setTimeout(() => search(query), 180);
});
input.addEventListener('keydown', (event) => {
const options = Array.from(results.querySelectorAll('[role="option"]'));
if (event.key === 'Escape') {
event.preventDefault();
setPanelOpen(false);
} else if (event.key === 'ArrowDown' && options.length) {
event.preventDefault();
options[0].focus();
}
});
results.addEventListener('keydown', (event) => {
const options = Array.from(results.querySelectorAll('[role="option"]'));
const index = options.indexOf(document.activeElement);
if (index < 0) return;
if (event.key === 'ArrowDown') {
event.preventDefault();
options[(index + 1) % options.length].focus();
} else if (event.key === 'ArrowUp') {
event.preventDefault();
if (index === 0) input.focus();
else options[index - 1].focus();
} else if (event.key === 'Escape') {
event.preventDefault();
input.focus();
setPanelOpen(false);
}
});
form.addEventListener('submit', (event) => {
if (context.placeholderLinks) event.preventDefault();
});
document.addEventListener('pointerdown', (event) => {
if (!host.contains(event.target)) setPanelOpen(false);
});
}
function boot(scope = document) {
scope.querySelectorAll('[data-mc-header]').forEach(init);
}
boot();
document.addEventListener('shopify:section:load', (event) => boot(event.target));
})();
