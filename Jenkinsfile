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
                sh 'apk update'
                sh 'apk upgrade --avialable && sync'
            }
        }
        stage('Running the application'){
            steps{
                sh 'lxc info alpine-www01e'
            }
        }
    }

}

