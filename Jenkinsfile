pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Bana143123/py_test.git', branch: 'master'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                #!/bin/bash
                echo "Setting up Python virtual environment"
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                #!/bin/bash
                echo "Activating virtual environment and running tests"
                source venv/bin/activate
                pytest --alluredir=allure-results
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure([
                    results: [[path: 'allure-results']]
                ])
            }
        }
    }

    post {
        always {
            echo "Cleaning workspace"
            cleanWs()
        }
    }
}
