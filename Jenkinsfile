node {
   def commit_id
   stage('Preparation') {
     checkout scm
     sh "git rev-parse --short HEAD > .git/commit-id"                        
     commit_id = readFile('.git/commit-id').trim()
   }
   stage('test') {
     nodejs(pythonversion: 'python3') {
       sh 'pip install -r requirements.txt'
       sh 'python manage.py test'
     }
   }
   stage('docker build/push') {
     docker.withRegistry('https://index.docker.io/v1/', 'dockerhub') {
       def app = docker.build("nkirui2030/matatusacco:${commit_id}", '.').push()
     }
   }
}
