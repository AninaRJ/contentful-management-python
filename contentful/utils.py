import contentful_management
from dotenv import load_dotenv
import os
load_dotenv()

space = os.environ.get("space_id")
environment = os.environ.get("environment")
cma_token =  os.environ.get("cma_token")
client =  contentful_management.Client(cma_token)
music_space = client.spaces().find(space)
environment = music_space.environments().find('master')

def create_entry(entry_id, entry_attributes):
    existing_entry = get_entry(entry_id)
    if existing_entry is not None:
        print(f"Entry with ID {entry_id} already exists.")
        return existing_entry
    entry = environment.entries().create(entry_id, entry_attributes)
    if not entry:
        raise Exception(f"Failed to create entry with ID {entry_id}.")
    publish_entry(entry)
    return entry

def get_entry(entry_id):
    try:
        entry = environment.entries().find(entry_id)
        return entry
    except contentful_management.errors.NotFoundError:
        # Entry not found
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def update_entry(entry_id, fields):
    entry = environment.update_entry(entry_id, fields=fields)
    return entry

def delete_entry(entry_id):
    environment.delete_entry(entry_id)
    return

def publish_entry(entry):
    entry.publish()
    return 

### Non Contentful Functions ###
def transform_title_to_id(title):
    """
    Transform the album title into a suitable ID format.
    
    :param album_title: The title of the album.
    :return: A string representing the album ID.
    """
    return title.lower().replace(" ", "-").replace("'", "").replace(".", "")