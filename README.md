# Devops tooling

## Jenkins

### Sources

- https://www.jenkins.io/doc/book/managing/casc/
- https://www.youtube.com/watch?v=ANU7jkxbZSM
- https://github.com/darinpope/ansible-jenkins

### Docs

- https://github.com/darinpope/ansible-jenkins
- https://github.com/jenkinsci/matrix-auth-plugin/blob/master/src/test/resources/org/jenkinsci/plugins/matrixauth/integrations/casc/configuration-as-code-v3.yml
- https://jenkinsci.github.io/kubernetes-operator/docs/

### Snippets

### Starting Jenkins (Operator)

```sh
./scripts/start.sh
kubectl get secret jenkins-operator-credentials-jenkins-master -n devops-tools -o 'jsonpath={.data.user}' | base64 -d
kubectl get secret jenkins-operator-credentials-jenkins-master -n devops-tools -o 'jsonpath={.data.password}' | base64 -d
kubectl port-forward jenkins-jenkins-master -n devops-tools 8080:8080
```

### Export current plugin name en versions

```groovy
Jenkins.instance.pluginManager.plugins.each{
  plugin ->
  println ("${plugin.getShortName()}:${plugin.getVersion()}")
}
```

### Get casc.reload.token

```groovy
println(System.getProperty("casc.reload.token"))
```

### Reset Jenkins security settings

```bash
sed -i 's/<useSecurity>true<\/useSecurity>/<useSecurity>false<\/useSecurity>/g' /var/jenkins_home/config.xml 
```

## Gitlab

### Deploy

```sh
kubectl apply -f .k8s/03-cert-manager
kubectl apply -f .k8s/40-gitlab
```

### Add Gitlab to hosts

```txt
127.0.0.1 gitlab.devops-gitlab.com
127.0.0.1 kas.devops-gitlab.com
127.0.0.1 minio.devops-gitlab.com
127.0.0.1 registry.devops-gitlab.com
```

### Get password

```sh
kubectl get secret gitlab-gitlab-initial-root-password -ojsonpath='{.data.password}' | base64 --decode ; echo
```

### Add k8s Gitlab as a remote to your local Git repo

```sh
git remote set-url --add --push origin <url> https://gitlab.devops-gitlab.com/admin
```

### My account credentials

Username: zbarnoussi
Password: Assasin!

## TODO's

[] Jenkins with domain name (use LoadBalancer)
[] OpenLDAP with domain name (use LoadBalancer)
[] Authenticate Gitlab using OpenLDAP
[] Nexus Repository working
