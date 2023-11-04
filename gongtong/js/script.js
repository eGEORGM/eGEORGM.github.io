// $(function() {
//     function updateCarousel() {
//       // 每次轮播事件触发时，更新图片的样式
//       $('#myCarousel .carousel-item').each(function() {
//         if ($(this).hasClass('active')) {
//           // 如果图片是当前显示的图片，设置为最大大小
//           $(this).find('img').css({width: '100%', height: '100%'});
//         } else {
//           // 如果图片不是当前显示的图片，设置为较小的大小
//           $(this).find('img').css({width: '80%', height: '80%'});
//         }
//       });
//     }
//     $('#myCarousel').on('slide.bs.carousel', updateCarousel);
//     updateCarousel();
//   });
//   $('#carouselExampleIndicators').on('slide.bs.carousel', function (e) {
//     var $e = $(e.relatedTarget);
//     var idx = $e.index();
//     var itemsPerSlide = 3;
//     var totalItems = $('.carousel-item').length;

//     if (idx >= totalItems - (itemsPerSlide - 1)) {
//         var it = itemsPerSlide - (totalItems - idx);
//         for (var i = 0; i < it; i++) {
//             // append slides to end
//             if (e.direction === 'left') {
//                 $('.carousel-item').eq(i).appendTo('.carousel-inner');
//             } else {
//                 $('.carousel-item').eq(0).appendTo('.carousel-inner');
//             }
//         }
//     }
// });
// $(document).ready(function() {
//   $(".carousel-control-prev.multi-carousel-control").click(function() {
//     $("#carouselExampleIndicators1").carousel('prev');
//     $("#carouselExampleIndicators2").carousel('prev');
//     $("#carouselExampleIndicators3").carousel('prev');
//   });

//   $(".carousel-control-next.multi-carousel-control").click(function() {
//     $("#carouselExampleIndicatorsl1").carousel('next');
//     $("#carouselExampleIndicators2").carousel('next');
//     $("#carouselExampleIndicators3").carousel('next');
//   });
// });
// $(document).ready(function() {
//   $('.multi-carousel-control').click(function() {
//     var targetCarousel = $(this).parent().attr('id');
//     switch (targetCarousel) {
//       case 'carouselExampleIndicators1':
//         $('#carouselExampleIndicators2').carousel('prev');
//         $('#carouselExampleIndicators3').carousel('prev');
//         break;
//       case 'carouselExampleIndicators2':
//         $('#carouselExampleIndicators1').carousel('prev');
//         $('#carouselExampleIndicators3').carousel('prev');
//         break;
//       case 'carouselExampleIndicators3':
//         $('#carouselExampleIndicators1').carousel('prev');
//         $('#carouselExampleIndicators2').carousel('prev');
//         break;
//       default:
//         console.log('No matching carousel id found.');
//     }
//   });
// });
// $(document).ready(function() {
//   // 为每个轮播图添加监听器
//   $('#carouselExampleIndicators1, #carouselExampleIndicators2, #carouselExampleIndicators3').on('slide.bs.carousel', function (event) {
//       // 获取下一个将显示的幻灯片的索引
//       var nextSlideIndex = $(event.relatedTarget).index();

//       // 将其他两个轮播图同步到这个索引
//       $('#carouselExampleIndicators1, #carouselExampleIndicators2, #carouselExampleIndicators3').not(this).each(function() {
//           $(this).carousel(nextSlideIndex);
//       });
//   });
// });
$(document).ready(function() {
  var numSlides = 5; // 设定每个轮播图的图片数量

  $('#carouselExampleIndicators2').on('slide.bs.carousel', function (event) {
      var nextSlideIndex = $(event.relatedTarget).index();

      // 为轮播图1设置前一张图片的索引
      var prevSlideIndex = (nextSlideIndex - 1 + numSlides) % numSlides;
      $('#carouselExampleIndicators1').carousel(prevSlideIndex);

      // 为轮播图3设置后一张图片的索引
      var nextSlideIndexFor3 = (nextSlideIndex + 1) % numSlides;
      $('#carouselExampleIndicators3').carousel(nextSlideIndexFor3);
  });
});
$(document).ready(function() {
  $('#carouselExampleIndicators2').on('slide.bs.carousel', function (event) {
      var nextSlideIndex = $(event.relatedTarget).index();
      $('#carouselExampleIndicators1').carousel(nextSlideIndex);
      $('#carouselExampleIndicators3').carousel(nextSlideIndex);
  });
});