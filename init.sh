#!/bin/bash
apt-get update
apt-get install nginx
pip install -U Django

ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
/etc/nginx/nginx start

gunicorn -b 0.0.0.0:8080 /home/box/web/hello:app &

cd ask
gunicorn -b 0.0.0.0:8000 ask.wsgi &

