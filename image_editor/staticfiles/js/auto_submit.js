function autoSubmit(id) {
    var form = document.getElementById(id);
    form.submit();
}

function refreshImage() {
    var element = document.getElementById('image');
    var ref = element.src;
    element.setAttribute('src', ref);
}