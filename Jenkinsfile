pipeline {
    agent any

    stages {

        stage('Setup Python Environment') {
            steps {
                echo "Setting up Python environment..."
                sh 'python3 --version'
            }
        }

        stage('Install Packages') {
            steps {
                echo "Installing required packages..."
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Python Script') {
            steps {
                echo "Running Python file..."
                sh 'python3 test.py'
            }
        }
    }
}
