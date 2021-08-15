function enableContinue() {
    document.getElementById("continue-button").classList.remove("btn-custom-disabled");
}

function disableContinue() {
    var file_path = document.getElementById('id_image').value;
    let file_name = file_path.substring(12);
    if (file_name === "") {
        document.getElementById('upload-text').innerHTML = "Upload"
        document.getElementById("continue-button").classList.add("btn-custom-disabled");
    }
}