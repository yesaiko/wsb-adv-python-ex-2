import requests
import json

class Holidays:
    country_code = "PL"
    needed_holidays = []

    def __init__(self, yearfrom, yearto, holidays):
        self.needed_holidays = holidays
        years = list(range(int(yearfrom), int(yearto)))
        if yearfrom == yearto:
            years = [yearfrom]
        print(years)
        holidays = [self.get(year) for year in years]
        print(holidays)

    def get(self, year):
        response =  requests.get(f"https://date.nager.at/api/v3/publicholidays/{ year }/{ self.country_code }")
        return response.text

    def get_dates(holidays):
        for holiday in holidays:
            data = json.loads(holiday)
            
class Holiday:
    name = ""
    date = ""
        

