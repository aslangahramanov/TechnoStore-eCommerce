'use strict'

// ------------HEADER SCRIPTS---------------






// ------------HEADER SCRIPTS---------------



// ------------SLIDER SCRIPTS---------------

let slideWidth = document.querySelector('#sectionSlider .secOne .slider').clientWidth;
let slider = document.querySelector('#sectionSlider .secOne ul');
let sliderLength = document.querySelectorAll('#sectionSlider .secOne .slider ul li').length;

let nextBtn = document.querySelector('#sectionSlider .secOne .sliderBtn .nextBtn');
let prevBtn = document.querySelector('#sectionSlider .secOne .sliderBtn .prevBtn');

slider.style.width = slideWidth * sliderLength + 'px';


let c = 0

prevBtn.addEventListener('click', function () {
    SliderPrev()
})

nextBtn.addEventListener('click', function () {
    SliderNext()
})

function SliderNext() {
    c++;
    if (c == sliderLength) {
        c = 0;
    }
    slider.style.left = -(c * slideWidth) + 'px';
}

function SliderPrev() {
    c--;
    if (c == -1) {
        c = sliderLength - 1;
    }
    slider.style.left = -(c * slideWidth) + 'px';
}

let SliderInt = setInterval(SliderNext, 5000)

// ------------SLIDER SCRIPTS---------------



let category = document.querySelector('#secHeader .category')
let droppedCategory = document.querySelector('#secHeader .openCategory')





category.addEventListener('click', () => {
    droppedCategory.classList.toggle('active')
    category.classList.toggle('active')
})





let tabBtn = $('#allProducts .tabMenu ul li')
let content = $('#allProducts .showProduct')



$(document).ready(function () {
    tabBtn.filter(':first').addClass('is_active')
    content.filter(':not(:first)').hide()

    tabBtn.click(function () {
        var index = $(this).index()
        tabBtn.removeClass('is_active').eq(index).addClass('is_active')
        content.hide().eq(index).fadeIn(500)
    })
})


let cartBtn = document.querySelector('#secHeader .userProg .cart-icon')
let cartUp = document.querySelector('#secHeader .userProg .cart-up')
let x_icon = document.querySelector('#secHeader .userProg .cart-up .xmark')

cartBtn.addEventListener('click', () => {
    cartUp.classList.toggle('cart_active')
})

x_icon.addEventListener('click', () =>{
    cartUp.classList.remove('cart_active')
})