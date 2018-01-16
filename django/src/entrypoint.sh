#!/bin/bash
python3 manage.py rqworker default &
uwsgi --chdir=/app/ --module=core.wsgi --master --process=4 --socket=:8002 --max-requests=50 --close-on-exec --harakiri=30
