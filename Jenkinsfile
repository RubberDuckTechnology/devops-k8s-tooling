pipeline {
  agent any
  stages {
    stage('Reload Configuration') {
      steps {
        steps.withCredentials([usernamePassword(credentialsId: 'github-rdt-api', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          sh 'java -jar jenkins-cli.jar -s http://localhost:32000/ -auth $USERNAME:$PASSWORD reload-configuration'
        }
      }
    }
  }
}
