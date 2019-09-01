/* import shared library */
@Library('jenkins-shared-library')_

pipeline {
    agent any
    environment {
        //be sure to replace "sampriyadarshi" with your own Docker Hub username
        DOCKER_IMAGE_NAME = "nkirui2030/matatusacco"
        CANARY_REPLICAS = 0
    }
    stages {
        stage('Build') {
            steps {
                    withPythonEnv('/usr/bin/python3.5') {
                                echo  " start installing dependencies"
                                sh 'pip install -r requirements.txt'
                                sh 'python manage.py test'
                
            
            }
          }
        }
        stage('Build Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                    app.inside {
                        sh 'echo Hello, World!'
                    }
                }
            }
        }
        stage('Push Docker Image') {
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        
        stage('DeployToProduction') {
            when {
                branch 'master'
            }
            steps {
                milestone(1)
                kubernetesDeploy(
                    kubeconfigId: 'kubeconfig',
                    configs: 'deploymanifest.yml',
                    enableConfigSubstitution: true
                )
            }
        }
    }
    /*post {
	always {
            kubernetesDeploy (
                kubeconfigId: 'kubeconfig',
                configs: 'deploymanifest-canary.yml',
                enableConfigSubstitution: true
            )
        }
	*/    
        //cleanup {
	    
	    /* Use slackNotifier.groovy from shared library and provide current build result as parameter */   
        //    slackNotifier(currentBuild.currentResult)
            // cleanWs()
        //}
   // }
}