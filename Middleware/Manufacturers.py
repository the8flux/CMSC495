from DB import DBSelect
from collections import namedtuple


class Manufacturers:
    """
    A class to retrieve manufacturers from the database in a list of namedtuple manufacturer objects.

    Attributes:
        _db (str): The name or full path of the database file.
    """
    def __init__(self, db_name):
        self._db = DBSelect.DBSelect(db_name)
        self._manufacturer = namedtuple("Manufacturer", "user_id, first_name, last_name, email, phone, user_logon, "
                                                        "description, manufacturer_name")

    def all_manufacturers(self):
        return [self._manufacturer(*manufacturer) for manufacturer in self._db.VIEW_UserManufacturers()]

"""
for manufacturer in Manufacturers("C:\\Users\\rbr4n\\PycharmProjects\\CMSC495\\DB\\databases\\test_db3.db").all_manufacturers():
    print(manufacturer)
"""
