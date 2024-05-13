FROM jenkins/jenkins:lts
USER root

# Copy plugin list
COPY ./docker/jenkins-controller/plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY ./docker/jenkins-controller/jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml
COPY ./docker/jenkins-controller/set-casc-reload-token.groovy /usr/share/jenkins/ref/init.groovy.d/set-casc-reload-token.groovy
COPY ./docker/jenkins-controller/reset-security.groovy /usr/share/jenkins/ref/init.groovy.d/reset-security.groovy
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

# Install specified plugins
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

# Disable initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

USER jenkins
