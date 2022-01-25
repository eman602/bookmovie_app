pipeline {
    agent any
    stages {
        stage('installing pip and other stuff') {
            steps {
               apt update -y
               apt install pyhthon3 python3-venv python3-pip -y 

            }
        }
        stage('setting up the system') {
            steps {
                echo "hello2"
            }
        }
        stage('setting up further environment') {
            steps {
                echo "hello3"
            }
        }

        stage('setting up variables and starting application') {
            steps {
            echo "hello4"
            }
    }
    
    
    }
}

