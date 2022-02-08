pipeline {
    agent any

    stages {
        stage('Making sure environment is built'){
            environment {
                BITBUCKET_COMMON_CREDS = credentials('hello-emmanuel-just-checking')
            }
            steps{
                sh 'chmod +x ./script/*'
                sh "echo ${BITBUCKET_COMMON_CREDS}"
            }
        }
        stage("making environment"){
            environment {
                CC = """${sh(
                    returnStdout: true,
                    script: 'echo "clang"'
                )}"""
                EXIT_STATUS = """${sh(
                    returnStatus: true,
                    script: 'exit 1'
                    )}"""
                }
            steps{
                sh './script/before_installation.sh'
                sh './script/installation.sh'
            }
        }
        stage('Running the application'){
            environment {
                DEBUG_FLAGS = '-g'
            }
            steps{
                sh 'sudo systemctl restart flask.service'
                
            }
        }
         
        stage('checking run was succesfful'){
            when {
                expression { 
                    currentBuild.result == null || currentBuild.result == 'SUCCESS'
                }
            }
            steps {
                    sh ' echo successfully'
             }
            
        }
         
            
    }

}

