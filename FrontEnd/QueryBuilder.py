from DB import DBSelect
from DB import DBExtract
from pprint import pprint

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class QueryBuilder:
    def __init__(self, db_name: str):
        self.extract = DBExtract.DBExtract(db_name)
        self.select = DBSelect.DBSelect(db_name)


class TableInfo(QueryBuilder):
    depth = 0

    def __init__(self, db_name: str, table_name: str, **kwargs):
        if not db_name:
            db_name = "../DB/databases/test_db3.db"
        super().__init__(db_name)


        self._extract = self.extract
        self._select = self.select
        self._table_name = table_name
        self._table_pk_headers = self._extract.get_table_pk_headers_from_table(table_name)
        self._table_fk_headers = self._extract.get_table_fk_headers_from_table(table_name)
        self._table_data_headers = self._extract.get_table_data_headers(table_name)
        self._table_concat_all_rows_query_part = self._extract.get_table_id_all_cols_as_name(table_name)

        target_row_id = kwargs.get('target_row_id', None)
        if target_row_id:
            self._record = self.get_row(target_row_id)
        else:
            self._record = None



    @property
    def record(self) -> dict:
        return self._record

    def get_record(self) -> dict:
        return self._record

    @property
    def table_name(self) -> str:
        return self._table_name

    @property
    def pk_headers(self) -> list:
        return ["".join(item['pk_header']) for item in self._table_pk_headers]

    @property
    def fk_headers(self) -> list:
        return ["".join(item['column_header']) for item in self._table_fk_headers]

    @property
    def data_headers(self) -> list:
        return ["".join(item['data_header']) for item in self._table_data_headers]

    @property
    def all_headers(self) -> list:
        return_value = []
        header_list = [self.pk_headers, self.fk_headers, self.data_headers]
        for headers in header_list:
            for item in headers:
                return_value.append(item)
        return return_value

    def get_row(self, row_id_pk: int) -> dict:
        return_value = dict()
        if isinstance(row_id_pk, int):
            row_id_pk = int(row_id_pk)
        else:
            return ""

        query = f'''SELECT {",".join(self.all_headers)}'''
        query += f''' FROM {self.table_name}'''
        query += f''' WHERE {self.pk_headers[0]} = {row_id_pk}'''
        print(query)

        result_row = self.extract.execute_query(query)
        print(result_row)


        for row in result_row:
            col = 0
            for header in self.all_headers:
                return_value[header] = row[col]
                col += 1

        return return_value

    def get_rows(self) -> list:
        return_value = list()
        record = dict()


        query = f'''SELECT {",".join(self.all_headers)}'''
        query += f''' FROM {self.table_name}'''
        #query += f''' WHERE {self.pk_headers[0]} = {row_id_pk}'''
        #print(query)

        result_row = self.extract.execute_query(query)
        #print(result_row)

        for row in result_row:
            col = 0
            record = dict()
            for header in self.all_headers:
                record[header] = row[col]
                col += 1
            return_value.append(record)
        return return_value




    def _get_table_id_all_cols_as_name(self):
        query_part_headers = ''
        table_headers = self.all_headers
        #table_headers = self.data_headers
        for header in table_headers:
            query_part_headers += f'''{header} || '|' || '''

        query_part_headers = query_part_headers[:-10]

        query_part = f''' {query_part_headers} as name '''
        # self._log_it(query_part)
        return query_part

    def _get_query_select_pk__headers_as_name(self):
        table_name = self.table_name
        table_id = self.pk_headers[0]
        headers = self._get_table_id_all_cols_as_name()
        query = f'''SELECT {table_id}, {headers} FROM {table_name} ORDER BY name'''
        return query

    def get_items_pk_headers(self) -> list:
        return_result = self.extract.execute_query(self._get_query_select_pk__headers_as_name())
        return return_result

    def get_items_data_headers(self) -> list:
        return_value = list()
        row_item = dict()
        query = f'''SELECT {",".join(self.data_headers)} FROM {self.table_name}'''
        result_set = self.extract.execute_query(query)

        for row in result_set:
            col = 0
            for header in self.data_headers:
                row_item[header] = row[col]
                col += 1
            return_value.append(row_item)
        return return_value

    def __str___(self):
        return self.__dir__()

# #################### TESTING Module #######################################################################
# if __name__ == '__main__':
#     app = TableInfo('../DB/databases/test_db3.db', 'Users', target_row_id=10)
#     print(app.record)

