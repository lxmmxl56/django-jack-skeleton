'use strict';

const section = document.querySelectorAll(".anchor");
const sections = {};
let i = 0;

const rem = parseInt(getComputedStyle(document.documentElement).fontSize);

Array.prototype.forEach.call(section, function(e) {
    sections[e.id] = e.offsetTop;
});
const last = Object.keys(sections)[Object.keys(sections).length - 1];

window.onscroll = function() {
    const scrollPosition = document.documentElement.scrollTop || document.body.scrollTop;
    for (i in sections) {
        if (scrollPosition + window.innerHeight >= document.body.offsetHeight) {
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
};
