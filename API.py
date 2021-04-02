import requests

def api():
    '''Returns project's API.'''

    url = 'https://api-escapamet.vercel.app/'

    response = requests.request('GET', url)

    return response.json()

def get_api():
    pass