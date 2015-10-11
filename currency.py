__author__ = 'Genevieve'

import web_utility

open('currency_details.txt', encoding='utf-8')


def convert(amount, home_currency, location_currency_code):
    url_string = "https://www.google.com/finance/converter?a={}&from={}&to={}".format(amount, home_currency, location_currency_code)

    result = web_utility.load_page(url_string)
    result = result[result.index('result'):]


    split_result = result.split('>')[2]
    conversion_amount = split_result.split(' ')[0]

    if conversion_amount == '\\n</div':
        return '-1.00'
    return conversion_amount


def details(country_name):
    in_file = open("currency_details.txt", 'r', encoding='utf-8')
    lines = in_file.readlines()
    if country_name == '':
         return tuple()
    for line in lines:
        if country_name in line:
            line = line.strip().split(',')
            line_info = line[0], line[1], line[2]
            return tuple(line_info)
    return tuple()
        # parts = line.strip().split(',')
        # if parts[0] == country_name:
        #     found = True
        # return(parts[0], parts[1], parts[2])
    # return()


# test to see if this stuff works


def main():
    amount = [1.00, 1.00, 1.00, 10.95, 943.18, 10.95, 13.62, 200.15, 13859.49, 100.00, 0.83, 19.99, 34.58, 19.99, 27.80]
    home_currency_code = ['AUD', 'JPY', 'ABC', 'AUD', 'JPY', 'AUD', 'BGN', 'BGN', 'JPY', 'JPY', 'USD', 'USD', 'BGN', 'USD', 'AUD']
    location_currency_code = ['AUD', 'ABC', 'USD', 'JPY', 'AUD', 'BGN', 'AUD', 'JPY', 'BGN', 'USD', 'JPY', 'BGN', 'USD', 'AUD', 'USD']

    for i in range(0,15):
        test = convert(amount[i], home_currency_code[i], location_currency_code[i])
        if test == '-1.00':
            valid = 'invalid conversion'
        else:
            valid = 'valid conversion'
        print(valid, amount[i], home_currency_code[i], ' -> ', location_currency_code[i], test)

    country_name = ('Unknown', 'Japanese', '', 'Australia', 'Japan', 'Hong Kong')
    for i in range(0, 3):
        print('invalid details ', details(country_name[i]))
    for i in range(3, 6):
        print('valid details', details(country_name[i]))




if __name__ == "__main__":
    # execute only if run as a script
    main()