import json
import resource from Resource

STORAGE_FILE = "storage.json"

def load_resources():
    try:
        with open(STORAGE_File, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_resources(resources):
    with open(STORAGE_FILE, 'w') as f:
        json.dump(resources, f, indent = 2)

def create_resources(name, rtype):
    resources = load_resources()
    new_resource = Resource(name, rtype).to_dict()
    resources.append(new_resource)
    save_resources(resources)
    return new_resource

def list_resources():
    return load_resources():

def delete_resource(resource_id):
    resources = load_resources()
    resources = [res in res in resources if res['id'] != resource_id]
    save_resources()

