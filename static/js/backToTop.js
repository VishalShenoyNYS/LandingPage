// static/script.js

// Function to scroll to the top of the page
function backToTop() {
    document.body.scrollTop = 0; // For Safari
    document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
}

// Add an event listener to execute backToTop function when button is clicked
document.addEventListener('DOMContentLoaded', function() {
    var backButton = document.getElementById('backToTopButton');
    backButton.addEventListener('click', backToTop);
});
