function previewFile() {
  var previewContainer = document.getElementById('previewContainer');
  var file = document.querySelector('input[type=file]').files[0];
  var reader = new FileReader();

  reader.onloadend = function () {
    if (file.type.match('image.*')) {
      var img = document.createElement('img');
      img.src = reader.result;
      img.style.maxWidth = '500px'; // Set the maximum width for the image
      img.style.maxHeight = '500px'; // Set the maximum height for the image
      previewContainer.innerHTML = '';
      previewContainer.appendChild(img);
      document.getElementById('selectType').selectedIndex = 0;

    } else if (file.type === 'application/pdf') {
      var iframe = document.createElement('iframe');
      iframe.src = reader.result;
      iframe.style.width = '100%';
      iframe.style.height = '500px'; // Set the height for the iframe
      previewContainer.innerHTML = '';
      previewContainer.appendChild(iframe);
      document.getElementById('selectType').selectedIndex = 1;

    } else {
      previewContainer.innerHTML = 'File type not supported for preview';
    }
  }

  if (file) {
    reader.readAsDataURL(file); // reads the file as a data URL
  } else {
    previewContainer.innerHTML = "No file selected for preview";
  }
}