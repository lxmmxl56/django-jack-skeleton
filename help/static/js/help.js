'use strict';

import {
  $,
  $$
} from './utils/query.js';

let ticking = false;
const navbar = document.querySelector(".navbar");
// const helpText = document.querySelector("#helpText");
const section = $$(".anchor");
const sections = {};
let i = 0;

const rem = parseInt(getComputedStyle(document.documentElement).fontSize);
// there's a 1 rem margin (2 total, top + bottom) on the sidebar
const offset = 2 * rem + navbar.offsetHeight;

Array.prototype.forEach.call(section, function(e) {
  // subtract 1 pixel to prevent subpixel issues
  sections[e.id] = e.offsetTop - 1;
});
const last = Object.keys(sections)[Object.keys(sections).length - 1];


window.addEventListener('load', function() {
  const $sidebar = $("#helpSidebarMenu");
  let lastScrollTop = window.scrollTop;
  let wasScrollingDown = true;

  const halfOffset = offset/2;
  const windowHeight = Math.abs(window.innerHeight - offset);
  const sidebarHeight = $sidebar.offsetHeight;
  const isWindowLarger = (windowHeight > sidebarHeight);
  // const isWindowLarger = true;

  if (!isWindowLarger) {
    window.onscroll = function() {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          checkSidebarScrollPosition();
          highlightCurrentSection();
          ticking = false;
        });
        ticking = true;
      }
    };
    checkSidebarScrollPosition();
    highlightCurrentSection();
  } else {
    window.onscroll = function() {
      if (!ticking) {
        window.requestAnimationFrame(function() {
          highlightCurrentSection();
          ticking = false;
        });
        ticking = true;
      }
    };
    highlightCurrentSection();
  }

  function checkSidebarScrollPosition() {
    const bodyHeight = document.body.clientHeight;
    const windowHeight = Math.abs(window.innerHeight);
    const sidebarHeight = $sidebar.offsetHeight;
    const scrollTop = window.scrollY;
    const scrollBottom = scrollTop + windowHeight;
    const sidebarTop = $sidebar.getBoundingClientRect().top - halfOffset;
    const sidebarBottom = sidebarTop + sidebarHeight + offset;
    const heightDelta = Math.abs(windowHeight - sidebarHeight - offset);
    // const scrollDelta = (lastScrollTop - scrollTop) * sidebarHeight/bodyHeight;
    const scrollDelta = lastScrollTop - scrollTop;
    const isScrollingDown = (scrollTop > lastScrollTop);
    const isPageAtTop = scrollTop <= 0;
    const isWindowLarger = (windowHeight - offset > sidebarHeight);
    if (isPageAtTop) {
      const newTop = scrollTop;
      $sidebar.style.top = newTop + 'px';
    }
    const initialSidebarTop = $sidebar.offsetTop;
    if ((isWindowLarger && scrollTop > initialSidebarTop) || (!isWindowLarger && scrollTop > initialSidebarTop)) {
      $sidebar.classList.add('scrolling');
    } else if (!isScrollingDown && scrollTop <= initialSidebarTop) {
      $sidebar.classList.remove('scrolling');
    }
    const dragBottomDown = (sidebarBottom + scrollDelta <= windowHeight && isScrollingDown);
    const dragTopUp = (sidebarTop >= 0 && !isScrollingDown);
    if (dragBottomDown) {
      if (isWindowLarger && isPageAtTop) {
        const newTop = scrollTop;
        $sidebar.style.top = newTop + 'px';
      } else if (isWindowLarger) {
        $sidebar.style.top = 0;
      } else {
        $sidebar.style.top = -heightDelta + 'px';
      }
    } else if (dragTopUp) {
      const newTop = (isPageAtTop) ? scrollTop : 0;
      $sidebar.style.top = newTop + 'px';
    } else if ($sidebar.classList.contains('scrolling')) {
      const currentTop = parseInt($sidebar.style.top, 10);
      const minTop = -heightDelta;
      const scrolledTop = currentTop + scrollDelta;
      const isPageAtBottom = (scrollTop + windowHeight >= bodyHeight);
      const isPageAtTop = scrollTop <= initialSidebarTop;
      let newTop = (isPageAtBottom) ? minTop : scrolledTop;
      if (newTop > 0) {
        newTop = 0;
      }
      $sidebar.style.top = newTop + 'px';
    }
    lastScrollTop = scrollTop;
    wasScrollingDown = isScrollingDown;
  }

  function highlightCurrentSection() {
    const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
    for (i in sections) {
      if (scrollPosition + window.innerHeight >= document.body.offsetHeight) {
        const collapseActive = $('.collapse-nav-link.active');
        collapseActive && collapseActive.classList.remove('active');
        $('a.collapse-nav-link[href*=' + last + ']').classList.add('active');
        const offcanvasActive = $('.offcanvas-nav-link.active');
        offcanvasActive && offcanvasActive.classList.remove('active');
        $('a.offcanvas-nav-link[href*=' + last + ']').classList.add('active');
      }
      else if (sections[i] <= scrollPosition) {
        const collapseActive = $('.collapse-nav-link.active');
        collapseActive && collapseActive.classList.remove('active');
        $('a.collapse-nav-link[href*=' + i + ']').classList.add('active');
        const offcanvasActive = $('.offcanvas-nav-link.active');
        offcanvasActive && offcanvasActive.classList.remove('active');
        $('a.offcanvas-nav-link[href*=' + i + ']').classList.add('active');
      }
    }
  }
});

// function scrollSpyHelpText(scrollPosition) {
//   for (i in sections) {
//     if (scrollPosition + helpText.offsetHeight >= helpText.scrollHeight) {
//       const active = document.querySelector('.active');
//       active && active.classList.remove('active');
//       document.querySelector('a[href*=' + last + ']').classList.add('active');
//     }
//     else if (sections[i] <= scrollPosition) {
//       const active = document.querySelector('.active');
//       active && active.classList.remove('active');
//       document.querySelector('a[href*=' + i + ']').classList.add('active');
//     }
//   }
// }

// helpText.onscroll = function(e) {
//   const scrollPosition = helpText.scrollTop + offset;
//   if (!ticking) {
//     window.requestAnimationFrame(function() {
//       scrollSpyHelpText(scrollPosition);
//       ticking = false;
//     });
//     ticking = true;
//   }
// };


