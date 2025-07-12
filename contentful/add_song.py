def create_song_payload():
    """
    Create a payload for adding a new song to Contentful.
    
    :return: A dictionary representing the song entry payload.
    """
    return {
        'fields': {
            'songId': '',
            'songTitle': '',
            'length': '',
            'singers':[{}],
            'lyricists': [{}],
            'audioLinks': [{}]
        }
    }