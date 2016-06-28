$(function () {
    var base64 = decodeURIComponent(window.location.hash.split('#')[1]);
    var event = JSON.parse(Base64.decode(base64));

    fillCard(event);
    addButtons(event);
});

function fillCard(event) {
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

    // Preload and set image
    var image = getImage(event);
    var imageUrl = 'images/img_' + image + '.jpg';

    $('<img/>').attr('src', imageUrl).load(function () {
        $(this).remove();
        $('.event').css('background-image', 'url(' + imageUrl + ')');
        showCard();
    });
}

function addButtons(event) {
    var data = {
        title: event.name,
        start: new Date(parseInt(event.date) * 1000),
        duration: 60
    };

    if (event.place) {
        data.address = event.place;
    }

    if (event.description) {
        data.description = event.description;
    }

    var calendar = createCalendar({
        data: data
    });
    $('.add').append(calendar);
}

function showCard() {
    $('.page').fadeIn(200);
}