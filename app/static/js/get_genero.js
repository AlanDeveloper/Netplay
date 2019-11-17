const divGeneros = document.querySelector('#generos');
const add = document.querySelector('#add');
let genName = ['Ação', 'Aventura', 'Comédia', 'Documentário', 'Drama', 'Ficção científica', 'Romance', 'Suspense', 'Terror'];
let select, opt;

add.addEventListener('click', function (e) {
    select = document.createElement('select');
    select.setAttribute('class', 'form-control col-md-2 mb-2');
    select.setAttribute('name', 'genero');

    for (let i = 0; i < genName.length; i++) {
        opt = document.createElement('option');
        opt.innerText = genName[i];
        opt.value = genName[i];

        select.appendChild(opt);
    }
    divGeneros.insertBefore(select, add);

    e.preventDefault();
});