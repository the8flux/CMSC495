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

    def execute(self, query, *params):
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
            self.cursor.execute(query, params)
            self.connection.commit()
        except Exception as e:
            print("Error executing query:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "Error executing query:\n{} \nparams:{} ...".format(query, params))
        finally:
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}".format("Disconnecting..."))
            self.disconnect()

    def fetch(self, query, *params):
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
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}\n\t".format("Fetching Error..."), e)
        finally:

            self.disconnect()
        return result

    def fetch_all(self):
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
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
        except Exception as e:
            print("Error fetching data:", e)
            EventViewer.EventViewer.log(self._EventViewerSource,
                                        "{}\n\t".format("Fetching Error..."), e)
        finally:

            self.disconnect()
        return result

    def get_field_names(self, table_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        field_names = [description[0] for description in cursor.description]
        return field_names

    def get_table_name_by_field(self, field_name):
        # Get list of table names in the database
        self.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in self.cursor.fetchall()]
        # Iterate over table names
        for table_name in table_names:
            # Check if table has an ID field
            self.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in self.cursor.fetchall()]
            if 'ID' in columns:
                # Check if ID value exists in the table
                self.cursor.execute(f"SELECT ID FROM {table_name} WHERE ID=?", (field_name,))
                result = self.cursor.fetchone()
                if result:
                    # Return table name if ID value exists
                    return table_name
        # Return None if no matching table is found
        return None

    def get_tables_with_column(self, column_name):

        # Get list of table names in the database
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in self.cursor.fetchall()]
        # Iterate over table names
        tables_with_column = []
        for table_name in table_names:
            # Check if table has the specified column
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in self.cursor.fetchall()]
            if column_name in columns:
                # Add table name to list if it has the column
                tables_with_column.append(table_name)
        return tables_with_column

    def get_foreign_table(self, table_name, column_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA foreign_key_list({table_name})")
        foreign_keys = cursor.fetchall()
        # Iterate over foreign key information
        for foreign_key in foreign_keys:
            if foreign_key[3] == column_name:
                # Return name of referenced table
                return_value = foreign_key[2]
                return return_value
        # Return None if no foreign key is found
        return None




    def get_field_names(self, table_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table_name}")
        field_names = [description[0] for description in cursor.description]
        return field_names

    def get_table_name_by_field(self, field_name):
        # Get list of table names in the database
        self.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in self.cursor.fetchall()]
        # Iterate over table names
        for table_name in table_names:
            # Check if table has an ID field
            self.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in self.cursor.fetchall()]
            if 'ID' in columns:
                # Check if ID value exists in the table
                self.cursor.execute(f"SELECT ID FROM {table_name} WHERE ID=?", (field_name,))
                result = self.cursor.fetchone()
                if result:
                    # Return table name if ID value exists
                    return table_name
        # Return None if no matching table is found
        return None

    def get_tables_with_column(self, column_name):

        # Get list of table names in the database
        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        table_names = [row[0] for row in self.cursor.fetchall()]
        # Iterate over table names
        tables_with_column = []
        for table_name in table_names:
            # Check if table has the specified column
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            columns = [row[1] for row in self.cursor.fetchall()]
            if column_name in columns:
                # Add table name to list if it has the column
                tables_with_column.append(table_name)
        return tables_with_column

    def get_foreign_table(self, table_name, column_name):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(f"PRAGMA foreign_key_list({table_name})")
        foreign_keys = cursor.fetchall()
        # Iterate over foreign key information
        for foreign_key in foreign_keys:
            if foreign_key[3] == column_name:
                # Return name of referenced table
                return_value = foreign_key[2]
                return return_value
        # Return None if no foreign key is found
        return None



