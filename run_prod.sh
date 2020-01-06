#  /usr/local/src/coc/venv/bin/python

source ./venv/bin/activate

uwsgi -d --ini uwsgi.ini



# schedule
nohup python schedule/schedule_dashboard.py > /dev/null 2>&1 &