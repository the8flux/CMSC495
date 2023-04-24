import sqlite3
from DB import EventViewer

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class DBExecute:
    """
    Omega Team

    A class to control a SQLite database.

    Attributes:
        db_name (str): The name of the database file.
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """

    def __init__(self, db_name):
        """
        Initializes a new DBExec object.

        Args:
            db_name (str): The name of the database file.
        """
        self.db_name = db_name
        self.connection = None
        self.cursor = None
        self._EventViewerSource = "DBExecute"

    def connect(self):
        """
        Connects to the database.
        """
        EventViewer.EventViewer.log(self._EventViewerSource, "Connecting to Database...")
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        EventViewer.EventViewer.log(self._EventViewerSource,
                                    "Connected... Connected={}".format(self.connection.cursor()))

    def disconnect(self):
        """
        Disconnects from the database.
        """
        EventViewer.EventViewer.log(self._EventViewerSource, "Disconnecting Database...")
        if self.connection:
            self.connection.close()
            self.connection = None
            self.cursor = None

    def execute(self, query):
        """
        Executes a SQL query on the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute in the query.

        Raises:
            Exception: If there was an error executing the query.
        """
        EventViewer.EventViewer.log(self._EventViewerSource,
                                    "Attempting to execute query:\n{} \nparams:{} ...".format(query, params))
        try:
            self.connect()
            self.cursor.execute(query)
            self.connection.commit()
        except Exception as e:
            print("Error executing query:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "Error executing query:\n{} \nparams:{} ...".format(query, params))
        finally:
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}".format("Disconnecting..."))
            self.disconnect()

    def fetch(self, query):
        """
        Fetches data from the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute in the query.

        Returns:
            list: A list of tuples representing the data fetched from the database.

        Raises:
            Exception: If there was an error fetching the data.
        """

        result = None
        try:
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "Attempting to execute query:\n\t{} \n\tparams:{} ...".format(query))
            self.connect()
            print(query)
            self.cursor.fetch(query)
            result = self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}\n\t".format("Fetching Error..."), e)
        finally:

            self.disconnect()
        return result

    def fetch_all(self, query, *params):
        """
        Fetches data from the database.

        Args:
            query (str): The SQL query to execute.
            params (tuple): The parameters to substitute in the query.

        Returns:
            list: A list of tuples representing the data fetched from the database.

        Raises:
            Exception: If there was an error fetching the data.
        """

        result = None
        try:
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "Attempting to execute query:\n\t{} \n\tparams:{} ...".format(query, params))
            self.connect()
            #print(query)
            self.cursor.execute(query)
            result = self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}\n\t".format("Fetching Error..."), e)
        finally:

            self.disconnect()
        return result






