import urllib.request,json
from . models import Quote
import requests

api_key = None
list_id = None
data_center = 'us10'

def configure_request(app):
    '''
    function to get api_key and list_id
    '''
    global api_key
    global list_id
    api_key = app.config['MAILCHIMP_API_KEY']
    list_id = app.config['MAILCHIMP_EMAIL_LIST_ID']

mail_chimp_base_url = f'https://{data_center}.api.mailchimp.com/3.0'
members_endpoint = f'{mail_chimp_base_url}/lists/{list_id}/members'

def subscribe_user(email):
    data = {
        "email_address": email,
        "status": "subscribed"
    }
    r = requests.post(
        members_endpoint,
        auth=("", api_key),
        data=json.dumps(data)
    )
    return r.status_code, r.json()

def get_random_quote():
    '''
    function to get random quote
    '''
    random_quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(random_quote_url) as url:
        quote_data = url.read()
        quote_response = json.loads(quote_data)

        id = quote_response.get('id')
        author = quote_response.get('author')
        quote = quote_response.get('quote')
        
        quote_object = Quote(id,author,quote)

    return quote_object


    







