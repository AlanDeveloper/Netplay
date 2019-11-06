const dr = document.querySelector('#duration');
const watch = document.querySelector('#watch');
const close = document.querySelector('#close');
const video = document.querySelector('#video');
const jquery = $;

(function () {
    var onDurationChange = function () {
        if (video.readyState) {
            dr.innerText = "Duração: " + convertTime(video.duration);
        }
    };

    video.addEventListener('durationchange', onDurationChange);
    onDurationChange();
}());
video.oncontextmenu = function () { return false; }

watch.addEventListener('click', function () {
    jquery.ajax({
        url: '/tempo',
        type: 'POST',
        data: {
            video: url[url.length - 1]
        },
        async: true
    }).done(function (e) {
        video.currentTime = e.time
    });
});

let url = window.location.href.split('/');

close.addEventListener('click', function () {
    video.pause();

    jquery.ajax({
        url: '/assistidos',
        type: 'POST',
        data: {
            time: video.currentTime,
            video: url[url.length - 1]
        },
        async: true
    }).done(function () {
        console.log(null)
    });
});

function convertTime(duration) {
    let minute = Math.floor(duration / 60) % 60;
    let second = Math.floor(duration % 60);

    return (minute + ' : ' + second);
}
