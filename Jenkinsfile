pipeline{
    agent any
    stages{
        stage('Build Docker Image'){
            steps{
                script{
                    //docker.build('my-python-app:latest')
                    echo 'Docker image  is build .'
                    bat 'docker build -t exam2:latest .'
                    
                }
            }
        }
        stage('login to Docker Hub'){
            steps{
                script{
                    //docker.image('my-python-app:latest').run('-d -p 5000:5000')
                    echo 'Logged in to Docker Hub .'
                    bat 'docker login -u varimallamansa1 -p Manasa@247'    

                }
            }
        }
        stage('Push Docker Image to Docker Hub'){
            steps{
                script{
                    //docker.image('my-python-app:latest').push('latest')
                    echo 'Docker image is pushed to Docker Hub .'
                    bat ' docker tag exam2:latest varimallamansa1/exam2:latest'
                    bat 'docker push varimallamansa1/exam2:latest'
                }
            }
        }
        stage('deploy deployment.yaml and service.yaml'){
            steps{
                script{
                    echo 'deployment and service are created .'
                    bat 'kubectl apply -f deployment.yaml  exam2-deployment'
                    bat 'kubectl apply -f service.yaml'
                }
            }
        }
    }
}