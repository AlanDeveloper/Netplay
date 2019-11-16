const dr = document.querySelector('#duration');
const watch = document.querySelector('#watch');

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

function convertTime(duration) {
    let minute = Math.floor(duration / 60) % 60;
    let second = Math.floor(duration % 60);

    minute = minute.lenght == 1 ? '0' + minute : minute;
    second = second.lenght == 1 ? '0' + second : second;

    return (minute + ' : ' + second);
}
