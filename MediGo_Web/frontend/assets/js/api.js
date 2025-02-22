// Fetch and display doctors list
async function fetchDoctors() {
    try {
        const response = await fetch("http://127.0.0.1:8000/doctors");
        const doctors = await response.json();
        let doctorSelect = document.getElementById("doctor");
        doctors.forEach((doc) => {
            doctorSelect.innerHTML += `<option value="${doc.id}">${doc.name} - ${doc.specialization}</option>`;
        });
    } catch (error) {
        console.error("Error fetching doctors:", error);
    }
}

// Handle appointment booking
document.getElementById("appointment-form")?.addEventListener("submit", async function(e) {
    e.preventDefault();
    const name = document.getElementById("name").value;
    const doctorId = document.getElementById("doctor").value;
    const date = document.getElementById("date").value;

    const response = await fetch("http://127.0.0.1:8000/appointments", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, doctorId, date }),
    });

    if (response.ok) {
        alert("Appointment booked successfully!");
    } else {
        alert("Failed to book appointment");
    }
});

// Load doctors on page load
document.addEventListener("DOMContentLoaded", fetchDoctors);
