# Start k8s
kubectl apply -f .k8s/
kubectl apply -f .k8s/01-jenkins-operator
kubectl apply -f .k8s/02-openldap
kubectl apply -f .k8s/10-jenkins-controller
kubectl apply -f .k8s/20-jenkins-agents/connect_to
kubectl apply -f .k8s/20-jenkins-agents/ssh
