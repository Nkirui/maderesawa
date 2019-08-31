#!/bin/sh

node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                      
     commit_id = readFile('.git/commit-id').trim()
   } 
      
    stage('test1') {
      
      withPythonEnv('/usr/bin/python3.5') {
    // Uses the default system installation of Python
          // Equivalent to withPythonEnv('/usr/bin/python') 
       echo  " start installing dependencies"
      // sh 'virtualenv -p python3 env'
       //sh 'source env/bin/activate'
       sh 'pip install -r requirements.txt'
       sh 'python manage.py test'
      }     
     }
  
      
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub')
      {
       def app = docker.build("nkirui2030/matatusacco:${commit_id}", '.').push()
     }
   }

    stage('deploy to k8s')
    {
        sh """
          #!/bin/bash 
			    echo "deploy stage";
          curl https://sdk.cloud.google.com | bash > /dev/null;
          source $HOME/google-cloud-sdk/path.bash.inc
          gcloud components update kubectl
          gcloud auth activate-service-account --key-file service-account.json
          gcloud config set project cicid-251308
          gcloud config set compute/zone us-east1-d	
          gcloud container clusters get-credentials  jenkins-cd	
        
           """
      
    }
  stage('publish')
    {
        sh """
				#!/bin/bash
        kubectl apply -f k8s
        """
    
      
    }
 
  }


  //  catch(e) {    // mark build as failed
  //   currentBuild.result = "FAILURE";

  //   // send slack notification
  //   slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

  //   // throw the error
  //   throw e;
  //   }
// }