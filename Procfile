% prepara el repositorio para su despliegue. 
release:sh -c 'cd board && python manage.py migrate'
% especifica el comando para lanzar Decide
web:gunicorn board.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate