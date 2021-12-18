function validatePhone() {
    let Phone = document.forms["Contact"]["phone"].value;
    if (Phone.length != 10 || !Phone.startsWith("0")) {
        alert('Phone is not valid. Phone must be 10 digits and start with "0"');
        return false;
    }
}