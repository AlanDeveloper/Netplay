# Netplay

Rodar virtualenv

virtualenv --python=/usr/bin/python3 'NomeDeUmaPastaSemAspas'

source 'NomeDeUmaPastaSemAspas'/bin/activate

pip install -r requirements.txt

Rodar servidor

export FLASK_APP=runserver.py

export FLASK_ENV=development

export FLASK_DEBUG=True

flask run
