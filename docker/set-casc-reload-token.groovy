import java.util.UUID

def generateToken() {
    return UUID.randomUUID().toString()
}

def token = generateToken()
System.setProperty("casc.reload.token", token)
println "casc.reload.token set to: $token"
