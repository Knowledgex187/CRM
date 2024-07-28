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
            if (filterValues.uuid && !cells[0].textContent.toLowerCase().includes(filterValues.uuid)) {
                showRow = false;
            }
            if (filterValues.firstName && !cells[1].textContent.toLowerCase().includes(filterValues.firstName)) {
                showRow = false;
            }
            if (filterValues.middleName && !cells[2].textContent.toLowerCase().includes(filterValues.middleName)) {
                showRow = false;
            }
            if (filterValues.lastName && !cells[3].textContent.toLowerCase().includes(filterValues.lastName)) {
                showRow = false;
            }
            if (filterValues.dob && !cells[4].textContent.toLowerCase().includes(filterValues.dob)) {
                showRow = false;
            }
            if (filterValues.phone && !cells[5].textContent.toLowerCase().includes(filterValues.phone)) {
                showRow = false;
            }
            if (filterValues.email && !cells[6].textContent.toLowerCase().includes(filterValues.email)) {
                showRow = false;
            }
            if (filterValues.address && !cells[7].textContent.toLowerCase().includes(filterValues.address)) {
                showRow = false;
            }
            if (filterValues.city && !cells[8].textContent.toLowerCase().includes(filterValues.city)) {
                showRow = false;
            }
            if (filterValues.zip && !cells[9].textContent.toLowerCase().includes(filterValues.zip)) {
                showRow = false;
            }
            if (filterValues.country && !cells[10].textContent.toLowerCase().includes(filterValues.country)) {
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
