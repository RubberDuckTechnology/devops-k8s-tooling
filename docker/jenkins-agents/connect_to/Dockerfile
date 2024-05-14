FROM jenkins/agent:latest-bullseye-jdk11

ENV TZ=Europe/Amsterdam

# Switch to Jenkins user
USER jenkins

# Set the working directory
WORKDIR /home/jenkins

# Start the Jenkins  agent
COPY docker/jenkins-agent/agent.jar /home/jenkins/agent.jar
CMD ["java", "-jar", "agent.jar", "-connectTo", "jenkins-service:8080", "-secret", "89467600f29d07d6ff5a6b88c7f98c1e80f5da4080cf8ddb37f76e2d32c7c515", "-name", "buildhost_minions_ubuntu", "-workDir", "/home/jenkins"]