# Start k8s
kubectl apply -f .k8s/
kubectl apply -f .k8s/openldap
kubectl apply -f .k8s/jenkins-agents/ssh
kubectl apply -f .k8s/jenkins-agents/connectto
kubectl apply -f .k8s/jenkins-controller
