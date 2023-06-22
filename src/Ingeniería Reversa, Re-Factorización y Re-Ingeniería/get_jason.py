# Import necessary modules
import json
import sys
import argparse

# pylint: disable=too-few-public-methods

# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (default, Jun  8 2023, 22:55:19)
# [GCC 13.1.1 20230429]
# Embedded file name: getJason.py
# Compiled at: 2022-06-14 16:15:55


"""

    This program is the property of the company IS2© 2022,2023. All rights reserved.


    This program extracts the API access key to use the services of a bank.
    It takes two arguments:
    - The path to the JSON file containing the access key and
    - the key to extract from the JSON file.
    The program uses the Singleton pattern to ensure that only one
    instance of the BankAPI class is created.
    The program also uses the argparse module to parse the command-line arguments
    and validate them before retrieving the access key.
    If the access key cannot be retrieved, the program prints an error message.
"""


# Define a decorator to implement the Singleton pattern
def singleton(cls):
    """
    A decorator that implements the Singleton pattern in Python.

    Args:
        cls (class): The class to decorate.

    Returns:
        class: A new class that can only be instantiated once.
    """
    instances = {}
    def getinstance():
        """
        Returns the single instance of the decorated class.

        If the instance does not exist, it is created and stored in the `instances` dictionary.

        Returns:
            object: The single instance of the decorated class.
        """
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

# Define a class to represent the bank API
@singleton
class BankAPI(object):
    """
    A class to represent the bank API.

    Attributes:
        version (str): The version of the bank API.
        balance (float): The current account balance.
    """
    def __init__(self):
        """
        Initializes the BankAPI class.

        Sets the version of the bank API to "{1.0}" and the account balance to 0.
        """
        self.version = "{1.0}"
        self.accounts = {"token1": 1000.00, "token2": 2000.00}
        self.payments = []
    def get_access_key(self, jsonfile, jsonkey):
        """
        Retrieves the API access key from a JSON file.

        Arguments:
            jsonfile (str): The path to the JSON file containing the access key.
            jsonkey (str): The key to extract from the JSON file.

        Returns:
            str: The API access key in the format "{version}{access_key}".
        """
        with open(jsonfile, 'r') as myfile:
            data = myfile.read()
        obj = json.loads(data)
        return str(self.version + obj[jsonkey])
    def get_balance(self, token):
        """
        Retrieves the current account balance.

        Returns:
            float: The current account balance.
        """
        return self.accounts[token]

    def make_payment(self, order_number, token, amount):
        """
        Makes a payment from the account corresponding to the given token.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made.
        """
        if token in self.accounts:
            if self.accounts[token] >= amount:
                self.accounts[token] -= amount
                self.payments.append((order_number, token, amount))
                return "Payment %d of %.2f made from %s." % (order_number, amount, token)
            else:
                return "Payment %d of %.2f from %s failed due to insufficient balance." % (order_number, amount, token)
        else:
            return "Invalid token %s." %token


    def select_account(self, amount):
        """
        Selects the account to use for a payment.

        Arguments:
            amount (float): The amount of the payment.

        Returns:
            str: The token corresponding to the account to use for the payment.
        """
        if self.accounts["token1"] >= amount:
            return "token1"
        elif self.accounts["token2"] >= amount:
            return "token2"
        else:
            return None

    def request_payment(self, order_number, amount):
        """
        Requests a payment of the given amount.

        Arguments:
            order_number (int): The order number of the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made.
        """
        token = self.select_account(amount)
        if token is None:
            return "Payment %d of %.2f failed due to insufficient balance in both accounts." % (order_number, amount)
        else:
            return self.make_payment(order_number, token, amount)


    def list_payments(self):
        """
        Lists all payments made in chronological order.

        Returns:
            str: A string representation of the list of payments made.
        """
        # payment_list = "\n".join([f"Order {p[0]}:
        # {p[2]} paid from {p[1]}" for p in self.payments])
        # payment_list = ""
        # for p in self.payments:
        #     payment_list += f"Order {p[0]}: {p[2]} paid from {p[1]}\n"
        payment_list = []
        for payment_move in self.payments:
            payment_list.append("Order %d: %.2f paid from %s" % (payment_move[0], payment_move[2], payment_move[1]))
        payment_list = "\n".join(payment_list)

        return "List of payments:\n%s" % payment_list

    def iterator(self):
        """
        Returns an iterator that iterates over the list
        of payments made in chronological order.

        Returns:
            iterator: An iterator that iterates over the list
            of payments made in chronological order.
        """
        return iter(sorted(self.payments, key=lambda x: x[0]))


