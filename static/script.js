$(function () {
    var base64 = decodeURIComponent(window.location.hash.split('#')[1]);
    var event = JSON.parse(Base64.decode(base64));

    $('#title').html(event.name);
    $('#description').html(event.description);
    $('#place').html(event.place);
    $('#date').html(event.date);
    var calendar = createCalendar({
        data: {
            title: event.name,
            start: new Date(parseInt(event.date) * 1000),
            duration: 60,
            address: event.place,
            description: event.description
        }
    });
    $('body').append(calendar);
});