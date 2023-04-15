from DB import DBSelect
from collections import namedtuple


class Customers:
    """
    A class to retrieve customers from the database in a list of namedtuple customer objects.

    Attributes:
        _db (str): The name or full path of the database file.
    """
    def __init__(self, db_name):
        self._db = DBSelect.DBSelect(db_name)
        self._customer = namedtuple("Customer", "user_id, first_name, last_name, email, phone, user_logon, "
                                                "description, customer_name")

    def all_customers(self):
        return [self._customer(*customer) for customer in self._db.VIEW_UserCustomers()]

"""
for customer in Customers("C:\\Users\\rbr4n\\PycharmProjects\\CMSC495\\DB\\databases\\test_db3.db").all_customers():
    print(customer)
"""
