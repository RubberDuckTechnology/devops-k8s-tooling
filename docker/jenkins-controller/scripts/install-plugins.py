import yaml
import subprocess
import sys

def install_plugins(yaml_file):
    with open(yaml_file, 'r') as file:
        config = yaml.safe_load(file)
        
    plugins = config.get('plugins', [])
    for plugin in plugins:
        name = plugin.get('name')
        version = plugin.get('version')
        if name and version:
            plugin_spec = f"{name}:{version}"
            subprocess.run(["jenkins-plugin-cli", "--plugins", plugin_spec], check=True)
        else:
            print(f"Invalid plugin entry: {plugin}", file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: install-plugins.py <path to plugins.yaml>", file=sys.stderr)
        sys.exit(1)
    
    yaml_file = sys.argv[1]
    install_plugins(yaml_file)
