FROM jenkins/agent:latest-bullseye-jdk11

ENV TZ=Europe/Amsterdam

# Switch to Jenkins user
USER jenkins

# Set the working directory
WORKDIR /home/jenkins

# Start the Jenkins  agent
COPY agent.jar /home/jenkins/agent.jar
CMD ["java", "-jar", "agent.jar", "-url", "http://jenkins-service:8080/", "-secret", "be474ed015945f2c4c6da309499b525973134924611d6bb5479726fa9ce079fd", "-name", "buildhost_cyphers_ubuntu", "-workDir", "/home/jenkins"]