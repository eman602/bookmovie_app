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
                sh 'sudo ./script/before_installation.sh'
                sh 'sudo ./script/installation.sh'
            }
        }
        stage('Running the application'){
            steps{
                sh 'sudo systemctl restart flask.service'
            }
        }
    }

}

