pipeline {
    agent any
    stages {
        stage('Making sure environment is built'){
            steps{
                sh 'chmod +x ./script/*'
            }
        }
        stage("making environment"){
            steps{
                sh 'apt update -y'
                sh 'sudo apt install python3 python3-venv python3-pip -y'
            }
        }
        stage('Running the application'){
            steps{
                sh 'sudo systemctl restart flask.service'
            }
        }
    }

}

