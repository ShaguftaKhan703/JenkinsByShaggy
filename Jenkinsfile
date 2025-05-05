pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                echo 'Cloning repository...'
                // Code is already cloned by Jenkins when using Pipeline from SCM
            }
        }
        stage('Build') {
            steps {
                echo 'Compiling Java code...'
                bat 'javac HelloWorld.java'
            }
        }
        stage('Run') {
            steps {
                echo 'Running Java program...'
                bat 'java HelloWorld'
            }
        }
    }
}

