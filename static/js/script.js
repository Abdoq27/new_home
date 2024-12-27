document.addEventListener("DOMContentLoaded", function () {
    const learnButton = document.querySelector('.learn');
    const contactButton = document.querySelector('.contact');

    learnButton.addEventListener('click', function () {
        alert('Learn more about our bakery!');
    });

    contactButton.addEventListener('click', function () {
        alert('Contact us at hello@sitename.com');
    });

    // Example of showing/hiding elements
    const feedbackSection = document.getElementById('feedback');
    feedbackSection.style.display = 'none';

    const feedbackButton = document.createElement('button');
    feedbackButton.innerText = 'Give Feedback';
    document.body.appendChild(feedbackButton);

    feedbackButton.addEventListener('click', function () {
        if (feedbackSection.style.display === 'none') {
            feedbackSection.style.display = 'block';
        } else {
            feedbackSection.style.display = 'none';
        }
    });
});
