const dr = document.querySelector('#duration');

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

function convertTime(duration) {
    let minute = Math.floor(duration / 60) % 60;
    let second = Math.floor(duration % 60);

    minute = minute.lenght == 1 ? '0' + minute : minute;
    second = second.lenght == 1 ? '0' + second : second;

    return (minute + ' : ' + second);
}
