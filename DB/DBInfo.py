import sqlite3

from DB import DBSelect
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


class DBInfo(DBSelect.DBSelect):
    """

    Omega Team

    A class to create sql statements to Select tables.

    Attributes:
        db_name (str): The name of the database file.
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """

    def __init__(self, db_name):
        super().__init__(db_name)
        """
        Initializes a new DBInfo object.

        Args:
            db_name (str): The name of the database file.
        """
        self._EventViewerSource = "DBInfo"
        self.db = DBExecute.DBExecute(db_name)


    def _log_it(self, msg):
        formatted_result_set = "{0}{1}".format( "Result Set Found...\n\t", pprint.pformat(msg))
        EventViewer.EventViewer.log(self._EventViewerSource, formatted_result_set )

    def print_all_table_headers(self, table_names: list):
        """
         Get All Table Headers
        :return:
        """
        # Loop through the table names and execute a query to get the table headers
        output= ''
        for table in table_names:
            output += "Table: {}\n\t Headers: ".format(table[0])
            output += " ".join(self.get_table_headers(table[0]))
            output += "\n"
            self._log_it(output)
        return output

    def get_table_headers(self, table_name):
        if type(table_name) is list():
            table_name = table_name[0]

        query = f"PRAGMA table_info({table_name})"
        headers = [row[1] for row in self.db.fetch_all(query)]
        output = headers
        self._log_it(output)
        return output

    def get_table_pk_headers_from_table(self, table_name):
        query = f"PRAGMA table_info({table_name})"
        result = self.db.fetch_all(query)
        pk_columns = [{'table_name': table_name, 'pk_header': row[1]} for row in result if row[5] == 1]
        return pk_columns

    def get_table_fk_headers_from_table(self, table_name: str):
        query = f"PRAGMA foreign_key_list('{table_name}')"
        result = self.db.fetch_all(query)
        # Fetch all the foreign key column names
        fk_columns = [{'foreign_table': row[2],'column_header':row[3]} for row in result]
        return fk_columns

    def get_fk_table_name(self, table :str, fk_name: dict):
        fk_headers = self.get_table_fk_headers_from_table(table)
        for item in fk_headers:
            if fk_name['column_header'] in item['column_header']:
                return item['foreign_table']
        return None


    def get_table_data_headers(self, table_name:str):
        query = f"PRAGMA table_info({table_name})"
        result = self.db.fetch_all(query)
        # Iterate over the rows and extract the column names that are not PK or FK
        column_names = []
        for row in result:
            column_name = row[1]
            is_pk = row[5]
            is_id = str(row[1]).endswith('ID')
            if not is_pk and not is_id:
                column_names.append(column_name)
        columns = [{'table': table_name, 'data_header': row} for row in column_names]
        return columns

    def get_table_id_all_cols_as_name(self, table_name: str):
        #table_pk_name = self.get_table_pk_headers_from_table(table_name)[0]['pk_header']
        query_part_headers = ''
        table_headers = self.get_table_headers(table_name)
        for header in table_headers:
            query_part_headers += f'''{header} || ', ' || '''

        query_part_headers = query_part_headers[:-11]

        query_part = f''' {query_part_headers} as name '''
        self._log_it(query_part)
        return query_part

    def get_table_names(self):
        query = "SELECT name FROM sqlite_master WHERE type='table';"
        table_names = self.db.fetch_all(query)
        self._log_it(table_names)
        return table_names







if __name__ == '__main__':
    app = DBInfo('./databases/test_db3.db')
    print(app.get_table_names())
    # print(app.get_all_table_headers(table_names=app.get_table_names()))
    print(app.get_table_fk_headers_from_table('Invoices'))
    # print(app.get_table_pk_headers_from_table('Invoices'))
    # print(app.get_table_data_headers('Invoices'))






