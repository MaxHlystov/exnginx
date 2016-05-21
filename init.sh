#!/bin/bash
apt-get update -y
apt-get install nginx -y
pip install -U Django

ln -sf /home/box/web/etc/nginx.conf /etc/nginx/nginx.conf
/etc/init.d/nginx -s start

# запуск сервера MySQL
/etc/init.d/mysql start

#cd /home/box/web
#gunicorn -b 0.0.0.0:8080 hello:app &

# создать базу. установить для нее все права для пользователя box
sudo mysql -uroot -e "CREATE DATABASE stepic_web CHARACTER SET UTF8;"
sudo mysql -uroot -e "create user 'box'@'localhost';"
sudo mysql -uroot -e "GRANT ALL PRIVILEGES ON stepic_web.* TO 'box'@'localhost' WITH GRANT OPTION;"
sudo mysql -uroot -e "FLUSH PRIVILEGES;"

# установить поддержку mysql в python
sudo apt-get install python-dev libmysqlclient-dev -y
sudo pip install pip --upgrade
sudo apt-get build-dep python-mysqldb -y
sudo pip install MySQL-python

# создать миграцию
cd /home/box/web/ask
python manage.py makemigrations
python manage.py makemigrations qa

# обновить базу данных по данным моделей из миграции
python manage.py migrate

# запустить Django через сервер gunicorn
#cd ask
#gunicorn -b 0.0.0.0:8000 ask.wsgi &

