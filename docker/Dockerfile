FROM jenkins/jenkins:lts
USER root

# Copy plugin list
COPY docker/plugins.txt /usr/share/jenkins/ref/plugins.txt

# Install specified plugins
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt

USER jenkins
