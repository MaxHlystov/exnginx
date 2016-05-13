#!/bin/bash
ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
/etc/init.d/nginx start
#/etc/rc.d/init.d/nginx
#ln -sf /home/box/web/etc/hello.py /etc/gunicorn.d/hello.py
#/etc/init.d/gunicorn start
gunicorn -b 0.0.0.0:8080 /home/box/web/hello:app &

