__author__ = 'Genevieve'

import web_utility
from trip import Country
from trip import Details

open('currency_details.txt', encoding='utf-8')


def convert(amount, home_currency, location_currency_code):
    amount = input("please enter the amount you wish to convert")
    home_currency = input("Please enter your current currency")
    location_currency_code = input("Please enter where you are going")
    url = 'https://www.google.com/finance/converter='
    values = {amount, home_currency, location_currency_code}
    url_string = url + values
    result = web_utility.load_page(url_string)
    print(result[result.index('result'):])



# def get_details(country_name):
#     country_name = input("Please enter a country ")
#     found = False
#     in_file = open("currency_details.txt", encoding='utf-8')
#     for line in in_file:
#         parts = line.strip().split(',')
#     if parts[0] == country_name:
#         found = True
#         print(parts[0], parts[1], parts[2])
#     if found == False:
#         print('', ' , ', '', ' , ',  '')
