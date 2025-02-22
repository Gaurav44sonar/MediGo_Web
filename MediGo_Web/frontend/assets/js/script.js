document.addEventListener("DOMContentLoaded", function () {
    loadNavbar();
    loadFooter();
    setupFormHandlers();
});

// ✅ Load Navbar dynamically
function loadNavbar() {
    const navbar = document.getElementById("navbar");
    if (navbar) {
        navbar.innerHTML = `
            <nav class="navbar">
                <a href="index.html">Home</a>
                <a href="doctors.html">Find a Doctor</a>
                <a href="appointment.html">Book Appointment</a>
                <a href="login.html">Login</a>
                <a href="register.html">Register</a>
            </nav>
        `;
    }
}

// ✅ Load Footer dynamically
function loadFooter() {
    const footer = document.getElementById("footer");
    if (footer) {
        footer.innerHTML = `
            <footer class="footer">
                <p>&copy; 2025 DocLink. All Rights Reserved.</p>
            </footer>
        `;
    }
}

// ✅ Form Handlers for Login & Registration
function setupFormHandlers() {
    const loginForm = document.getElementById("login-form");
    if (loginForm) {
        loginForm.addEventListener("submit", function (event) {
            event.preventDefault();
            loginUser();
        });
    }

    const registerForm = document.getElementById("register-form");
    if (registerForm) {
        registerForm.addEventListener("submit", function (event) {
            event.preventDefault();
            registerUser();
        });
    }
}

// ✅ Handle User Login
function loginUser() {
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!email || !password) {
        alert("Please fill all fields.");
        return;
    }

    // Simulating API call (Replace this with actual backend call)
    console.log("Logging in:", { email, password });

    alert("Login successful! Redirecting...");
    window.location.href = "index.html";
}

// ✅ Handle User Registration
function registerUser() {
    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    if (!name || !email || !password) {
        alert("Please fill all fields.");
        return;
    }

    console.log("Registering user:", { name, email, password });

    alert("Registration successful! Redirecting to login...");
    window.location.href = "login.html";
}
