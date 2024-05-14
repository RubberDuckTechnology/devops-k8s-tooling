# Start k8s
kubectl delete -f .k8s/jenkins-controller
kubectl delete -f .k8s/jenkins-agents/ssh
kubectl delete -f .k8s/openldap
kubectl delete -f .k8s/
