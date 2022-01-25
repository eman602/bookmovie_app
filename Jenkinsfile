pipeline {
    agent any
    stages {
    stage('installing pip and other stuff') {
        steps {
            apt update -y
            apt install pyhthon3 python3-venv python3-pip -y 

        }
    stage('setting up the system') {
        steps {
            sudo cp /etc/systemd/system/flask.service /etc/systemd/system/
            sudo systemctl daemon-reload
            sudo systemctl enable flask.service

        }
    stage('setting up further environment') {
        steps {
            source venv/bin/activate
            pip3 install -r requirements.txt

        }

    stage('setting up variables and starting application') {
        steps {
            source ~/bashrc
            
            python3 app.py
        }
    }
    }
    }
    }
}
}
