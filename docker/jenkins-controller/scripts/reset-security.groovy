import jenkins.model.*
import hudson.security.*

def instance = Jenkins.getInstance()

// Disable security
instance.disableSecurity()

// Save the configuration
instance.save()
