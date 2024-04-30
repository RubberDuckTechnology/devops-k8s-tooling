FROM jenkins/jenkins:lts
USER root

# Copy plugin list
COPY docker/plugins.txt /usr/share/jenkins/ref/plugins.txt
COPY docker/jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

# Install specified plugins
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

USER jenkins
