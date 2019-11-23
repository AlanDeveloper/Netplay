const watch = document.querySelector('#watch');

if (url[3] === 'filme') {
    watch.addEventListener('click', function () {
        data = {
            type: 'filme',
            time: video.currentTime,
            video: url[url.length - 1]
        }

        jquery.ajax({
            url: '/tempo',
            type: 'POST',
            data: data,
            async: true
        }).done(function (e) {
            video.currentTime = e.time
        });
    });
} else if (url[3] === 'serie') {
    watch.addEventListener('click', function () {
        data = {
            type: 'serie',
            time: video.currentTime,
            video: url[url.length - 1],
            season: url[url.length - 2],
            serie: url[url.length - 3]
        }

        jquery.ajax({
            url: '/tempo',
            type: 'POST',
            data: data,
            async: true
        }).done(function (e) {
            video.currentTime = e.time
        });
    });
}