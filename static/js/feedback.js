document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.question-btn');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const answerDiv = this.nextElementSibling;
            if (answerDiv.style.display === 'none' || answerDiv.style.display === '') {
                answerDiv.style.display = 'block';
            } else {
                answerDiv.style.display = 'none';
            }
        });
    });
});
