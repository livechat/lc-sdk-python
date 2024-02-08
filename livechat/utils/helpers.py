'''
Helper methods which are used within SDK.
'''


def prepare_payload(parameters: dict) -> dict:
    ''' Prepares payload for request based on provided parameters by removing
        unnecessary or protected variables and removing `None` values. Please
        note that main use is to pass `locals()` as `parameters`.

        Args:
            parameters (dict): parameters provided as key -> value pairs.

        Returns:
            dict: payload object without unnecessary items to be used in requests.
    '''
    return {
        key: value
        for key, value in parameters.items()
        if key not in ['self', 'payload', 'headers', 'date_to', 'date_from']
        and value is not None
    }
