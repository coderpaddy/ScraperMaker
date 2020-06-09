import sys

class ScrapeErrors:
    """
    Docstring
    """
    @staticmethod
    def data_field_options_error(obj):
        print(f" You have set {len(obj.which_data_fields)} fields to collect \n resseting...")
        obj.which_data_fields = obj.ask_data_fields()
        if len(obj.which_data_fields) > 0:
            return obj.ConfigureDataFields()
        else:
            print(" Something is going wrong, please start again")
            sys.exit()