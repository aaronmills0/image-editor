

function getFilename() {
    var file_path = document.getElementById('id_image').value;
    let file_name = file_path.substring(12);
    document.getElementById('upload-text').innerHTML = file_name;
}