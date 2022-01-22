from flask import Flask, render_template, request

from pprint import pformat
import os
import requests


app = Flask(__name__)
app.secret_key = 'SECRETSECRETSECRET'


API_KEY = os.environ['YAHOO_KEY']


@app.route('/')
def homepage():
    """Show homepage."""

    return render_template('homepage.html')


@app.route('/afterparty')
def show_afterparty_form():
    """Show event search form"""

    return render_template('search-form.html')


@app.route('/afterparty/search')
def find_afterparties():
    """Search for afterparties on Eventbrite"""

    url = "https://yfapi.net/v6/finance/quote"

    querystring = {"symbols":"AAPL,BTC-USD,EURUSD=X"}

    headers = {
        'x-api-key': YAHOO_KEY
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return render_template('search-results.html',
                           pformat=pformat,
                           data=data,
                           results=events)


@app.route('/event/<id>')
def get_event_details(id):
    """View the details of an event."""

    url = f'https://app.ticketmaster.com/discovery/v2/events/{id}'
    payload = {'apikey': API_KEY}

    response = requests.get(url, params=payload)

    event = response.json()
    venues = event['_embedded']['venues']

    return render_template('event-details.html',
                           event=event,
                           venues=venues)


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
