function setupPicker() {
    document.getElementById('id_color_pop_color').addEventListener("change", setColor, false);
}

function setColor() {
    var elem = document.getElementById('id_color_pop_color');
    var dropper = document.getElementById('id_bi_eyedropper');
    dropper.style.color = String(elem.value);
}