class PaymentValidator(object):
    """
    A class to represent a payment validator in the chain of responsibility.

    Attributes:
        next_validator (PaymentValidator): The next validator in the chain of responsibility.
    """
    def __init__(self, next_validator=None):
        """
        Initializes the PaymentValidator class.

        Sets the next validator in the chain of responsibility.
        """
        self.next_validator = next_validator

    def validate(self, order_number, token, amount):
        """
        Validates a payment request.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made,
            or an error message if the payment request is invalid.
        """
        if self.next_validator is not None:
            return self.next_validator.validate(order_number, token, amount)
        else:
            return "Payment %d of %.2f failed due to an unknown error." % (order_number, amount)

class OrderNumberValidator(PaymentValidator):
    """
    A class to represent an order number validator in the chain of responsibility.
    """
    def validate(self, order_number, token, amount):
        """
        Validates a payment request.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made,
            or an error message if the payment request is invalid.
        """
        if order_number <= 0:
            return "Payment %d of %.2f failed due to an invalid order number." % (order_number, amount)
        else:
            return super(OrderNumberValidator, self).validate(order_number, token, amount)

class TokenValidator(PaymentValidator):
    """
    A class to represent a token validator in the chain of responsibility.
    """
    def validate(self, order_number, token, amount):
        """
        Validates a payment request.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made,
            or an error message if the payment request is invalid.
        """
        if token not in ["token1", "token2"]:
            return "Payment %d of %.2f failed due to an invalid token." % (order_number, amount)
        else:
            return super(TokenValidator, self).validate(order_number, token, amount)

class BalanceValidator(PaymentValidator):
    """
    A class to represent a balance validator in the chain of responsibility.
    """
    def validate(self, order_number, token, amount):
        """
        Validates a payment request.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made,
            or an error message if the payment request is invalid.
        """
        if amount > BANK_API.accounts[token]:
            return "Payment %d of %.2f failed due to insufficient balance in %s." % (order_number, amount, token)
        else:
            return super(BalanceValidator, self).validate(order_number, token, amount)

class PaymentProcessor(PaymentValidator):
    """
    A class to represent a payment processor in the chain of responsibility.
    """
    def validate(self, order_number, token, amount):
        """
        Validates a payment request.

        Arguments:
            order_number (int): The order number of the payment.
            token (str): The token corresponding to the account to use for the payment.
            amount (float): The amount of the payment.

        Returns:
            str: A message indicating the order number, token used, and amount of the payment made,
            or an error message if the payment request is invalid.
        """
        BANK_API.accounts[token] -= amount
        BANK_API.payments.append((order_number, token, amount))
        return "Payment %d of %.2f made from %s." % (order_number, amount, token)



if len(sys.argv) == 2 and sys.argv[1] == "-h":
    print "This program extracts the API access key to use the services of a bank."
    print "Usage: {executable path}/getJason.pyc {path JSON file}/{file name JSON}.json"
    print "Example: ./getJason.pyc ./sitedata.json"
    print "The access key can be retrieved from the standard output in the format:"
    print "{1.0}XXXX-XXXX-XXXX-XXXX"
else:
    # Parse the command-line arguments using argparse
    PARSER = argparse.ArgumentParser(description='Extract the API access key to use the services.')
    PARSER.add_argument('jsonfile', type=str, help='Path to the JSON file with the access key')
    PARSER.add_argument('jsonkey', type=str, help='Key to extract from the JSON file')
    ARGS = PARSER.parse_args()

    # Create an instance of the BankAPI class and retrieve the access key
    BANK_API = BankAPI()
    try:
        print BANK_API.get_access_key(ARGS.jsonfile, ARGS.jsonkey)

        # Make payments
        # print BANK_API.make_payment(1, "token1", 500)
        # print BANK_API.make_payment(2, "token2", 500)
        # print BANK_API.make_payment(3, "token1", 500)

        # # List payments
        # print BANK_API.list_payments()

        # # Request 8 payments of $500 each
        # for i in range(1, 8):
        #     result = BANK_API.request_payment(i, 500)
        #     print result

        # # Iterate over the list of payments made in chronological order
        # for payment_move in BANK_API.iterator():
        #     print payment_move


        # print "---------------------------------------------------------"

        # Create a chain of payment validators
        VALIDATOR = OrderNumberValidator(TokenValidator(BalanceValidator(PaymentProcessor())))

        # Request 8 payments of $500 each
        for i in range(1, 9):
            result = VALIDATOR.validate(i, BANK_API.select_account(500), 500)
            print result

        # Iterate over the list of payments made in chronological order
        for payment in BANK_API.iterator():
            print payment


    except IOError:
        print "The specified file was not found or cannot be opened."
    except KeyError:
        print "The specified key was not found in the JSON file."
    except IndexError:
        print "The specified index was not found or is invalid."
# okay decompiling getJason.pyc
