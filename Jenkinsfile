node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   } 
   try{
   
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
   stage('ochestration') 
       {       
            sh """
              echo "deploy stage";
              curl https://sdk.cloud.google.com | bash > /dev/null;
              source $HOME/google-cloud-sdk/path.bash.inc
              gcloud components update kubectl
              gcloud auth activate-service-account --key-file service-account.json
              gcloud config set project mathree
              gcloud config set compute/zone us-central1-a	
              gcloud container clusters get-credentials mathree-cluster
       
            """              
       }
      
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub')
      {
       def app = docker.build("nkirui2030/matatusacco:${commit_id}", '.').push()
     }
   }
   steps
   {
      sh "./deploy.sh"
  
   }
  }
   catch(e) {    // mark build as failed
    currentBuild.result = "FAILURE";

    // send slack notification
    slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")

    // throw the error
    throw e;
    }
}