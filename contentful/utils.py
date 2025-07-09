import contentful_management
import os

space = os.environ['space_id']
environment = os.environ['environment']
access_token = os.environ['access_token']
client =  contentful_management.Client(access_token=access_token, space_id=space, environment_id=environment)

def create_entry(content_type_id, fields):
    entry = environment.create_entry(content_type_id, fields=fields)
    return entry

def get_entry(entry_id):
    entry = environment.get_entry(entry_id)
    return entry

def update_entry(entry_id, fields):
    entry = environment.update_entry(entry_id, fields=fields)
    return entry

def delete_entry(entry_id):
    environment.delete_entry(entry_id)
    return

def publish_entry(entry):
    entry.publish()
    return 