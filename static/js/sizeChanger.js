// Function to switch classes based on screen orientation
function switchFlexClasses() {
    var mainElements = document.querySelector('main');
    const rowFlexElements = mainElements.querySelectorAll('.row-flex');
    if (window.matchMedia("(orientation: portrait)").matches) {
        // Switch to col-flex for portrait mode
        rowFlexElements.forEach(element => {
            element.classList.add('col-flex');
            element.classList.remove('row-flex');
        });
    } else {
        // Switch to row-flex for landscape mode and other devices
        rowFlexElements.forEach(element => {
            element.classList.add('row-flex');
            element.classList.remove('col-flex');
        });
    }
}

// Add event listener for orientation change
window.addEventListener('resize', switchFlexClasses);
window.addEventListener('orientationchange', switchFlexClasses);

// Initial check when the script runs
switchFlexClasses();
