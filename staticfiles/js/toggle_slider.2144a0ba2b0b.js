function toggleSlider(id) {
    var cur = document.getElementById(id);
    if (cur.value == "1") {
        cur.value = "0";
    } else {
        cur.value = "1";
    }
    location.reload();
}