import sys
import requests
from bs4 import BeautifulSoup

class ScrapeTools:
    """
    Docstring
    """
    @staticmethod
    def get_soup(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html.parser')
        return soup

    @staticmethod
    def get_element(soup, tag_type, id_type, search_term):
        if id_type == "class":
            actual_element = soup.find(tag_type, class_=search_term)
        elif id_type == "id":
            actual_element = soup.find(tag_type, id=search_term)
        else:
            actual_element = soup.find(tag_type, {id_type: search_term})
        return actual_element

    
    @staticmethod
    def count_tags(soup):
        how_much_data = int(input(" How many items of data on this page? : "))
        all_tags = soup.find_all()
        tag_names = [
            {x.name: {
                "class": try x["class"] except KeyError False,
                "id": try x["id"] except KeyError False
                }
            } for x in all_tags]
        """tag_count = {}
        for tag in all_tags:
            if tag in tag_count.keys()"""
        return tag_names


    @staticmethod
    def test_get_elements(soup, element_options):
        test_data = {}
        for key in element_options.keys():
            field_name, tag_type, id_type, search_term = key, element_options["tag_type"], element_options["id_type"], element_options["search_term"]
            actual_element = ScrapeTools.get_element(soup, tag_type, id_type, search_term)
            test_data[field_name] = actual_element
        print(test_data)
        is_correct_data = input(" Is this example correct? y/n: ").lower()
        if is_correct_data == "n":
            print(" It is probably best to start again ... \n exiting now")
            sys.exit()
        else:
            return True