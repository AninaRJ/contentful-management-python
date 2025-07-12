def create_label_payload():
    """
    Create a payload for adding a new label to Contentful.
    
    :return: A dictionary representing the label entry payload.
    """
    return {
        'fields': {
            'labelId': '',
            'labelName': '',
            'labelDescription': '',
            'wikipediaUrl': '',
            'startYear': ''
        }
    }