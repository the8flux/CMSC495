import sqlite3
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


class DBInfo:
    """

    Omega Team

    A class to create sql statements to Select tables.

    Attributes:
        db_name (str): The name of the database file.
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """

    def __init__(self, db_name):
        """
        Initializes a new DBInfo object.

        Args:
            db_name (str): The name of the database file.
        """
        self._EventViewerSource = "DBInfo"
        self.db = DBExecute.DBExecute(db_name)
        self.get_all_table_headers()

    def _log_it(self, msg):
        formatted_result_set = "{0}{1}".format( "Result Set Found...\n\t", pprint.pformat(msg))
        EventViewer.EventViewer.log(self._EventViewerSource, formatted_result_set )

    def get_all_table_headers(self):
        """
         Get All Table Headers
        :return:
        """
        # Define the table names
        table_names = ['ItemCategories', 'PriceAdjustment', 'UserType', 'CatalogItems', 'InventoryItems', 'Address',
                       'Manufacturers', 'Customers', 'Users', 'LineItems', 'Invoices']

        # Loop through the table names and execute a query to get the table headers
        for table in table_names:
            query = f"PRAGMA table_info({table})"
            headers = [row[1] for row in self.db.fetch(query)]
            output = f"{table} headers: {headers}"
            self._log_it(output)
