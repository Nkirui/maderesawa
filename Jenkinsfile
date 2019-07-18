node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   }
     stage('test') {
     def myTestContainer = docker.image('python:3.5')
     myTestContainer.pull()
     myTestContainer.inside {
       sh 'virtualenv -p python3 env'
       sh 'source env/bin/activate'
       sh 'pip install -r requirements.txt'
       sh 'python manage.py runserver'
     }

   }
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub')
      {
       def app = docker.build("nkirui2030/matatusacco:${commit_id}", '.').push()
     }
   }