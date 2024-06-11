# stop k8s
kubectl delete -f .k8s/20-jenkins-agents/ssh
kubectl delete -f .k8s/20-jenkins-agents/connect_to
kubectl delete -f .k8s/10-jenkins-controller
kubectl delete -f .k8s/02-openldap
kubectl delete -f .k8s/01-jenkins-operator
kubectl delete -f .k8s/
