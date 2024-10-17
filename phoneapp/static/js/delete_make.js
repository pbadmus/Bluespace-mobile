function deleteMake(makeId) {
    // Get the table row by the ID
    var row = document.getElementById("make-row-" + makeId);

    // Confirm the deletion with the user
    var confirmed = confirm("Are you sure you want to delete this item?");
    
    if (confirmed) {
        try {
            // Hide the row from the table (simulate deletion)
            row.style.display = 'none';

            // Show the success message
            document.getElementById("success-message").style.display = 'block';

            // Hide the success message after 3 seconds
            setTimeout(function() {
                document.getElementById("success-message").style.display = 'none';
            }, 3000);

        } catch (error) {
            // If any error occurs, show the error message
            document.getElementById("error-message").style.display = 'block';

            // Hide the error message after 3 seconds
            setTimeout(function() {
                document.getElementById("error-message").style.display = 'none';
            }, 3000);
        }
    }
}
