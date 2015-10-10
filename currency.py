__author__ = 'Genevieve'

from web_utility import load_page
from trip import Country
from trip import Details
from trip import Error

open('currency_details.txt', encoding='utf-8')


def convert(amount, home_currency, location_currency_code):
    amount = input("please enter the amount you wish to convert")
    if amount <= 0:
        print('-1')
    else:
        amount = amount

    home_currency = get_details()
    location_currency_code = get_details()
    url = 'https://www.google.com/finance/converter?a='.join(amount, home_currency, location_currency_code)
    url_string = url
    result = web_utility.load_page(url_string)
    print(result[result.index('result'):])


def get_details(country_name):
    country_name = input("Please enter a country ")
    found = False
    in_file = open("currency_details.txt", encoding='utf-8')
    for line in in_file:
        parts = line.strip().split(',')
    if parts[0] == country_name:
        found = True
        return(parts[1])
    if found == False:
         print('', ' , ', '', ' , ',  '')