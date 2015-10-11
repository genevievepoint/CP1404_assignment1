__author__ = 'Genevieve'


class Error:
    def __init__(self, value):
        super().__init__(value)


class Country:
    def __init__(self, name="", currency_code="", currency_symbol=""):
        self.name = name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol

    def currency_string(self, amount):
        amount = '{:.2f}'.format(amount)
        return str(amount)

    def __str__(self):
        return self.name + ' ' + self.currency_code + ' ' + self.currency_symbol + ' '


class Details:
    def __init__ (self):
        self.locations = []

    def add(self, country_name, start_date, end_date):
        self.locations.append((country_name, start_date, end_date))
        start_date = start_date.strip().split('/')
        if len(start_date[0]) < 4 and len(start_date[1]) < 2 and len(start_date[2]) <2:
            raise Error('Date does not follow format. YYYY/MM/DD')
        end_date = end_date.strip().split('/')
        if len(end_date[0]) < 4 and len(end_date[1]) < 2 and len(end_date[2]) < 2:
            raise Error('Date does not follow format. YYYY/MM/DD')
        if start_date < end_date:
            self.locations.append((country_name, start_date, end_date))
        else:
            raise Error('End date is before start date')



    def current_country(self, date_string):
        for location in self.locations:
            if location[1] <= date_string <= location[2]:
                return location[0]
        raise Error('Date not found')

    def is_empty(self, is_empty):
        if self.locations is False:
            return False
        else:
            return True



def main():
    australia = Country('Australia', 'AUD', '$')
    print(australia.currency_string(100.236))
    print(australia)




if __name__ == "__main__":
     # execute only if run as a script
    main()