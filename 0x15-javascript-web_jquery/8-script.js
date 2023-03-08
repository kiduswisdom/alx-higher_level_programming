$(document).ready(function () {
  const film = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.getJSON(film, function (data) {
    for (const f of data.results) {
      $('UL#list_movies').append(`<li>${f.title}</li>`);
    }
  });
});

