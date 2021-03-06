#!/usr/bin/env bash
# actavated venv ans run django server
# wykys and remogeus 2018

if [ ! -d ".venv" ]; then
  echo ".venv not exist"
  ./venv.sh
fi

echo "activate venv"
. .venv/bin/activate

echo "run server"
./manage.py runserver 0.0.0.0:8000

echo "run browser"
xdg-open localhost:8000/show_data.html
