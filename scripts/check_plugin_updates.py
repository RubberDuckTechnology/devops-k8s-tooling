import requests
import yaml
import subprocess
import os
import sys

# Configuration
GITLAB_API_TOKEN = os.getenv("GITLAB_API_TOKEN")
GITLAB_PROJECT_ID = os.getenv("CI_PROJECT_ID")
GITLAB_API_URL = f"https://gitlab.com/api/v4/projects/{GITLAB_PROJECT_ID}"
PLUGINS_FILE="docker/jenkins-controller/config/plugins.yaml"
UPDATE_CENTER_URL = "https://updates.jenkins.io/current/update-center.json"

# Fetch the latest plugin versions from the Jenkins Update Center
def fetch_latest_plugin_versions():
    response = requests.get(UPDATE_CENTER_URL)
    response.raise_for_status()
    update_center = response.json()
    return {plugin: data["version"] for plugin, data in update_center["plugins"].items()}

# Load the current plugins and their versions from plugins.yaml
def load_current_plugins():
    with open(PLUGINS_FILE, "r") as file:
        plugins = yaml.safe_load(file)
    return {plugin["name"]: plugin["version"] for plugin in plugins["plugins"]}

# Save the updated plugins to plugins.yaml
def save_updated_plugins(plugins):
    with open(PLUGINS_FILE, "w") as file:
        yaml.dump({"plugins": [{"name": name, "version": version} for name, version in plugins.items()]}, file)

# Create a new Git branch and commit the changes
def commit_changes():
    subprocess.run(["git", "checkout", "-b", "update-plugins"], check=True)
    subprocess.run(["git", "add", PLUGINS_FILE], check=True)
    subprocess.run(["git", "commit", "-m", "Update Jenkins plugins"], check=True)
    subprocess.run(["git", "push", "--set-upstream", "origin", "update-plugins"], check=True)

# Create a merge request in GitLab
def create_merge_request():
    headers = {"PRIVATE-TOKEN": GITLAB_API_TOKEN}
    data = {
        "source_branch": "update-plugins",
        "target_branch": "main",
        "title": "Update Jenkins plugins"
    }
    response = requests.post(f"{GITLAB_API_URL}/merge_requests", headers=headers, data=data)
    response.raise_for_status()
    print("Merge request created successfully")

def main():
    # Fetch the latest plugin versions
    latest_versions = fetch_latest_plugin_versions()

    # Load the current plugin versions
    current_plugins = load_current_plugins()

    # Check for updates and apply them
    updates_available = False
    for plugin, current_version in current_plugins.items():
        latest_version = latest_versions.get(plugin)
        if latest_version and current_version != latest_version:
            print(f"Update available for {plugin}: {current_version} -> {latest_version}")
            current_plugins[plugin] = latest_version
            updates_available = True

    if updates_available:
        # Save the updated plugins to plugins.yaml
        save_updated_plugins(current_plugins)

        # Commit the changes and create a merge request
        commit_changes()
        create_merge_request()
    else:
        print("No updates available.")

if __name__ == "__main__":
    if not GITLAB_API_TOKEN:
        print("Error: GITLAB_API_TOKEN environment variable not set.")
        sys.exit(1)
    if not GITLAB_PROJECT_ID:
        print("Error: CI_PROJECT_ID environment variable not set.")
        sys.exit(1)
    main()
