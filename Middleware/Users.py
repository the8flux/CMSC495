from DB import DBSelect
from collections import namedtuple


class Users:
    """
    A class to retrieve users from the database in a list of namedtuple user objects.

    Attributes:
        _db (str): The name or full path of the database file.
    """
    def __init__(self, db_name):
        self._db = DBSelect.DBSelect(db_name)
        self._user = namedtuple("User", "user_id, first_name, last_name, email, phone, user_logon, description")

    def _admins(self):
        return [self._user(*admin) for admin in self._db.VIEW_UserAdmins()]

    def _employees(self):
        return [self._user(*employee) for employee in self._db.VIEW_UserEmployees()]

    def all_users(self):
        return self._admins() + self._employees()

"""
for user in Users("C:\\Users\\rbr4n\\PycharmProjects\\CMSC495\\DB\\databases\\test_db3.db").all_users():
    print(user)
"""