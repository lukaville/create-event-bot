$(function () {
    var base64 = decodeURIComponent(window.location.hash.split('#')[1]);
    var event = JSON.parse(Base64.decode(base64));

    fill_card(event);
    add_buttons(event);
});

function fill_card(event) {
    $('#title').html(event.name);
    $('#description').html(event.description);

    // Create place link
    var place = $('#place');
    place.html(event.place);
    place.click(function () {
        window.open('https://maps.google.com/?q=' + event.place);
    });

    // Format and show date
    var date = new Date(parseInt(event.date) * 1000);

    var options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: 'numeric',
        minute: 'numeric'
    };

    var formattedDate = date.toLocaleDateString(navigator.language, options);

    $('#date').html(formattedDate);
}

function add_buttons(event) {
    var calendar = createCalendar({
        data: {
            title: event.name,
            start: new Date(parseInt(event.date) * 1000),
            duration: 60,
            address: event.place,
            description: event.description
        }
    });
    $('.add').append(calendar);
}