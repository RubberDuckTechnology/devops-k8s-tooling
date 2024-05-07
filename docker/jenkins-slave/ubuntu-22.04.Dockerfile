FROM jenkins/agent:latest-bullseye-jdk11

# Switch to Jenkins user
USER jenkins

# Set the working directory
WORKDIR /home/jenkins

# Start the Jenkins slave agent
CMD ["java", "-jar", "/usr/share/jenkins/agent.jar", "-connectTo", "jenkins-service:32000", "-secret", "7edb200f25ab17c4b6c178d8bc465c98301a4bda738cc9c20c41183f96bd329e", "-workDir", "/home/jenkins"]