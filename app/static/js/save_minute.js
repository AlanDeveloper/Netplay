const video = document.querySelector('#video');
const close = document.querySelector('#close');
const url = window.location.href.split('/');
const jquery = $;

let data = {}

close.addEventListener('click', function () {
    video.pause();

    data = {
        time: video.currentTime,
        video: url[url.length - 1]
    }
    data.watched = video.currentTime === video.duration ? true : false; 

    jquery.ajax({
        url: '/assistidos',
        type: 'POST',
        data: data,
        async: true
    }).done(function () {
        console.log(null)
    });
});