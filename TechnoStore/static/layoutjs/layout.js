let category = document.querySelector('#category-button')
let droppedCategory = document.querySelector('#secHeader .openCategory')





category.addEventListener('click', () => {
    droppedCategory.classList.toggle('active')
    category.classList.toggle('active')
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