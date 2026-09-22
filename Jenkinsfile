pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out ResQLink source code'
            }
        }

        stage('Build') {
            steps {
                echo 'Building backend and frontend'
            }
        }

        stage('Test') {
            steps {
                echo 'Running automated tests'
                sh 'pytest tests -v'
            }
        }

        stage('Package') {
            steps {
                echo 'Packaging application'
            }
        }
    }

    post {
        success {
            echo 'ResQLink Jenkins pipeline completed successfully'
        }

        failure {
            echo 'ResQLink Jenkins pipeline failed'
        }
    }
}
