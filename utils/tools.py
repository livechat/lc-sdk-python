

def parse_url_and_return_origin(url) -> str:
    ''' Parse url and return correct origin.
           Args:
                url(str): String which defines environment.
    '''
    domain = 'livechatinc.com'
    if 'labs' in url:
        return f'https://secure.labs.{domain}'
    elif 'staging' in url:
        return f'https://secure-lc.{domain}'
    else:
        return f'https://secure.{domain}'
