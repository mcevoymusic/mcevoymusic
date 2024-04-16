$(document).ready(function() {
    // Get the current date
    const currentDate = new Date();

    // Set the target date to April 14
    const targetDate = new Date(currentDate.getFullYear(), 3, 18); // Note: Month is zero-based (0 = January, 3 = April)

    // Compare the current date with the target date
    if (currentDate > targetDate) {
        $('#valid').hide();
    } else {
        $('#error').hide();
    }
});
