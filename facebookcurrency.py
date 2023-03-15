import requests
from bs4 import BeautifulSoup
import facebook
import time
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler

# Authentication keys for Facebook API
access_token = 'your_access_token'
page_id = 'your_page_id'

# Authenticate with Facebook API
graph = facebook.GraphAPI(access_token)
facebook_page = graph.get_object(page_id)

# Define the URL for currency exchange rates
url = 'https://finance.yahoo.com/currencies'

# Define a function to scrape and post currency exchange rates
def post_currency_exchange_rate():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    exchange_rates = {}
    for row in soup.select('table tr'):
        cells = row.select('td')
        if len(cells) > 1:
            exchange_rate = cells[1].text.strip()
            exchange_rates[cells[0].text.strip()] = exchange_rate
    message = 'Currency exchange rates:\n\n'
    for currency, exchange_rate in exchange_rates.items():
        message += '{}: {}\n'.format(currency, exchange_rate)
    graph.put_object(facebook_page['id'], 'feed', message=message)

# Set up a scheduler to post currency exchange rates every hour
scheduler = BlockingScheduler()
scheduler.add_job(post_currency_exchange_rate, 'interval', hours=1)

# Start the scheduler
scheduler.start()
