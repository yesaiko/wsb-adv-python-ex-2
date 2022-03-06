import requests


class Holidays:
    country_code = "PL"

    def get(self, year):
        response =  requests.get(f"https://date.nager.at/api/v3/publicholidays/{ year }/{ self.country_code }")
        return response.text

