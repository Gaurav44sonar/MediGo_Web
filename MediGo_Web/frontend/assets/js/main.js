// (function ($) {
//     "use strict";

//     // Load Navbar and Footer dynamically
//     $(document).ready(function () {
//         // Load Navbar
//         $("#navbar-container").load("../frontend/components/footer.html", function () {
//             console.log("Navbar loaded successfully.");
//         });

//         // Load Footer
//         $("#footer-container").load("../frontend/components/footer.html", function () {
//             console.log("Footer loaded successfully.");
//         });

//         // Function to handle dropdowns on hover
//         function toggleNavbarMethod() {
//             if ($(window).width() > 992) {
//                 $('.navbar .dropdown').on('mouseover', function () {
//                     $('.dropdown-toggle', this).trigger('click');
//                 }).on('mouseout', function () {
//                     $('.dropdown-toggle', this).trigger('click').blur();
//                 });
//             } else {
//                 $('.navbar .dropdown').off('mouseover').off('mouseout');
//             }
//         }
//         toggleNavbarMethod();
//         $(window).resize(toggleNavbarMethod);
//     });

//     // Date and time picker
//     $('.date').datetimepicker({
//         format: 'L'
//     });
//     $('.time').datetimepicker({
//         format: 'LT'
//     });

//     // Back to top button
//     $(window).scroll(function () {
//         if ($(this).scrollTop() > 100) {
//             $('.back-to-top').fadeIn('slow');
//         } else {
//             $('.back-to-top').fadeOut('slow');
//         }
//     });
//     $('.back-to-top').click(function () {
//         $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
//         return false;
//     });

//     // Price carousel
//     $(".price-carousel").owlCarousel({
//         autoplay: true,
//         smartSpeed: 1000,
//         margin: 45,
//         dots: false,
//         loop: true,
//         nav : true,
//         navText : [
//             '<i class="bi bi-arrow-left"></i>',
//             '<i class="bi bi-arrow-right"></i>'
//         ],
//         responsive: {
//             0: { items: 1 },
//             992: { items: 2 },
//             1200: { items: 3 }
//         }
//     });

//     // Team carousel
//     $(".team-carousel, .related-carousel").owlCarousel({
//         autoplay: true,
//         smartSpeed: 1000,
//         margin: 45,
//         dots: false,
//         loop: true,
//         nav : true,
//         navText : [
//             '<i class="bi bi-arrow-left"></i>',
//             '<i class="bi bi-arrow-right"></i>'
//         ],
//         responsive: {
//             0: { items: 1 },
//             992: { items: 2 }
//         }
//     });

//     // Testimonials carousel
//     $(".testimonial-carousel").owlCarousel({
//         autoplay: true,
//         smartSpeed: 1000,
//         items: 1,
//         dots: true,
//         loop: true,
//     });

// })(jQuery);

document.addEventListener("DOMContentLoaded", function () {
    // Detects the correct path based on how deep the current file is
    let depth = window.location.pathname.split("/").length;
    let basePath = depth > 3 ? "../../.." : depth > 2 ? "../.." : ".";

    console.log("🔍 Base Path:", basePath); // Debugging output

    // Load Navbar
    fetch(`${basePath}/frontend/components/navbar.html`)
        .then(response => {
            if (!response.ok) throw new Error("Navbar not found");
            return response.text();
        })
        .then(data => {
            document.getElementById("navbar-container").innerHTML = data;
        })
        .catch(error => console.error("❌ Error loading navbar:", error));

    // Load Footer
    fetch(`${basePath}/frontend/components/footer.html`)
        .then(response => {
            if (!response.ok) throw new Error("Footer not found");
            return response.text();
        })
        .then(data => {
            document.getElementById("footer-container").innerHTML = data;
        })
        .catch(error => console.error("❌ Error loading footer:", error));
});
