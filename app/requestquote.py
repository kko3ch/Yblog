import urllib.request,json
from . models import Quote

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

        print('author: ',quote_object.author)

    return quote_object
