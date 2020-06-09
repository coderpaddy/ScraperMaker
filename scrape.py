"""
This will serve as a helper class for:
A. Creation and testing of scraper
B. For the created scraper to be used.
"""

# Dependencies
import requests
from bs4 import BeautifulSoup


# Main Utility Class
# class ScrapeTools:

class ScrapeErrors:
    @staticmethod
    def data_field_options_error(obj):
        print(f" You have set {len(obj.which_data_fields)} fields to collect \n resseting...")
        obj.which_data_fields = obj.AskDataFields()
        if len(obj.which_data_fields) > 0:
            return obj.ConfigureDataFields()
        else:
            print(" Something is going wrong, please start again")
            exit()


class ScrapeOptions:
    def __init__(self):
        self.main_url = input(" Please enter the main url to scrape including http/https: ")
        self.which_data_fields = self.AskDataFields()
        self.data_field_options = self.ConfigureDataFields() if len(self.which_data_fields) > 0 else ScrapeErrors.data_field_options_error(self)
        self.has_own_data_pages = True if input("Would you like to scrape individual Product Pages? y/n: ").lower() == "y" else False
        self.link_for_each_data_page = self.GetPageUrlPattern() if self.has_own_data_pages is True else None
        self.start_scrape = self.IndividualScrape() if self.has_own_data_pages is True else self.SeperateScrape()

    
    def AskDataFields(self):
        data_fields_to_collect = []
        done = False
        while done is False:
            field_to_collect = input(" Please enter the name of this heading of data e.g Product Name: ")
            if field_to_collect != "":
                data_fields_to_collect.append(field_to_collect) 
            user_wants_more = input(" Would you like to add another field? y/n: ")
            if user_wants_more.lower() == "n":
                try_again = input(f" You have asked to search for:\n{[str(x) for x in data_fields_to_collect]}\n is this correct? y/n: ")
                if try_again.lower() == "y":
                    done = True
                else:
                    print(" reseting fields...")
                    data_fields_to_collect = []        
        return data_fields_to_collect

    def ConfigureDataFields(self):
        data_fields_options = {}
        for data_field in self.which_data_fields:
            data_fields_options[data_field] = {
                    "tag_type": input(" What Type of tag is the data inside? e.g div, a, h1: "),
                    "id_type": input(" How is the field differentiated? e.g id, class, name:"),
                    "search_term": input(" What is the identifying term? e.g title-class, attr-id:")
                }
        return data_fields_options

    def GetPageUrlPattern(self):
        print(" Pleas help to find the field with the individual data link...")
        page_url_pattern_options = {
                    "tag_type": True if input(" Is the link inside an <a> tag? y/n: ").lower() == "y" else input(" What tag is the url inside? e.g <div>, <a>: "),
                    "id_type": input(" How is the field differentiated? e.g id, class, name:"),
                    "search_term": input(" What is the identifying term? e.g title-class, attr-id:")
                }
        return page_url_pattern_options

    def IndividualScrape(self):
        print("individual")

    def SeperateScrape(self):
        print("seperate")

so = ScrapeOptions()
print(so.data_field_options)