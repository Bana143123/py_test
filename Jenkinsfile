pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: '', branch: 'master'
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                pip install allure-pytest
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
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
            cleanWs()
        }
    }
}
