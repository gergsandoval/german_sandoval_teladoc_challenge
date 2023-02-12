from distutils.util import strtobool

class Helper:
    
    @staticmethod
    def string_to_bool(string):
        return bool(strtobool(str(string)))