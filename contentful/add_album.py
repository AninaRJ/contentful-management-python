from contentful.utils import transform_title_to_id
from contentful.add_reference_link import create_reference_link_payload

def create_album_payload(album_title, album_description='', language='', year_released='', album_links=[], lyricists=[], songs=None, album_label=None, awards='', lead_actors=''):
    """
    Create a payload for adding a new album to Contentful.
    
    :param album_title: The name of the album to be added.
    :return: A dictionary representing the album entry payload.
    """

    if album_links is not None:
        album_links = create_reference_link_payload(album_links[0], album_links[1], album_links[2], album_links[3])
    
   # if lyricists is not None:
    #    lyricist_id = transform_title_to_id(lyricists[0].get('lyricistName', ''))
        

    return {
        'fields': {
          'albumId': transform_title_to_id(album_title),
          'albumTitle': album_title,
          'albumDescription': album_description,
          'language': language,
          'yearReleased': year_released,
          'albumLinks': album_links,
          'lyricists': [{}],
          'songs': [{}],
          'albumLabel': [{}],
          'awards': awards,
          'leadActors': lead_actors
        }
    }