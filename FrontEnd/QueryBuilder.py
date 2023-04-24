from DB import DBSelect
from DB import DBExtract


"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""

class TableInfo:
    def __init__(self, db_name: str, table_name: str):
        self._extract = DBExtract.DBExtract(db_name)
        self._select = DBSelect.DBSelect(db_name)
        self._table_name = table_name
        self._table_pk_headers = self._extract.get_table_pk_headers_from_table(table_name)
        self._table_fk_headers = self._extract.get_table_fk_headers_from_table(table_name)
        self._table_data_headers = self._extract.get_table_data_headers(table_name)
        self._table_concat_all_rows_query_part = self._extract.get_table_id_all_cols_as_name(table_name)

    @property
    def table_name(self):
        return self._table_name

    @property
    def pk_headers(self):
        return ["".join(item['pk_header']) for item in self._table_pk_headers]

    @property
    def fk_headers(self):
        return ["".join(item['column_header']) for item in self._table_fk_headers]

    @property
    def data_headers(self):
        return ["".join(item['data_header']) for item in self._table_data_headers]

    @property
    def all_headers(self):
        return self._table_pk_headers + self._table_fk_headers + self._table_fk_headers

    def get_from_table_records_id_name_header(self):
        return_result = []
        table_name = self.table_name
        pk_header = self.pk_headers[0]
        name_field = self.fk_headers

        for col in self._table_data_headers:
            if 'Name' in col['data_header'] or 'Title' in col['data_header']:
                return_result.append({'table_name': table_name,
                                      'id_field': pk_header,
                                      'name_field': col['data_header']})
            else:
                name_field = self.get_table_id_all_cols_as_name(table_name)
                return_result.append({'table_name': table_name,
                                      'id_field': pk_header,
                                      'name_field': name_field})
                # print(return_result)
        return return_result

    def get_table_id_all_cols_as_name(self, table_name):
        query_part_headers = ''
        table_headers = self.all_headers
        for header in table_headers:
            query_part_headers += f'''{header} || ', ' || '''

        query_part_headers = query_part_headers[:-11]

        query_part = f''' {query_part_headers} as name '''
        #self._log_it(query_part)
        return query_part

    def _switch(self, table_name):
        if table_name == None:
            return ""
        # elif table == "VIEW_GUIManufacturers":
        #     return super().VIEW_GUIManufacturers()
        # elif table == "VIEW_GUICustomers":
        #     return super().VIEW_GUICustomers()
        elif type(table_name) is dict():
            query_part = self._extract.get_table_id_name_header(table_name['table_name'])
            query = '''SELECT {} FROM {}'''.format(table_name['name_field'], table_name['table_name'])
        else:
            query_part = self._extract.get_table_id_name_header(table_name)
            query = '''SELECT {} FROM {}'''.format(query_part['name_field'], query_part['table_name'])

    # def _table_data_headers(self):
    #     pass




if __name__ == '__main__':
    app = TableInfo('../DB/databases/test_db3.db', 'Invoices')
    print(app.pk_headers)
    print(app.fk_headers)
    print(app.data_headers)
    print(app.get_from_table_records_id_name_header())
