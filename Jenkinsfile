pipeline {
    agent any
    environment {
            // Ми кажемо Jenkins: візьми секрет з ID 'USER_EMAIL_LOGIN'
            // і поклади його значення в змінну середовища з таким самим ім'ям
            USER_EMAIL_LOGIN = credentials('LOGIN')
            USER_PASSWORD_LOGIN = credentials('PASSWORD')
        }
    parameters {
        string(name: 'UI_URL', defaultValue: 'https://qauto.forstudy.space', description: 'Who should I say hello to?')
        choice(name: 'MARKS', choices: ['api_test', 'Two', 'Three'], description: 'Pick something')
    }
    // Використання облікових даних для авторизації доступу до репозиторію
    stages {
        stage('Checkout') {
            steps {
                // Використання облікових даних для клонування репозиторію
                git branch: 'main', url: 'https://github.com/Hellrazers/Hillel_19_12.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                #!/bin/bash
                apt-get update && apt-get install -y python3-venv
                python3 -m venv venv
                '''
            }
        }
        stage('Install requirements') {
            steps {
                sh '''
                 . venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run tests') {
            steps {
                sh '''
                . venv/bin/activate
                echo "UI_URL=https://qauto.forstudy.space" > .env
                echo "LOGIN=${USER_EMAIL_LOGIN}" >> .env
                echo "PASSWORD=${USER_PASSWORD_LOGIN}" >> .env
                echo "AUTH_BASIC_USER=guest" >> .env
                echo "AUTH_BASIC_PASSWORD=welcome2qauto" >> .env
                pytest -m ${params.MARKS} --alluredir=allure-results
                '''
            }
        }

    }
     post {
        always {
            allure commandline: 'allure-results', includeProperties: false, jdk: '', resultPolicy: 'LEAVE_AS_IS', results: [[path: 'allure-results']]
        }

     }
}