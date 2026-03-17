pipeline {
    agent any
  
    environment {
        DOCKER_HUB_REPO = "saurabhk91/flask-app"
        // This creates a unique name like saurabhk91/flask-app:5
        IMAGE_TAG = "${DOCKER_HUB_REPO}:${env.BUILD_NUMBER}"
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
    }
  
    stages {
        stage('Build') {
            steps {
                sh "docker build -t ${IMAGE_TAG} ."
            }
        }
        stage('Push') {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                sh "docker push ${IMAGE_TAG}"
            }
        }
        stage('Deploy') {
            steps {
                // Apply the base configuration
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
                
                // Update the image to the specific build version
                // 'flask-app-container' must match the name in deployment.yaml
                sh "kubectl set image deployment/flask-app-deployment flask-app-container=${IMAGE_TAG}"
                
                // Verify the rollout
                sh "kubectl rollout status deployment/flask-app-deployment"
            }
        }
    }
}
