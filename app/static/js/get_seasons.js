const divSerie = document.querySelector('#serie');
const jquery = $;

divSerie.addEventListener('change', function (e) {
    jquery.ajax({
        url: '/serie/temporada',
        type: 'POST',
        data: {
            id: e.target.value
        },
        async: true
    }).done(function (e) {
        genero(e.season);
    });
});

const divSeason = document.querySelector('#season');
const label = document.createElement('label');
label.innerText = 'Temporada';
let select;

function genero(s) {
    select = divSeason.querySelector('select');
    if(select != null) {
        divSeason.removeChild(select);
        select = document.createElement('select');
    } else {
        select = document.createElement('select');
    }

    select.setAttribute('class', 'form-control col-md-1 mb-2');
    select.setAttribute('name', 'seasonNumber');
    let opt;
    
    for (let i = 0; i < parseInt(s); i++) {
        opt = document.createElement('option');
        opt.innerText = i + 1;
        opt.value = i + 1;
    
        select.appendChild(opt);
    }
    divSeason.appendChild(label);
    divSeason.appendChild(select);
}