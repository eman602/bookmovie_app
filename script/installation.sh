#!/usr/bin/env bash
 
sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y
 
python3 -m venv venv
 
source ~/.bashrc

source /var/lib/jenkins/workspace/Bookmovie_app/venv/bin/activate

cd /var/lib/jenkins/workspace/Bookmovie_app
 
pip3 install -r requirements.txt
 


gunicorn --bind=0.0.0.0:5000 application:app

