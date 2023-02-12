from distutils.util import strtobool

class StringHelper:
    
    @staticmethod
    def string_to_bool(string):
        return bool(strtobool(str(string)))