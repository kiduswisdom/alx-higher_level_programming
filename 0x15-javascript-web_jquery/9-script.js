$(document).ready(function () {
  const greet = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.getJSON(greet, function (data) {
    $('#hello').text(data.hello);
  });
});
