import json
import sys
import argparse


def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class BankAPI(object):
    def __init__(self):
        self.version = "{1.0}"
        self.accounts = {"token1": 1000.00, "token2": 2000.00}
        self.payments = []
    def get_access_key(self, jsonfile, jsonkey):
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return str(self.version + obj[jsonkey])



if len(sys.argv) == 2 and sys.argv[1] == "-h":
    print("This program extracts the API access key to use the services of a bank.")
    print("Usage: {executable path}/getJason.pyc {path JSON file}/{file name JSON}.json")
    print("Example: ./getJason.pyc ./sitedata.json")
    print("The access key can be retrieved from the standard output in the format:")
    print("{1.0}XXXX-XXXX-XXXX-XXXX")
else:
    # Parse the command-line arguments using argparse
    PARSER = argparse.ArgumentParser(description='Extract the API access key to use the services.')
    PARSER.add_argument('jsonfile', type=str, help='Path to the JSON file with the access key')
    PARSER.add_argument('jsonkey', type=str, help='Key to extract from the JSON file')
    ARGS = PARSER.parse_args()


    BANK_API = BankAPI()
    try:
        print(BANK_API.get_access_key(ARGS.jsonfile, ARGS.jsonkey))

    except IOError:
        print("The specified file was not found or cannot be opened.")
    except KeyError:
        print("The specified key was not found in the JSON file.")
    except IndexError:
        print("The specified index was not found or is invalid.")
# okay decompiling getJason.pyc