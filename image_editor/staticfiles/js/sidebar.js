function openNav() {
    document.getElementById("sidebar").style.left = "0px";
}

function closeNav() {
    document.getElementById("sidebar").style.left = "-250px";
}

function resetFilter(id) {
    const defaults = new Map();
    defaults.set('id_horizontal_flip', "0")
    defaults.set('id_vertical_flip', "0")
    defaults.set('id_grayscale', "0")
    defaults.set('id_sepia', "0")
    defaults.set('id_binarize', "0")
    defaults.set('id_histogram_equalize', "0")
    defaults.set('id_invert', "0")
    defaults.set('id_smoothness', "0")
    defaults.set('id_sharpness', "0")
    defaults.set('id_brightness', "0")
    defaults.set('id_contrast', "10")
    defaults.set('id_gamma_correction', "10")
    defaults.set('id_saturation', "10")
    defaults.set('id_resize', "0")
    defaults.set('id_color_pop_bool', "0")
    defaults.set('id_color_pop_color', "#ff0946")

    var elem = document.getElementById(id);
    elem.value = defaults.get(id);
}

function resetAll() {
    document.getElementById('id_horizontal_flip').value = 0;
    document.getElementById('id_vertical_flip').value = 0;
    document.getElementById('id_grayscale').value = 0;
    document.getElementById('id_sepia').value = 0;
    document.getElementById('id_binarize').value = 0;
    document.getElementById('id_histogram_equalize').value = 0;
    document.getElementById('id_invert').value = 0;
    document.getElementById('id_smoothness').value = 0;
    document.getElementById('id_sharpness').value = 0;
    document.getElementById('id_brightness').value = 0;
    document.getElementById('id_contrast').value = 10;
    document.getElementById('id_gamma_correction').value = 10;
    document.getElementById('id_saturation').value = 10;
    document.getElementById('id_resize').value = 0;
    document.getElementById('id_color_pop_bool').value = 0;
    document.getElementById('id_color_pop_color').value = "#ff0946";
}

function sidebarScroll() {
    var sidebar = document.getElementById("sidebar");

    var tp = sessionStorage.getItem("sidebar-scroll");
      if (tp !== null) {
        sidebar.scrollTop = parseInt(tp, 10);
      }

      window.addEventListener("beforeunload", () => {
        sessionStorage.setItem("sidebar-scroll", sidebar.scrollTop);
      });
}