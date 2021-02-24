let btnNav = document.querySelector(".btn-nav");
let navContainer = document.querySelector(".nav-menu");
let btnClose = document.querySelector(".btn-close");

btnNav.addEventListener("click", openNavMenu);
btnClose.addEventListener("click", closeNavMenu);

function openNavMenu() {
  navContainer.style.display = "block";
}

function closeNavMenu() {
  navContainer.style.display = "none";
}
