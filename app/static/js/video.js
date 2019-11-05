const dr = document.querySelector('#duration');
const close = document.querySelector('#close');
let video = document.querySelector('#video');
const jquery = $;

video.oncontextmenu = function () { return false; }
// video.addEventListener('loadedmetadata', function (e) {
//     console.log('ola');
//     dr.innerText = "Duração: " + convertTime(video.duration);
// });

let url = window.location.href.split('/');

close.addEventListener('click', function () {
    // console.log("posição atual:", video.currentTime);
    // console.log("duração:", convertTime(video.duration));
    video.pause();

    jquery.ajax({
        url: '/watch',
        type: 'POST',
        data: {
            time: video.currentTime,
            video: url[url.length - 1]
        },
        async: true
    });
});

function convertTime(duration) {
    let minute = Math.floor(duration / 60) % 60;
    let second = Math.floor(duration % 60);

    return (minute + ' : ' + second);
}
