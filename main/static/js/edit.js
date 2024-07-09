document.addEventListener('DOMContentLoaded', function () {
    const customerDropdown = document.getElementById('customer');
    customerDropdown.addEventListener('change', function () {
        const selectedOption = customerDropdown.options[customerDropdown.selectedIndex];
        const customerData = JSON.parse(selectedOption.getAttribute('data-customer'));

        if (customerData) {
            document.getElementById('email').value = customerData.email;
            document.getElementById('firstName').value = customerData.firstName;
            document.getElementById('middleName').value = customerData.middleName;
            document.getElementById('lastName').value = customerData.lastName;
            document.getElementById('phoneNumber').value = customerData.phoneNumber;
            document.getElementById('streetAddress').value = customerData.streetAddress;
            document.getElementById('city').value = customerData.city;
            document.getElementById('post_code_or_zip').value = customerData.post_code_or_zip;
            document.getElementById('country').value = customerData.country;
        }
    });
});