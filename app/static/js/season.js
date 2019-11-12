const divSeason = document.querySelector('#season');
const season = document.querySelector('#season-value');

const select = document.createElement('select');
select.setAttribute('class', 'form-control col-md-1 mb-2');
select.setAttribute('name', 'seasonNumber');
let opt;

for (let i = 0; i < parseInt(season.innerText); i++) {
    opt = document.createElement('option');
    opt.innerText = i + 1;
    opt.value = i + 1;

    select.appendChild(opt);
}
divSeason.appendChild(select);
divSeason.removeChild(season);