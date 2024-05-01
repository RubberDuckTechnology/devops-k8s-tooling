# jenkins-jcac-mvp

## Sources

- https://www.jenkins.io/doc/book/managing/casc/
- https://www.youtube.com/watch?v=ANU7jkxbZSM
- https://github.com/darinpope/ansible-jenkins

## Docs

- https://github.com/darinpope/ansible-jenkins
- https://github.com/jenkinsci/matrix-auth-plugin/blob/master/src/test/resources/org/jenkinsci/plugins/matrixauth/integrations/casc/configuration-as-code-v3.yml
- https://plugins.jenkins.io/role-strategy/
- 
## Snippets

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
