document.getElementById('feedbackForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form from submitting the traditional way

    // Display success message
    document.getElementById('successMessage').classList.remove('hidden');

    // Reset the form
    document.getElementById('feedbackForm').reset();
});
