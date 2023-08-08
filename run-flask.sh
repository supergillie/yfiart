#!/bin/bash
command -v pip3 > /dev/null
if [ $? -ne 0 ]; then
  echo "Install pip3!"
  exit
fi
export FLASK_APP=app
export FLASK_ENV=development
pip3 install -r requirements.txt
flask run
