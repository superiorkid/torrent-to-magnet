$('#input-file').on('change', function(){
  // get the file name
  var filename = $(this).val();
  // replace the choose file label
  $(this).next('.custom-file-label').html(filename)
});