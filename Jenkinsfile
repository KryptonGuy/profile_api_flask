pipeline {
    agent {label 'jenkins-docker'}
    options{
        buildDiscarder(logRotator(numToKeepStr: '5', daysToKeepStr: '5'))
        timestamps()
    }
    environment{
        
        registry = "yashspam/profile-api"
        registryCredential = 'dockerhubId'        
    }
    
    stages{
        
       stage('Build') {
      steps{
          sh "pwd"
        script {
          dockerImage = docker.build(registry + ":$BUILD_NUMBER", "./app")
        }
      }
    }
       stage('Deploy') {
      steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
          }
        }
      }
    }
}
}
