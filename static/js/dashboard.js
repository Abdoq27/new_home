// Filter Users by Search
document.getElementById("user-search").addEventListener("input", function (event) {
    const searchTerm = event.target.value.toLowerCase();
    const userRows = document.querySelectorAll(".user-row");

    userRows.forEach(row => {
        const userName = row.querySelector(".user-name").textContent.toLowerCase();
        if (userName.includes(searchTerm)) {
            row.style.display = ""; // Show matching row
        } else {
            row.style.display = "none"; // Hide non-matching row
        }
    });
});

// Assign Course to User
document.getElementById("assign-course-button").addEventListener("click", function () {
    const userId = document.getElementById("assign-user-id").value.trim();
    const courseId = document.getElementById("assign-course-id").value.trim();

    if (userId && courseId) {
        fetch("/assign_course", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ user_id: userId, course_id: courseId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert("Course assigned successfully!");
                location.reload(); // Reload the page to show updated data
            } else {
                alert(data.message);
            }
        })
        .catch(error => console.error("Error:", error));
    } else {
        alert("Please fill out both User ID and Course ID.");
    }
});