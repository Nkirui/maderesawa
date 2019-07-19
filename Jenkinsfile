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
  environment {
    GOOGLE_PROJECT_ID = 'madereva';
    GOOGLE_SERVICE_ACCOUNT_KEY = credentials('./madereva-04c3e76546d5.json');
    }
   stage('ochestration') 
       {
        
        steps{

            sh """
              echo "deploy stage";
              curl -o /tmp/google-cloud-sdk.tar.gz https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-sdk-220.0.0-linux-x86_64.tar.gz;
              tar -xvf /tmp/google-cloud-sdk.tar.gz -C /tmp/;
              /tmp/google-cloud-sdk/install.sh -q;
              source /tmp/google-cloud-sdk/path.bash.inc;
              gcloud config set project ${GOOGLE_PROJECT_ID};
              gcloud components install app-engine-java;
              gcloud components install app-engine-python;
              gcloud auth activate-service-account --key-file ${GOOGLE_SERVICE_ACCOUNT_KEY};
              gcloud container clusters get-credentials maderesawa-clus
              echo "After authentication gcloud";
              gcloud config list;
              mvn -X clean package appengine:deploy -Dmaven.test.failure.ignore=true;
            """
          }	
          post{
            always{
              println "Result : ${currentBuild.result}";
              println "Deploy to GCP ..";
            } 
          }
       }
      
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub')
      {
       def app = docker.build("nkirui2030/matatusacco:${commit_id}", '.').push()
     }
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