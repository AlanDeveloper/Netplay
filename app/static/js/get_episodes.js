const divSeason = document.querySelector('.container');
const number = document.querySelector('#number');
const url = window.location.href.split('/');
const jquery = $;
let div, button;

const card_seasons = function (i) {
    button = document.createElement('button');
    button.setAttribute('class', 'div_' + i);
    button.innerText = 'Ver episódios';
    button.value = i + 1;
    button.addEventListener('click', get_episodes);
    button.style.color = "white";
    button.style.background = "#1c728d";
    
    div = document.createElement('div');
    div.setAttribute('class', 'alert alert-dark div_' + i);
    div.setAttribute('role', 'alert');
    div.innerText = 'Temporada: ' + (i + 1);

    div.appendChild(button);
    divSeason.appendChild(div);
}

const get_episodes = function (event) {
    button_season = document.querySelector('button.' + event.target.className);
    div_season = document.querySelector('div.' + event.target.className);

    if (div_season.children.length == 1) {
        jquery.ajax({
            url: '/serie/lista/' + url[url.length - 1] + '/' + event.target.value,
            type: 'POST',
            async: true
        }).done(function (res) {
            for (let i = 0; i < res.length; i++) {

                div = document.createElement('div');
                div.setAttribute('class', 'mt-3 alert alert-light');
                div.setAttribute('role', 'alert');
                div.innerText = 'Episódio ' + (res[i].episode_number + 1) + ': ' + (res[i].title);

                button = document.createElement('button');             
                
                a = document.createElement('a');
                a.innerText = 'Assistir';
                a.setAttribute('href', '/serie/' + url[url.length - 1] + '/' + event.target.value + '/' + res[i].id);
                a.style.backgroundColor = "#8585d8";
                a.style.color = "white";                
                button.style.backgroundColor = "#8585d8";
                button.appendChild(a);
                div.appendChild(button);
                div_season.appendChild(div);
            }
            if(res.length == 0) {
                div = document.createElement('div');
                div.setAttribute('class', 'mt-3 alert alert-light');
                div.setAttribute('role', 'alert');
                div.innerText = 'Nenhum episódio';
                
                div_season.appendChild(div);
            }
        });
        button_season.innerText = 'Desver episódios';
    } else {
        button_season.innerText = 'Ver episódios';
        
        for (let i = 1; i < div_season.children.length; i++) div_season.removeChild(div_season.children[i]);
    }
}

for (let i = 0; i < parseInt(number.innerText); i++) card_seasons(i);
divSeason.removeChild(number);
