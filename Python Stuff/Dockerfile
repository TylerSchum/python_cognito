FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y python python-pip python-virtualenv gunicorn

RUN mkdir -p /deploy/app
COPY gunicorn_config.py /deploy/gunicorn_config.py
COPY app /deploy/app
RUN pip install -r /deploy/app/requirements.txt
WORKDIR /deploy/app

EXPOSE 80

CMD ["/usr/bin/gunicorn", "--config", "/gunicorn_config.py", "web:app"]