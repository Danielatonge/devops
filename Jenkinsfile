pipeline {
    environment {
        registry = "Danielatonge/devops"
        app_dir = "app_python"
    }
    agent {
        docker {
            image 'python:3.9.6-alpine'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Installation') {
            steps {
                echo "Started Installation"
                sh 'python pip install --upgrade pip'
                sh 'pip install -r $app_dir/requirements.txt'
            }
        }
        stage('Linting') {
            steps {
                echo "Started Linting..."
                sh 'cd $app_dir/Current_Moscow_Time'
                sh 'pylint `ls |grep .py$|xargs`'
            }
        }
        stage('Testing'){
            steps {
                echo "Started Testing..."
                sh 'cd $app_dir/Current_Moscow_Time'
                sh "pytest"
            }
        }
        stage('Building and Deployment') {
            steps {
                script {
                    echo "Started Building and Deployment"
                    def app_image = docker.build('$registry')
                    docker.withRegistry('', 'dockerhub'){
                        app_image.push()
                    }
                }
            }
        }
    }
}