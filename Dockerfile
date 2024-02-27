FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/uthem150/insta_project.git

WORKDIR /home/instagram/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRETE_KEY=.env파일 안의 secrete key~~~" > .env


RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=instagram.settings.deploy && python manage.py migrate --settings=instagram.settings.deploy && gunicorn instagram.wsgi --env DJANGO_SETTINGS_MODULE=instagram.settings.deploy --bind 0.0.0.0:8000"]