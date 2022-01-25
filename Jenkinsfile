pipeline {
    agent any
    stages {
        stage('installing pip and other stuff') {
            steps {
                retry(3) {
                    echo "hello therre with the etry"
                }
                timeout(time: 3. unit: 'MINUTES') {
                    echo  "another one"

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

