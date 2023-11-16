document.addEventListener("scroll", function() {
    var navbar = document.querySelector(".navbar");
    var navLinks = document.querySelectorAll(".nav-link"); 
    if (window.pageYOffset > 1) {  
        navbar.classList.remove("transparent-bg");
        navbar.classList.add("fade-in-slide-down");
        navbar.classList.add("shadow-on");
        
    } else {
        navbar.classList.add("transparent-bg");
        navbar.classList.remove("fade-in-slide-down");
        navbar.classList.remove("shadow-on");
        
    }
});
document.addEventListener("scroll", function() {
    var navLinks = document.querySelectorAll(".nav-link"); 

    if (window.pageYOffset > 1) {
        navLinks.forEach(function(link) {
            link.classList.add("tran-color"); 
        });
    } else {
        navLinks.forEach(function(link) {
            link.classList.remove("tran-color");
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    var navbar = document.querySelector('.navbar.custom-navbar');
    
    // 当动画结束后移除这个类
    navbar.addEventListener('animationend', function() {
        navbar.classList.remove('fade-in-on-load');
    });
});
document.addEventListener("scroll", function() {
    var image = document.getElementById("dynamicImage"); // 获取图像元素

    if (window.pageYOffset > 1) {  // 假设在滚动超过 200px 时切换图像
        image.src = "../img/logo2.png"; // 更改图像的 src
    } else {
        image.src = "../img/logo3.png"; // 滚动回顶部时恢复初始图像
    }
});
