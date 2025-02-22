document.addEventListener("DOMContentLoaded", function () {
    // Define Navbar and Footer HTML
    const navbarHTML = `
        <div class="container-fluid sticky-top bg-white shadow-sm mb-5">
            <div class="container">
                <nav class="navbar navbar-expand-lg bg-white navbar-light py-3 py-lg-0">
                    <a href="index.html" class="navbar-brand">
                        <h1 class="m-0 text-uppercase text-primary"><i class="fa fa-clinic-medical me-2"></i>MediGo</h1>
                    </a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="navbarCollapse">
                        <div class="navbar-nav ms-auto py-0">
                            <a href="index.html" class="nav-item nav-link">Home</a>
                            <a href="about.html" class="nav-item nav-link">About</a>
                            <a href="service.html" class="nav-item nav-link">Service</a>
                           
                            <a href="contact.html" class="nav-item nav-link">Contact</a>
                        </div>
                    </div>
                </nav>
            </div>
        </div>
    `;

    const footerHTML = `
        <div class="container-fluid bg-dark text-light mt-5 py-5">
            <div class="container py-5">
                <div class="row g-5">
                    <div class="col-lg-3 col-md-6">
                        <h4 class="text-primary text-uppercase border-bottom border-5 border-secondary mb-4">Get In Touch</h4>
                        <p class="mb-4">No dolore ipsum accusam no lorem. Invidunt sed clita kasd clita et et dolor sed dolor</p>
                        <p class="mb-2"><i class="fa fa-map-marker-alt text-primary me-3"></i>123 Street, New York, USA</p>
                        <p class="mb-2"><i class="fa fa-envelope text-primary me-3"></i>info@example.com</p>
                        <p class="mb-0"><i class="fa fa-phone-alt text-primary me-3"></i>+012 345 67890</p>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Inject Navbar and Footer
    document.getElementById("navbar-container").innerHTML = navbarHTML;
    document.getElementById("footer-container").innerHTML = footerHTML;

    // // Dropdown Hover Effect
    // function toggleNavbarHover() {
    //     if (window.innerWidth > 992) {
    //         document.querySelectorAll('.navbar .dropdown').forEach(dropdown => {
    //             dropdown.addEventListener('mouseenter', () => {
    //                 dropdown.querySelector('.dropdown-toggle').click();
    //             });
    //             dropdown.addEventListener('mouseleave', () => {
    //                 dropdown.querySelector('.dropdown-toggle').click();
    //             });
    //         });
    //     } else {
    //         document.querySelectorAll('.navbar .dropdown').forEach(dropdown => {
    //             dropdown.removeEventListener('mouseenter', () => {});
    //             dropdown.removeEventListener('mouseleave', () => {});
    //         });
    //     }
    // }
    // toggleNavbarHover();
    // window.addEventListener('resize', toggleNavbarHover);

    // // Back to Top Button
    // const backToTop = document.createElement("button");
    // backToTop.className = "back-to-top";
    // backToTop.innerHTML = "⬆";
    // document.body.appendChild(backToTop);

    // function toggleBackToTop() {
    //     if (window.scrollY > 100) {
    //         backToTop.style.display = "block";
    //     } else {
    //         backToTop.style.display = "none";
    //     }
    // }
    // window.addEventListener("scroll", toggleBackToTop);

    // backToTop.addEventListener("click", function () {
    //     window.scrollTo({ top: 0, behavior: "smooth" });
    // });

    // // Carousel Setup (for Owl Carousel)
    // function setupCarousel(selector, options) {
    //     const carousel = document.querySelector(selector);
    //     if (carousel) {
    //         new Glide(selector, options).mount();
    //     }
    // }

    // setupCarousel(".price-carousel", { type: "carousel", autoplay: 1000, perView: 3 });
    // setupCarousel(".team-carousel", { type: "carousel", autoplay: 1000, perView: 2 });
    // setupCarousel(".testimonial-carousel", { type: "carousel", autoplay: 1000, perView: 1 });
});
{/* <a href="price.html" class="nav-item nav-link">Pricing</a>
<div class="nav-item dropdown">
    <a href="#" class="nav-link dropdown-toggle active" data-bs-toggle="dropdown">Pages</a>
    <div class="dropdown-menu m-0">
        <a href="blog.html" class="dropdown-item">Blog Grid</a>
        <a href="detail.html" class="dropdown-item active">Blog Detail</a>
        <a href="team.html" class="dropdown-item">The Team</a>
        <a href="testimonial.html" class="dropdown-item">Testimonial</a>
        <a href="appointment.html" class="dropdown-item">Appointment</a>
        <a href="search.html" class="dropdown-item">Search</a>
    </div>
</div> */}