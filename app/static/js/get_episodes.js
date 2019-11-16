const divSeason = document.querySelector('.container');
const number = document.querySelector('#number');
const url = window.location.href.split('/');
const jquery = $;
let div, button;

for (let i = 0; i < parseInt(number.innerText); i++) {
    button = document.createElement('button');
    button.innerText = 'Ver episódios';
    button.value = i + 1;
    button.addEventListener('click', get_episodes);

    div = document.createElement('div');
    div.setAttribute('class', 'alert alert-dark');
    div.setAttribute('role', 'alert');
    div.innerText = 'Temporada: ' + (i + 1);

    div.appendChild(button);
    divSeason.appendChild(div);
}

divSeason.removeChild(number);

function get_episodes(e) {
    jquery.ajax({
        url: '/serie/lista/' + url[url.length - 1] + '/' + e.target.value,
        type: 'POST',
        async: true
    }).done(function (e) {
        console.log(e);
    });
}