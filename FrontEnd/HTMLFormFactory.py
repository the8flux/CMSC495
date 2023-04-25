from DB import DBSelect
from DB import DBExtract
from DB import DBInfo
from FrontEnd import HTMLElementFactory
from FrontEnd import QueryBuilder
from FrontEnd import CSSLoader
import pprint

from FrontEnd.QueryBuilder import TableInfo

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class Form:
    def __init__(self, db_name):
        self._db_name = db_name
        self.db_info = DBInfo.DBInfo(db_name)

    def peek(self):
        return vars(self)

    def load_tables(self):
        tables = []
        db_info = self.db_info
        table_names = db_info.get_table_names()

        for table in table_names:
            table_n = table[0]
            table_info_obj = QueryBuilder.TableInfo(self._db_name, table_n)
            tables.append(table_info_obj)
        return tables


class UpdateForm(Form):
    def __init__(self, db_name: str, table_name: str):
        super().__init__(db_name)
        self._tables = self.load_tables()

        self._table_object = QueryBuilder.TableInfo(db_name, table_name)
        self._form_select_elements = []
        self._form_text_box_elements = []

        self.create_select_elements()

    @property
    def table_object(self):
        return self._table_object

    def create_select_elements(self):
        fk_table_headers = self.table_object.fk_headers
        fk_table_object_list = []
        for fk_table_header in self.table_object.fk_headers:
            for table in self._tables:
                if fk_table_header in table.fk_headers:
                    fk_table_object_list.append(table)

        table: TableInfo
        for table in fk_table_object_list:
            select_element_data: list
            select_element_data = table.get_items_pk_headers()
            select_element = HTMLElementFactory.SelectTag(select_element_data, selected=-1)
            print(select_element)
            self._form_select_elements.append(select_element)

    def create_



    def create_form_update(self, table_name: str):
        # Getting Table Information

        # # Get Updated Item
        #
        # query = f'''SELECT {",".join(field_pk)}, {",".join(field_fk)}, {",".join(field_data)}
        #              FROM {table_name}
        #              WHERE {",".join(field_pk)} = {table_field_id}
        #          '''.replace("\n", "")
        # print(query)
        # result = self._extract.execute_query(query)
        # print(result)
        #
        # headers = list()
        # headers += field_pk
        # headers += field_fk
        # headers += field_data
        #
        # fields = dict()
        # index = 0
        # print(headers)
        # for column in headers:
        #     fields[column] = result[0][index]
        #     index += 1
        # print(fields)
        #
        # fk_html_select_elements = list()
        # for fk_item in field_fk_result:
        #     fk_table = self._extract.get_fk_table_name(table_name, fk_item)
        #
        #     print(fk_table + "<<<")
        #     fk_table_pk_header = self._extract.get_table_pk_headers_from_table(fk_table)
        #     tstruct = self._extract.get_table_id_name_header(fk_table)
        #
        #     selected = 1
        #     select_element = self.get_select_element(table=tstruct, selected=selected)
        #     fk_html_select_elements.append(select_element)

        # Create Form

        html = f"<form action='submit_{table_name}.py' method='POST'>"
        # html += f"{' '.join(fk_html_select_elements)}"
        html += "<input type='submit' value='Submit'>"
        html += "</form>"
        # with open(f"out-{table_name}.html", "w") as f:
        #     f.write(html)
        return html


if __name__ == '__main__':
    app = UpdateForm('../DB/databases/test_db3.db', 'Customers')
