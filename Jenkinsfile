pipeline {
    environment {
        registry = "danielatonge/continuous_integration"
        app_dir = "app_python"
    }
    agent {
        docker {
            image 'python:3.9.6-alpine'
            args '-v /var/run/docker.sock:/var/run/docker.sock -u 0 --network host'
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
                sh 'apk add gcc musl-dev docker'
                sh 'pip3 install pylint -r $app_dir/requirements.txt'
            }
        }
        stage('Linting') {
            steps {
                echo "Started Linting..."
                sh 'cd $app_dir/Current_Moscow_Time && pylint `ls |grep .py$|xargs`'
            }
        }
        stage('Testing'){
            steps {
                echo "Started Testing..."
                sh 'cd $app_dir/Current_Moscow_Time && pytest'
            }
        }
        stage('Building and Deployment') {
            steps {
                dir("${app_dir}") {
                    script {
                        echo "Started Building and Deployment"
                        def app_image = docker.build('$registry:latest')
                        docker.withRegistry('', 'dockerhub'){
                            app_image.push()
                        }
                    }
                }
            }
        }
    }
}
