#!/bin/bash
 
 
sudo cp etc/systemd/system/flask.service /etc/systemd/system/

sudo systemctl daemon-reload

sudo systemctl enable flask.service

source venv/bin/activate
source ~/bashrc
pip3 install -r requirements.txt

