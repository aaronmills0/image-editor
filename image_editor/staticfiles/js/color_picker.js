function setupPicker() {
    document.getElementById('id_color_pop_color').addEventListener("change", setColor, false);
}

function setColor() {
    var elem = document.getElementById('id_color_pop_color');
    var dropper = document.getElementById('id_bi_eyedropper');
    dropper.style.color = String(elem.value);
    var bucket = document.getElementById('id_bi_paint_bucket');
    bucket.style.color = String(elem.value);
}

function toggle() {
    var dropper = document.getElementById('id_bi_eyedropper');
    dropper.classList.toggle("clicked-on");
}

function getData(x, y, width, height){
    var dropper = document.getElementById('id_bi_eyedropper');
    var data = document.getElementById('id_color_pop_data');
    if (dropper.classList.contains("clicked-on")){
        data.value = String(x) + ":" + String(y) + ":" + String(width) + ":" + String(height);
        document.getElementById('id_color_pop_bool').value = "1";
        autoSubmit('data-form');
    }
}