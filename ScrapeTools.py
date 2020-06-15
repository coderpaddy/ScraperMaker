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
    def check_tag_attr(tag, attr):
        try:
            tag_attr = tag[attr]
            return tag_attr
        except KeyError as ke:
            return None
    
    @staticmethod
    def count_tags(soup):
        all_tags = soup.find_all()
        tag_dict = {}
        for a_tag in all_tags:
            if a_tag:
                all_attr = a_tag.attrs
                if "class" in all_attr.keys():
                    for act_class in all_attr["class"]:
                        if a_tag.name not in tag_dict.keys():
                            tag_dict[a_tag.name] = {
                                "classes": {},
                                "ids": {}
                            }
                        if act_class not in tag_dict[a_tag.name]["classes"].keys():
                            tag_dict[a_tag.name]["classes"][act_class] = 1
                        else:
                            tag_dict[a_tag.name]["classes"][act_class] += 1
                if "id" in all_attr.keys():
                    if a_tag.name not in tag_dict.keys():
                        tag_dict[a_tag.name] = {
                            "classes": {},
                            "ids": {}
                        }
                    act_id = a_tag.attrs["id"]
                    if act_id not in tag_dict[a_tag.name]["ids"].keys():
                        tag_dict[a_tag.name]["ids"][act_id] = 1
                    else:
                        tag_dict[a_tag.name]["ids"][act_id] += 1
        return tag_dict


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