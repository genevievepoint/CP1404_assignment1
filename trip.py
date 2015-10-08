__author__ = 'Genevieve'


 open('currency_details.txt', encoding='utf-8')

# class Error:
#     def
#
 class Country:
     def __init__(self, name="", currency_code="", currency_symbol=""):
         self.name = name
         self.currency_code = currency_code
         self.currency_symbol = currency_symbol


    def currency_string(self):
        return "{}, self.currency_symbol{:.2f}".format(super().__str__(), self.currency_code, self.name)


    def __str__(self):
        return "self.name, self.currency_code, self.currency_symbol"

# class Details:
#     def __init__ (self, locations=""):
#         self.locations = locations
#
#
#     def add(self, country_name, start_date, end_date):
#         self.country_name = country_name
#         self.start_date = start_date
#         self.end_date = end_date
#
#
#     def current_country(self, date_string):
#         self.date_string = date_string
#         return
#
#     def is_empty(self):


