const video = document.querySelector('#video');
const close = document.querySelector('#close');
const url = window.location.href.split('/');
const jquery = $;

let data = {}

if (url[3] === 'filme') {
    close.addEventListener('click', function () {
        video.pause();
    
        data = {
            type: 'filme',
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
} else if(url[3] === 'serie'){
    close.addEventListener('click', function () {
        video.pause();

        data = {
            type: 'serie',
            time: video.currentTime,
            video: url[url.length - 1],
            season: url[url.length - 2],
            serie: url[url.length - 3]
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
}
