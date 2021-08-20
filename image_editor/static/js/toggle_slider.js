function toggleSlider(id) {
    var cur = document.getElementById(id);
    var slider = document.getElementById(id.concat('_slider'));
    if (cur.value == "1") {
        cur.value = "0";
    } else {
        cur.value = "1";
    }
    location.reload();
}