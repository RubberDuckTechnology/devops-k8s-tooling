FROM jenkins/jenkins:lts

# Install necessary tools
USER root
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pyyaml

# Copy and install plugins
COPY config/plugins.yaml /usr/share/jenkins/ref/plugins.yaml
COPY scripts/install-plugins.py /usr/local/bin/install-plugins.py
RUN python3 /usr/local/bin/install-plugins.py /usr/share/jenkins/ref/plugins.yaml

# Copy JCasC configuration
COPY config/jenkins.yaml /usr/share/jenkins/ref/jenkins.yaml
ENV CASC_JENKINS_CONFIG=/usr/share/jenkins/ref/jenkins.yaml

COPY scripts/set-casc-reload-token.groovy /usr/share/jenkins/ref/init.groovy.d/set-casc-reload-token.groovy
# COPY scripts/reset-security.groovy /usr/share/jenkins/ref/init.groovy.d/reset-security.groovy

# Disable initial setup
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false

USER jenkins
