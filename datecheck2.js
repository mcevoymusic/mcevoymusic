function checkDate() {
    // Get the current date
    const currentDate = new Date();

    // Set the target date to April 14
    const targetDate = new Date(currentDate.getFullYear(), 3, 12); // Note: Month is zero-based (0 = January, 3 = April)

    // Compare the current date with the target date
    if (currentDate > targetDate) {
        document.getElementById('valid').style.display = 'none';
    } else {
        document.getElementById('error').style.display = 'none';
    }
}

checkDate(); // Call the function to run the date check immediately
