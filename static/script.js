$(function () {
    var base64 = decodeURIComponent(window.location.hash.split('#')[1]);
    var event = JSON.parse(Base64.decode(base64));

    $('#title').html(event.name);
    $('#description').html(event.description);
    $('#place').html(event.place);
    $('#date').html(event.date);
});