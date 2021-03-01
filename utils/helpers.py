'''
Helper methods which are used within SDK.
'''


def parse_url_and_return_origin(url: str) -> str:
    ''' Parse url and return correct origin.

           Args:
                url (str): String which defines environment.

           Returns:
                str: String with correct origin depends on environment.
    '''
    domain = 'livechatinc.com'
    if 'labs' in url:
        return f'https://secure.labs.{domain}'
    if 'staging' in url:
        return f'https://secure-lc.{domain}'
    return f'https://secure.{domain}'


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
        if key not in ['self', 'payload'] and value is not None
    }
