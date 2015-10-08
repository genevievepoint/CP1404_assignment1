__author__ = 'Genevieve'

from web_utility import load_page

open('currency_details.txt', encoding='utf-8')


# def convert(amount, home_currency, location_currency_code):




def get_details(country_name):
    country = input("Please enter a country ")
    found = False
    in_file = open("currency_details.txt", encoding='utf-8')
    for line in in_file:
        parts = line.strip().split(',')
    if parts[0] == country:
        found = True
        print("In ", parts[0], "the currency is ", parts[1], "and the symbol is", parts[2])
    if found == False:
        print('Country has gone missing!')
