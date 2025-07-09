def create_album_payload(album_name):
    """
    Create a payload for adding a new album to Contentful.
    
    :param album_name: The name of the album to be added.
    :return: A dictionary representing the album entry payload.
    """
    return {
        'fields': {
            'title': {
                'en-US': album_name
            },
            'description': {
                'en-US': f'Description for {album_name}'
            }
        }
    }