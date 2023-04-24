import sqlite3
from DB import DBInfo
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


class DBExtract(DBInfo.DBInfo):
    def __init__(self, db_name):
        super().__init__(db_name)

    def get_table_id_names_headers(self):
        return_result = []
        table_names = super().get_table_names()
        for table_name in table_names:
            table_id_header = super().get_table_pk_headers_from_table(table_name[0])[0]
            header_columns = super().get_table_data_headers(table_name[0])
            for col in header_columns:
                if 'Name' in col['data_header'] or 'Title' in col['data_header']:
                    return_result.append({'table_name': table_name[0],
                                          'id_field': table_id_header['pk_header'],
                                          'name_field': col['data_header']})
                else:
                    name_field = self.get_table_id_all_cols_as_name(table_name[0])
                    return_result.append({'table_name': table_name[0],
                                          'id_field': table_id_header['pk_header'],
                                          'name_field': name_field})
                    #print(return_result)
        return return_result


    def get_table_id_name_header(self, table_name):
        id_name_list = self.get_table_id_names_headers()
        for row_dict in id_name_list:
            if table_name == row_dict['table_name']:
                if 'Users' in row_dict['table_name']:
                    row_dict =  {'table_name': 'Users', 'id_field': 'UserID', 'name_field': 'FirstName, LastName'}
                return row_dict
        return {'table_name': '', 'id_field': '', 'name_field': ''}

    def create_query_from_dict(self, instance_dict):
        query = f'''SELECT {instance_dict['id_field']}, {instance_dict['name_field']} FROM {instance_dict['table_name']} '''
        #query += f'''ORDER BY {instance_dict['name_field']} ASC '''
        return query


    def execute_query(self,query):
        return self.db.fetch_all(query)


if __name__ == '__main__':
    app = DBExtract('./databases/test_db3.db')
    #print(app.get_table_id_names_headers())
    print(app.get_table_id_name_header('Users'))
    print(app.get_table_id_name_header('Customers'))
    print(app.get_table_id_name_header('Address'))
    #print(app.create_query_from_dict(app.get_table_id_name_header('Customers')))
    #print(app.create_query_from_dict(app.get_table_id_name_header('Users')))

    print(app.execute_query(
         app.create_query_from_dict(app.get_table_id_name_header('Customers')
             )))
    #
    # print(app.execute_query(
    #     app.create_query_from_dict(app.get_table_id_name_header('Users')
    #         )))
    print(app.execute_query(
         app.create_query_from_dict(app.get_table_id_name_header('Address')
             )))

    # print(app.get_all_table_headers(table_names=app.get_table_names()))
    # print(app.get_table_fk_headers_from_table('Invoices'))
    # print(app.get_table_pk_headers_from_table('Invoices'))
    # print(app.get_table_data_headers('Invoices'))



    #
    #
    # def get_field_names(self, table_name):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute(f"SELECT * FROM {table_name}")
    #     field_names = [description[0] for description in cursor.description]
    #     return field_names
    #
    # def get_table_name_by_field(self, field_name):
    #     # Get list of table names in the database
    #     self.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #     table_names = [row[0] for row in self.cursor.fetchall()]
    #     # Iterate over table names
    #     for table_name in table_names:
    #         # Check if table has an ID field
    #         self.execute(f"PRAGMA table_info({table_name})")
    #         columns = [row[1] for row in self.cursor.fetchall()]
    #         if 'ID' in columns:
    #             # Check if ID value exists in the table
    #             self.cursor.execute(f"SELECT ID FROM {table_name} WHERE ID=?", (field_name,))
    #             result = self.cursor.fetchone()
    #             if result:
    #                 # Return table name if ID value exists
    #                 return table_name
    #     # Return None if no matching table is found
    #     return None
    #
    # def get_tables_with_column(self, column_name):
    #
    #     # Get list of table names in the database
    #     self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #     table_names = [row[0] for row in self.cursor.fetchall()]
    #     # Iterate over table names
    #     tables_with_column = []
    #     for table_name in table_names:
    #         # Check if table has the specified column
    #         self.cursor.execute(f"PRAGMA table_info({table_name})")
    #         columns = [row[1] for row in self.cursor.fetchall()]
    #         if column_name in columns:
    #             # Add table name to list if it has the column
    #             tables_with_column.append(table_name)
    #     return tables_with_column
    #
    # def get_foreign_table(self, table_name, column_name):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    #     foreign_keys = cursor.fetchall()
    #     # Iterate over foreign key information
    #     for foreign_key in foreign_keys:
    #         if foreign_key[3] == column_name:
    #             # Return name of referenced table
    #             return_value = foreign_key[2]
    #             return return_value
    #     # Return None if no foreign key is found
    #     return None
    #
    #
    #
    #
    # def get_field_names(self, table_name):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute(f"SELECT * FROM {table_name}")
    #     field_names = [description[0] for description in cursor.description]
    #     return field_names
    #
    # def get_table_name_by_field(self, field_name):
    #     # Get list of table names in the database
    #     self.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #     table_names = [row[0] for row in self.cursor.fetchall()]
    #     # Iterate over table names
    #     for table_name in table_names:
    #         # Check if table has an ID field
    #         self.execute(f"PRAGMA table_info({table_name})")
    #         columns = [row[1] for row in self.cursor.fetchall()]
    #         if 'ID' in columns:
    #             # Check if ID value exists in the table
    #             self.cursor.execute(f"SELECT ID FROM {table_name} WHERE ID=?", (field_name,))
    #             result = self.cursor.fetchone()
    #             if result:
    #                 # Return table name if ID value exists
    #                 return table_name
    #     # Return None if no matching table is found
    #     return None
    #
    # def get_tables_with_column(self, column_name):
    #
    #     # Get list of table names in the database
    #     self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    #     table_names = [row[0] for row in self.cursor.fetchall()]
    #     # Iterate over table names
    #     tables_with_column = []
    #     for table_name in table_names:
    #         # Check if table has the specified column
    #         self.cursor.execute(f"PRAGMA table_info({table_name})")
    #         columns = [row[1] for row in self.cursor.fetchall()]
    #         if column_name in columns:
    #             # Add table name to list if it has the column
    #             tables_with_column.append(table_name)
    #     return tables_with_column
    #
    # def get_foreign_table(self, table_name, column_name):
    #     conn = sqlite3.connect(self.db_name)
    #     cursor = conn.cursor()
    #     cursor.execute(f"PRAGMA foreign_key_list({table_name})")
    #     foreign_keys = cursor.fetchall()
    #     # Iterate over foreign key information
    #     for foreign_key in foreign_keys:
    #         if foreign_key[3] == column_name:
    #             # Return name of referenced table
    #             return_value = foreign_key[2]
    #             return return_value
    #     # Return None if no foreign key is found
    #     return None