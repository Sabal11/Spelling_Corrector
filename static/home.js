document.getElementById("spellCheckButton").addEventListener("click", function() {
    // Get the form
    var form = document.getElementById("spellForm");
    // Submit the form
    form.submit();
});

document.getElementById("grammarCheckButton").addEventListener("click", function() {
    // Get the form
    var form = document.getElementById("grammarForm");
    // Submit the form
    form.submit();
});

// scroll function
var scrollToTopButton = document.getElementById('scroll-to-top');

    // Show the button when the user scrolls down 100 pixels from the top
    window.onscroll = function () {
        if (document.body.scrollTop > 100 || document.documentElement.scrollTop > 100) {
            scrollToTopButton.style.display = 'block';
        } else {
            scrollToTopButton.style.display = 'none';
        }
    };

    // Scroll to the top when the button is clicked
    scrollToTopButton.onclick = function () {
        document.body.scrollTop = 0; // For Safari
        document.documentElement.scrollTop = 0; // For Chrome, Firefox, IE, and Opera
    };