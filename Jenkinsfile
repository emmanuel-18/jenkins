pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Run') {
            steps {
                echo 'Pipeline from GitHub working!'
            }
        }
    }
}