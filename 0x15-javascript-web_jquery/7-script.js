$(document).ready(function () {
  const people = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.getJSON(people, function (data) {
    $('#character').text(data.name);
  });
});
