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

        quote_results = None

        if quote_response:
            resonse_info = quote_response
            quote_results = process_quote(resonse_info)

        return quote_results

def process_quote(respone_quote):
    '''
    function that processes data from request
    '''
    quote_result = []

    id = respone_quote.get('id')
    author = respone_quote.get('author')
    quote = respone_quote.get('quote')

    quote_object = Quote(id,author,quote)
    quote_result.append(quote_object)

    return quote_result 
