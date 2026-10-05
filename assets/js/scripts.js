'use strict';

document.documentElement.classList.add('js');

const menuToggle = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#site-nav');
const mobileLayout = window.matchMedia('(max-width: 900px)');

function closeMenu(returnFocus = false) {
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', '開啟導覽選單');
    navigation.classList.remove('is-open');
    if (returnFocus) menuToggle.focus();
}

menuToggle.addEventListener('click', () => {
    const opening = menuToggle.getAttribute('aria-expanded') !== 'true';
    menuToggle.setAttribute('aria-expanded', String(opening));
    menuToggle.setAttribute('aria-label', opening ? '關閉導覽選單' : '開啟導覽選單');
    navigation.classList.toggle('is-open', opening);
});

navigation.addEventListener('click', event => {
    if (event.target.closest('a') && mobileLayout.matches) closeMenu();
});

document.addEventListener('keydown', event => {
    if (event.key === 'Escape' && menuToggle.getAttribute('aria-expanded') === 'true') closeMenu(true);
});

document.addEventListener('click', event => {
    if (!event.target.closest('.site-header')) closeMenu();
});

mobileLayout.addEventListener('change', () => closeMenu());

document.querySelector('#copyright-year').textContent = new Date().getFullYear();

// Preserve older product and retailer links after the move to separate pages.
if (location.pathname === '/' || location.pathname === '/index.html') {
    const previousSections = {
        '#product': '/products/cocoa/',
        '#about': '/about/',
        '#ritual': '/rituals/',
        '#portfolio': '/rituals/',
        '#shop': '/shop/',
        '#services': '/shop/',
        '#faq': '/products/cocoa/#faq'
    };
    if (previousSections[location.hash]) location.replace(previousSections[location.hash]);
}
