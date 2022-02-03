#!/bin/bash
 
 
cp etc/systemd/system/flask.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable flask.service

source venv/bin/activate

pip3 install -r requirements.txt

