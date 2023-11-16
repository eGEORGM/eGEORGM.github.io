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

// document.addEventListener("scroll", function() {
//     var animatedElems = document.querySelectorAll(".animate-on-scroll");  // 获取所有需要动画的元素

//     animatedElems.forEach(function(elem) {
//         var rect = elem.getBoundingClientRect();
        
//         if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
//             elem.classList.add("img-fade-in");
//         }
//     });
// });
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        checkVisibilityAndAnimate();
    }, 50);  // slight delay to ensure elements are rendered

    document.addEventListener("scroll", checkVisibilityAndAnimate);
});
function checkVisibilityAndAnimate() {
    var animatedElems = document.querySelectorAll(".animate-on-scroll:not(.img-fade-in)");

    animatedElems.forEach(function(elem) {
        var rect = elem.getBoundingClientRect();
        
        if (rect.top >= 0 && rect.bottom <= window.innerHeight) {
            elem.classList.add("img-fade-in");
        }
    });
}
$(document).ready(function() {
    // 当窗口大小改变时执行
    $(window).resize(function() {
        var width = $(window).width();
        if (width <= 991) {
            $('.school-herf').addClass('row-cols-2');
        } else {
            $('.school-herf').removeClass('row-cols-2');
        }
    });

    // 触发 resize 以便在页面加载时应用
    $(window).trigger('resize');
});
document.addEventListener("scroll", function() {
    var image = document.getElementById("dynamicImage"); // 获取图像元素

    if (window.pageYOffset > 1) {  // 假设在滚动超过 200px 时切换图像
        image.src = "img/logo2.png"; // 更改图像的 src
    } else {
        image.src = "img/logo3.png"; // 滚动回顶部时恢复初始图像
    }
});
