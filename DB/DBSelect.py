from DB import DBExecute
from DB import EventViewer
import pprint

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class DBSelect:
    """


    A class to create sql statements to Select tables.

    Attributes:
        db_name (str): The name of the database file.
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """

    def __init__(self, db_name):
        """
        Initializes a new DBInsert object.

        Args:
            db_name (str): The name of the database file.
        """
        self._EventViewerSource = "DBSelect"
        self.db = DBExecute.DBExecute(db_name)
        self.pprint_all_views()

    def _log_it(self, msg):
        """
         Log  Evemt
        :param msg:
        :return:
        """

        formatted_result_set = "{0}{1}".format("Result Set Found...\n\t", pprint.pformat(msg))
        EventViewer.EventViewer.log(self._EventViewerSource, "{}".format(formatted_result_set))

    def _fetch(self, query):
        result_set = self.db.fetch(query)
        self._log_it(str(result_set))
        return result_set

    def VIEW_CustomersAddress(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_CustomersAddress;"
        return self._fetch(query)

    def VIEW_GUICustomers(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_GUICustomers;"
        return self._fetch(query)

    def VIEW_GUIManufacturers(self):
        """"
        """
        query = " SELECT * FROM VIEW_GUIManufacturers;"
        return self._fetch(query)

    def VIEW_ManufacturersAddress(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_ManufacturersAddress;"
        return self._fetch(query)

    def VIEW_ManufacturersCatalogItems(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_ManufacturersCatalogItems;"
        return self._fetch(query)

    def VIEW_ManufacturersUser(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_ManufacturersUser;"
        return self._fetch(query)

    def VIEW_UserAdmins(self):
        """"
        """
        query = " SELECT * FROM VIEW_UserAdmins;"
        return self._fetch(query)

    def VIEW_UserCustomers(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_UserCustomers;"
        return self._fetch(query)

    def VIEW_UserEmployees(self):
        """

        :return:
        """
        query = " SELECT * FROM VIEW_UserEmployees;"
        return self._fetch(query)

    def VIEW_UserManufacturers(self):
        """"
        """
        query = " SELECT * FROM VIEW_UserManufacturers;"
        return self._fetch(query)

    def pprint_all_views(self):
        pprint.pprint(self.VIEW_UserEmployees())
        pprint.pprint(self.VIEW_CustomersAddress())
        pprint.pprint(self.VIEW_GUICustomers())
        pprint.pprint(self.VIEW_GUIManufacturers())
        pprint.pprint(self.VIEW_ManufacturersAddress())
        pprint.pprint(self.VIEW_ManufacturersCatalogItems())
        pprint.pprint(self.VIEW_ManufacturersUser())
        pprint.pprint(self.VIEW_UserAdmins())
        pprint.pprint(self.VIEW_UserCustomers())
        pprint.pprint(self.VIEW_UserEmployees())
        pprint.pprint(self.VIEW_UserManufacturers())
