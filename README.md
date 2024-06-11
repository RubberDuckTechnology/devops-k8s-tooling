# jenkins-jcac-mvp

## Sources

- https://www.jenkins.io/doc/book/managing/casc/
- https://www.youtube.com/watch?v=ANU7jkxbZSM
- https://github.com/darinpope/ansible-jenkins

## Docs

- https://github.com/darinpope/ansible-jenkins
- https://github.com/jenkinsci/matrix-auth-plugin/blob/master/src/test/resources/org/jenkinsci/plugins/matrixauth/integrations/casc/configuration-as-code-v3.yml
- https://jenkinsci.github.io/kubernetes-operator/docs/

## Snippets

## Starting Jenkins (Operator)

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
