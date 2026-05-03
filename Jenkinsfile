pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat 'python --version'
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python train.py'
            }
        }

        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'results.json', fingerprint: true
            }
        }
    }
}