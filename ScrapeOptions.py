"""
This will serve as a helper class for:
A. Creation and testing of scraper
B. For the created scraper to be used.
"""

# Dependencies
import sys
import requests
from bs4 import BeautifulSoup
from ScrapeTools import ScrapeTools
from ScrapeErrors import ScrapeErrors


# Main Utility Class
class ScrapeOptions:
    """
    Docstring
    """
    def __init__(self, main_url=None):
        self.main_url = main_url if main_url is not None else input(" Please enter the main url to scrape including http/https: ")
        self.has_own_data_pages = True if input("Does each item of data have its own page? y/n: ").lower() == "y" else False
        self.main_soup = ScrapeTools.get_soup(self.main_url)
        self.which_data_fields = self.ask_data_fields()
        self.data_field_options = self.configure_data_fields() if len(self.which_data_fields) > 0 else ScrapeErrors.data_field_options_error(self)
        self.link_for_each_data_page = self.get_page_url_pattern() if self.has_own_data_pages is True else None
        self.start_scrape = self.individual_page_scrape() if self.has_own_data_pages is True else self.all_together_scrape()

    def ask_data_fields(self):
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

    def configure_data_fields(self):
        data_fields_options = {}
        for data_field in self.which_data_fields:
            print(f" Configuring {data_field}: \n")
            data_fields_options[data_field] = {
                "tag_type": input(" What Type of tag is the data inside? e.g div, a, h1: "),
                "id_type": input(" How is the field differentiated? e.g id, class, name:"),
                "search_term": input(" What is the identifying term? e.g title-class, attr-id:")
            }
        return data_fields_options

    def get_page_url_pattern(self):
        print(" Pleas help to find the field with the individual data link...")
        page_url_pattern_options = {
            "tag_type": True if input(" Is the link inside an <a> tag? y/n: ").lower() == "y" else input(" What tag is the url inside? e.g <div>, <a>: "),
            "id_type": input(" How is the field differentiated? e.g id, class, name:"),
            "search_term": input(" What is the identifying term? e.g title-class, attr-id:")
        }
        return page_url_pattern_options

    def individual_page_scrape(self):
        print(" individual")

    def all_together_scrape(self):
        print(" All Together")


url = "https://www.blackhatworld.com/forums/brand-new-to-bhw.261/"
so = ScrapeOptions(main_url=url)
print(ScrapeTools.count_tags(so.main_soup))
