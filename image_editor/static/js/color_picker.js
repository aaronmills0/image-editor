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

function toggle(id) {
    var elem = document.getElementById(id);
    elem.classList.toggle("clicked-on");
}

function getData(x, y, width, height){
    var dropper = document.getElementById('id_bi_eyedropper');
    var color_data = document.getElementById('id_color_pop_data');
    var crop = document.getElementById('id_bi_crop');
    var crop_data = document.getElementById('id_crop_data')
    if (dropper.classList.contains("clicked-on")){
        color_data.value = String(x) + ":" + String(y) + ":" + String(width) + ":" + String(height);
        document.getElementById('id_color_pop_bool').value = "1";
        autoSubmit('data-form');
    }
    if (crop.classList.contains("clicked-on")) {
        var fp = sessionStorage.getItem("first-point");
        console.log(fp);
        if (fp == null) {
            sessionStorage.setItem("first-point", String(x) + ":" + String(y)) 
        } else {
            document.getElementById('id_crop_bool').value = "1";
            crop_data.value = sessionStorage.getItem("first-point") + ":" + String(x) + ":" + String(y) + ":" + String(width) + ":" + String(height);
            sessionStorage.removeItem("first-point");
            autoSubmit('data-form');
            console.log(crop_data);
            console.log(fp);
        }
    }
}