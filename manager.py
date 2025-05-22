import json
from resource import Resource

STORAGE_FILE = "storage.json"

def load_resources():
    try:
        with open(STORAGE_FILE, 'r') as f:
            content = f.read()
            print("Raw content of storage.json:", repr(content))  # 👀
            return json.loads(content)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print("Error loading JSON:", e)
        return []

def save_resources(resources):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(resources, f, indent = 2)

def create_resource(name, rtype):
    resources = load_resources()
    new_resource = Resource(name, rtype).to_dictionary()
    resources.append(new_resource)
    save_resources(resources)
    return new_resource

def list_resources():
    return load_resources()

def delete_resource(resource_id):
    resources = load_resources()
    resources = [res for res in resources if res['id'] != resource_id]
    save_resources(resources)

