from DB.DBSelect import DBSelect
from Middleware.User import User
from Middleware.Manufacturer import Manufacturer
from Middleware.Customer import Customer


class Users:
    """
    A class to retrieve different types of users from the database.

    Attributes:
        _db (str): The name or full path of the database file.
    """

    def __init__(self, db_name):
        self._db = DBSelect(db_name)

    def admins(self):
        return [User(*admin) for admin in self._db.VIEW_UserAdmins()]

    def employees(self):
        return [User(*employee) for employee in self._db.VIEW_UserEmployees()]

    def manufacturers(self):
        return [Manufacturer(*manufacturer) for manufacturer in self._db.VIEW_UserManufacturers()]

    def customers(self):
        return [Customer(*customer) for customer in self._db.VIEW_UserCustomers()]
