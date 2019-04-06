""" Used to load static json files """
from os import path
from json import load

SITE_ROOT = "api"

def getStaticData(name_file):
    """ Description
    :type name_file: String
    :param name_file: The name of the static file we want to load

    :raises: IOError if the file doesnt' exist

    :rtype: The data
    """    
    json_url = path.join(SITE_ROOT, "static", name_file)
    # We verify that the file exists before we load it
    if path.exists(json_url):
        return load(open(json_url))
    else:
        # If the file doesn't exit we raise an Exception
        raise FileNotFoundError("The file doesn't exist: " + json_url)