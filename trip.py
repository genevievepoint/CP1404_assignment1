__author__ = 'Genevieve'


class Error:
    def __init__(self, value, **kwargs):
        super(Error, self).__init__(value)


class Country:
    def __init__(self, name="", currency_code="", currency_symbol=""):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def currency_value(self, amount):
        amount = '{:.2f}'.format(amount)
        return str(amount)

    def __str__(self):
        return "self.name, self.currency_code, self.currency_symbol"


class Details:
    def __init__ (self, locations=""):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        self.locations.append((country_name, start_date, end_date))
        start_date = '[0] / [1] / [2]'.format(start_date[0], start_date[1], start_date[2])
        end_date = '[0] / [1] / [2]'.format(end_date[0], end_date[1], end_date[2])

        try:
            if start_day < end_date:



    def current_country(self, date_string):
        for location in
        self.date_string = date_string
        return

    def is_empty(self, is_empty):
        self.is_empty = is_empty

