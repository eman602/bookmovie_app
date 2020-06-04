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
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Running the application'){
            steps{
                sh 'sudo systemctl restart flask.service'
            }
        }
    }

}