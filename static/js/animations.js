'use strict'


async function animateNavBar() {
    var navContainer = document.getElementById("nav");
    let visor = document.getElementById('conte-view-form')
    var nav = document.getElementById("nav-bar");
    let elementoEstilo = window.getComputedStyle(visor);
    let display= elementoEstilo.getPropertyValue("display");
    if (display == 'none') {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            navContainer.style.height = "60px"
            navContainer.style.position = "fixed"
            navContainer.style.zIndex = "3"
            navContainer.style.top = "0"
            nav.style.width ="100%"
            navContainer.style.transition = 'all 1.2s ease-in-out';
            nav.style.transition = 'all 1.2s ease-in-out';
    }
    else {
        nav.style.width ="50%"
        navContainer.style.height = "40px"
        navContainer.style.position = "absolute"
        navContainer.style.removeProperty("top")

    }
    }
    
}