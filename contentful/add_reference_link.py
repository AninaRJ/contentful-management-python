def create_reference_link_payload(ref_id='',spotify_url='', apple_music='', youtube_url=''):
    """
    Create a payload for adding a new audio reference link to Contentful.
    
    :return: A dictionary representing the reference link entry payload.
    """
    return {
        'fields': {
            'referenceId': ref_id,
            'spotifyUrl': spotify_url,
            'appleMusic': apple_music,
            'youtubeUrl': youtube_url
        }
    }