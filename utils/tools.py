import re

def parse_url_and_return_origin(url):
    ''' Parse url and return correct origin '''
    pattern = r'\b(?:labs|staging)\b'
    found = re.search(pattern, url)
    if found:
        environment = found.group(0)
        if environment == 'labs':
            origin = 'https://secure.labs.livechatinc.com'
        else:
            origin = 'https://secure-lc.livechatinc.com'
    else:
        origin = 'https://secure.livechatinc.com'
    return origin
