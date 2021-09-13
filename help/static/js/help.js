'use strict';

let ticking = false;
const navbar = document.querySelector(".navbar");
const helpText = document.querySelector("#helpText");
const section = document.querySelectorAll(".anchor");
const sections = {};
let i = 0;

const rem = parseInt(getComputedStyle(document.documentElement).fontSize);
const offset = rem + navbar.offsetHeight;

Array.prototype.forEach.call(section, function(e) {
    sections[e.id] = e.offsetTop;
});
const last = Object.keys(sections)[Object.keys(sections).length - 1];

function scrollSpyHelpText(scrollPosition) {
    for (i in sections) {
        if (scrollPosition + helpText.offsetHeight >= helpText.scrollHeight) {
            const active = document.querySelector('.active');
            active && active.classList.remove('active');
            document.querySelector('a[href*=' + last + ']').classList.add('active');
        }
        else if (sections[i] <= scrollPosition) {
            const active = document.querySelector('.active');
            active && active.classList.remove('active');
            document.querySelector('a[href*=' + i + ']').classList.add('active');
        }
    }
}

helpText.onscroll = function(e) {
    const scrollPosition = helpText.scrollTop + offset;
    if (!ticking) {
        window.requestAnimationFrame(function() {
            scrollSpyHelpText(scrollPosition);
            ticking = false;
        });
        ticking = true;
    }
};
