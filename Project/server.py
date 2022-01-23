from flask import Flask, render_template, request

from pprint import pformat
import os
import requests


app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'
#remove in production
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

API_KEY = os.environ['YAHOO_KEY']


# @app.route('/')
# def homepage():
#     """Show homepage."""

#     return render_template('homepage.html')


# @app.route('/afterparty')
# def show_afterparty_form():
#     """Show event search form"""

#     return render_template('search-form.html')


@app.route('/')
def show_stock_data():
    """Search for afterparties on Eventbrite"""

    # url = "https://yfapi.net/v6/finance/quote"
    #querystring = {"symbols":"AAPL"}

    url = "https://yfapi.net/v1/finance/trending/US"
    querystring = {"region":"US"}

    headers = {'X-API-KEY': API_KEY}

    data = requests.request("GET", url, headers=headers, params=querystring)
    # data = requests.request("GET", url, headers=headers, params=querystring)
    json_data = data.json()
    # AAPL_quote = json_data['quoteResponse']['result'][0]
    # ticker = json_data['quoteResponse']['result'][0]['symbol']
    # stocks = data[symbol]
    #print(data.text)

    return render_template('base.html',
                           pformat=pformat,
                           data=json_data
                           )


# @app.route('/event/<id>')
# def get_event_details(id):
#     """View the details of an event."""

#     url = f'https://app.ticketmaster.com/discovery/v2/events/{id}'
#     payload = {'apikey': API_KEY}

#     response = requests.get(url, params=payload)

#     event = response.json()
#     venues = event['_embedded']['venues']

#     return render_template('event-details.html',
#                            event=event,
#                            venues=venues)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
