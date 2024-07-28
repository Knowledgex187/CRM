// Wait for the DOM content to be fully loaded before running the script
document.addEventListener('DOMContentLoaded', function () {
    // Select all input elements within the form with ID 'searchForm'
    var searchInputs = document.querySelectorAll('#searchForm input');

    // For each input element, add an event listener for the 'input' event
    searchInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            // Call the filterTable function whenever the input value changes
            filterTable();
        });
    });

    // Define the filterTable function
    function filterTable() {
        // Create an object to store the values from each input field
        var filterValues = {};
        searchInputs.forEach(function(input) {
            // Store the lowercased value of each input field in the filterValues object
            filterValues[input.name] = input.value.toLowerCase();
        });

        // Select all table rows within the tbody element
        var rows = document.querySelectorAll('tbody tr');

        // For each row, determine whether it should be displayed or hidden
        rows.forEach(function(row) {
            // Select all table data (td) elements within the row
            var cells = row.querySelectorAll('td');
            // Assume the row should be displayed initially
            var showRow = true;

            // Check each filter value against the corresponding cell's text content
            if (filterValues.customer && !cells[0].textContent.toLowerCase().includes(filterValues.customer)) {
                showRow = false;
            }
            if (filterValues.accountNumber && !cells[1].textContent.toLowerCase().includes(filterValues.accountNumber)) {
                showRow = false;
            }
            if (filterValues.accountType && !cells[2].textContent.toLowerCase().includes(filterValues.accountType)) {
                showRow = false;
            }
            if (filterValues.balance && !cells[3].textContent.toLowerCase().includes(filterValues.balance)) {
                showRow = false;
            }
            if (filterValues.created && !cells[4].textContent.toLowerCase().includes(filterValues.created)) {
                showRow = false;
            }
            if (filterValues.update && !cells[5].textContent.toLowerCase().includes(filterValues.update)) {
                showRow = false;
            }

            // Show or hide the row based on whether it matches the filter criteria
            if (showRow) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    }
});
