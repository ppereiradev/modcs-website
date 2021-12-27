#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Deployment') {
            steps {
                sh '''
                    docker-compose build --build-arg UID=$(id -u)
                    docker-compose up -d
                    docker logs dsci_dashboard_app
                   '''
            }
        }
    }
    post {
        failure {
            emailext to: "${env.USER_EMAIL}",
            subject: "[ERROR] deploying dashboard: ${currentBuild.fullDisplayName}",
            body: "An error occurred while deploying the dashboard."
        }
        success {
            emailext to: "${env.USER_EMAIL}",
            subject: "[SUCCESS] deploying dashboard: ${currentBuild.fullDisplayName}",
            body: "All good!"
        }
    }
}

