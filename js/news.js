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
        image.src = "img/logo2.png"; // 更改图像的 src
    } else {
        image.src = "img/logo3.png"; // 滚动回顶部时恢复初始图像
    }
});
document.addEventListener("DOMContentLoaded", function() {
    setTimeout(function() {
        checkVisibilityAndAnimate();
    }, 50);

    document.addEventListener("scroll", checkVisibilityAndAnimate);
});

function checkVisibilityAndAnimate() {
    var animatedElems = document.querySelectorAll(".animate-on-scroll:not(.img-fade-in)");

    animatedElems.forEach(function(elem) {
        var rect = elem.getBoundingClientRect();
        
        // 检查元素是否至少部分在视窗中
        var isVisible = rect.top < window.innerHeight && rect.bottom >= 0;

        if (isVisible) {
            elem.classList.add("img-fade-in");
        }
    });
}
function fetchNews(page) {
    
    fetch(`https://60.204.251.61:8000/api/news/?page=${page}`)
        .then(response => response.json())
        .then(data => {
            
            const newsList = data.results;  // 使用分页后的结果
            const container = document.getElementById('news-container');
            container.innerHTML = '';  // 清空现有内容

            // 将新闻列表倒序排列
            newsList.forEach(news => {
                // 创建新闻卡片的HTML结构
                const newsItem = `
                    <div class="col-lg-4 fade-in animate-on-scroll">
                        <div class="card  border-0 card-news" onclick="fetchNewsDetail(${news.id}, ${page})">
                            <p><span class="type">${news.type}</span></p>
                            <img src="${news.image.image}" class="img-fit" >
                            <div class="card-body">
                                <div class="mt-auto">
                                    <p>
                                        <span class="font font-change">${new Date(news.uploadtime).toLocaleDateString()}</span>
                                    </p>
                                    <h5>
                                        <span class="font font-change" style="font-weight:bold;">${news.title}</span>
                                    </h5>
                                </div>
                            </div>
                        </div>
                    </div>`;
                container.innerHTML += newsItem;
            });
            createPagination(data.count, 9, page); // 假设每页有9项
        })
        .catch(error => console.error('Error:', error));
}
function createPagination(totalCount, pageSize, currentPage) {
    const totalPages = Math.ceil(totalCount / pageSize);
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';  // 清空现有分页导航

    // 添加分页按钮
    for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement('button');
        pageButton.innerText = i;
        pageButton.onclick = function () { fetchNews(i); };
        pageButton.disabled = i === currentPage;

        paginationContainer.appendChild(pageButton);
    }
}

document.addEventListener('DOMContentLoaded', () => fetchNews(1));

function fetchNewsDetail(newsId,page) {
    sessionStorage.setItem('currentPage', page);
    // 隐藏新闻列表容器
    const newsContainer = document.getElementById('news-container');
    newsContainer.style.display = 'none';
    const pagination = document.getElementById('pagination')
    pagination.style.display = 'none';

    // 请求新闻详细信息
    fetch(`http://127.0.0.1:8000/api/news/${newsId}/`)
        .then(response => response.json())
        .then(news => {
            const detailContainer = document.getElementById('news-detail-container');
            const markdownContent = news.context; // 这是 Markdown 格式的内容
            const htmlContent = marked.parse(markdownContent); 
            const newsDetailHTML = `
            
                <div>
                    <p><span class="type1">${news.type}</span><span class="font font-change">${new Date(news.uploadtime).toLocaleDateString()}</span></p>
                    <h1>${news.title}</h1>
                    <div>${htmlContent}</div> <!-- 显示转换后的 HTML 内容 -->
                    <div class="row align-items-center justify-content-center">
                    <button class="modern-button" onclick="goBack()">Back</button>

                    </div>
                    
                </div>`;
            detailContainer.innerHTML = newsDetailHTML;
            detailContainer.style.display = 'block';  // 显示新闻详细信息
        })
        .catch(error => console.error('Error:', error));
}
function goBack() {
    const detailContainer = document.getElementById('news-detail-container');
    const newsContainer = document.getElementById('news-container');
    const pagination = document.getElementById('pagination');

    // 隐藏新闻详细信息
    detailContainer.style.display = 'none';

    // 重新显示新闻列表和分页导航
    newsContainer.style.display = 'flex';
    pagination.style.display = 'flex';

}
