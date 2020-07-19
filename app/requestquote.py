import urllib.request,json
from . models import Quote
import requests

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

# def subscribe_user(email, user_email, api_key):

# 	return requests.post(
# 		"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages",
# 		auth=("api", api_key),
# 		data={"from": user_email,
# 			"to": ["bar@example.com", "YOU@YOUR_DOMAIN_NAME"],
# 			"subject": "Hello",
# 			"text": "Testing some Mailgun awesomness!"})                                )










