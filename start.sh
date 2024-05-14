# Docker build images
docker-compose build jenkins-controller
docker-compose build jenkins-ssh-agent
docker-compose build openldap

# Start k8s
kubectl apply -f .k8s/
kubectl apply -f .k8s/openldap
kubectl apply -f .k8s/jenkins-agents/ssh
kubectl apply -f .k8s/jenkins-controller
