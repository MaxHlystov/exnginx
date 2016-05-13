bind = "0.0.0.0:8080"
# или через сокет
# bind = "unix:/home/proft/projects/blog/run/blog.socket"
workers = 3
#user = "box"
#group = "box"
logfile = "/home/box/web/etc/gunicorn.log"
loglevel = "info"
proc_name = "hello"
#pidfile = "/home/proft/projects/blog/gunicorn.pid"
