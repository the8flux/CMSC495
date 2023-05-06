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
    def __init__(self, db_name: str, table_name: str, **kwargs):
        super().__init__(db_name)
        self.target_row_id = kwargs.get('target_row_id', 0)
        self._tables = self.load_tables()
        self._table_object = QueryBuilder.TableInfo(db_name, table_name, target_row_id=self.target_row_id)
        self._form_select_tags = []
        self._form_input_tags = []
        #self._build_update_selection_div()
        self.build_input_tag()
        self.build_select_tags()

    def _build_update_selection_div(self):
        href_formatter = '''<ul><a href="/general_update?table_name={}&target_row_id={}">{}</a></ul>\n'''
        result_set = self.table_object.get_items_pk_headers()
        hrefs = ''
        for item in result_set:
            hrefs += href_formatter.format(self.table_object.table_name,item[0], item[1])

        html = HTMLElementFactory.DivTagScrolling("", hrefs).get_html()

        return html

    def get_update_selection_div(self):
        return self._build_update_selection_div()








    def build_select_tags(self, **kwargs):

        fk_table_headers = self.table_object.fk_headers
        fk_table_object_list = []
        for fk_table_header in fk_table_headers:
            for table in self._tables:
                if fk_table_header in table.pk_headers:
                    print(table)
                    fk_table_object_list.append(table)

            table: TableInfo
        for table in fk_table_object_list:
            selected_value = -1
            select_element_data: list
            select_element_data = table.get_items_pk_headers()
            label = HTMLElementFactory.LabelTag(f"{table.table_name}", f"{table.table_name}")
            self._form_select_tags.append(str(label))
            selected_value = self.table_object.record[table.pk_headers[0]]
            select_element = HTMLElementFactory.SelectTag(select_element_data,
                                                          selected=f"{selected_value}",
                                                          html_id=f"{table.table_name}",
                                                          html_name=f"{table.table_name}",
                                                          css_class=f"")
            self._form_select_tags.append(str(select_element))

    @property
    def table_object(self):
        return self._table_object

    def get_row_data_from_table(self):
        pass

    def build_select_tags(self, **kwargs):

        fk_table_headers = self.table_object.fk_headers
        fk_table_object_list = []
        for fk_table_header in fk_table_headers:
            for table in self._tables:
                if fk_table_header in table.pk_headers:
                    print(table)
                    fk_table_object_list.append(table)

            table: TableInfo
        for table in fk_table_object_list:
            selected_value = -1
            select_element_data: list
            select_element_data = table.get_items_pk_headers()
            label = HTMLElementFactory.LabelTag(f"{table.table_name}", f"{table.table_name}")
            self._form_select_tags.append(str(label))
            selected_value = self.table_object.record[table.pk_headers[0]]
            select_element = HTMLElementFactory.SelectTag(select_element_data,
                                                          selected=f"{selected_value}",
                                                          html_id=f"{table.table_name}",
                                                          html_name=f"{table.table_name}",
                                                          css_class=f"")
            self._form_select_tags.append(str(select_element))

    def build_input_tag(self):
        data_headers = self.table_object.data_headers

        for data_header in data_headers:
            label_tag = HTMLElementFactory.LabelTag(data_header, data_header)
            input_tag = HTMLElementFactory.InputTag("text", data_header, data_header, self.table_object.record[data_header])
            self._form_input_tags.append(str(label_tag))
            self._form_input_tags.append(str(input_tag))

    def get_html(self):
        # Create Form
        html = f'''{self._build_update_selection_div()}'''
        html = f'''<form action='/general_update' method='POST'>'''
        html += f'''<h3>ID # {self.table_object.record[self.table_object.pk_headers[0]]}<h3>'''
        html += f'''{' '.join(self._form_input_tags)}'''
        html += f'''{' '.join(self._form_select_tags)}'''
        html += f'''<input type="hidden" name="table_name" value="{self.table_object.table_name}"></input>'''
        html += f'''<input type="hidden" name="id_column" value="{self.table_object.pk_headers[0]}"></input>'''
        html += f'''<input type="hidden" name="id" value="{self.table_object.record[self.table_object.pk_headers[0]]}"></input>'''
        html += f'''<br><label for="delete">Delete Value:</label>'''
        html += f'''<input type="checkbox" name='ck_delete' value="delete">'''
        html += "<br><input type='submit' value='Submit'>"
        html += "</form>"
        html += f'''<p><a href="/">[ Home ]</a>'''
        html += f'''<a href="/general_update?table_name={self.table_object.table_name}&target_row_id={int(self.table_object.record[self.table_object.pk_headers[0]]) - 1}">[ Previous ]</a>'''
        html += f'''<a href="/general_update?table_name={self.table_object.table_name}&target_row_id={int(self.table_object.record[self.table_object.pk_headers[0]]) + 1}">[ Next ]</a></p>'''

        return html


    def __str__(self):
        # Create Form
        html = self.get_html()
        with open(f"update_page_for_{self.table_object.table_name}.html", "w") as f:
            f.write(html)
        return html


if __name__ == '__main__':
    app = UpdateForm('../DB/databases/test_db3.db', 'Users', target_row_id=10)
    print(app)


class AddForm(Form):
    def __init__(self, db_name: str, table_name: str, **kwargs):
        super().__init__(db_name)
        self.target_row_id = kwargs.get('target_row_id', 0)
        self._tables = self.load_tables()
        self._table_object = QueryBuilder.TableInfo(db_name, table_name, target_row_id=self.target_row_id)
        self._form_select_tags = []
        self._form_input_tags = []
        self.build_input_tag()
        self.build_select_tags()

    @property
    def table_object(self):
        return self._table_object

    def get_row_data_from_table(self):
        pass

    def build_select_tags(self, **kwargs):

        fk_table_headers = self.table_object.fk_headers
        fk_table_object_list = []
        for fk_table_header in fk_table_headers:
            for table in self._tables:
                if fk_table_header in table.pk_headers:
                    print(table)
                    fk_table_object_list.append(table)

            table: TableInfo
        for table in fk_table_object_list:
            selected_value = -1
            select_element_data: list
            select_element_data = table.get_items_pk_headers()
            label = HTMLElementFactory.LabelTag(f"{table.table_name}", f"{table.table_name}")
            self._form_select_tags.append(str(label))

            selected_value = self.table_object.record[table.pk_headers[0]]

            select_element = HTMLElementFactory.SelectTag(select_element_data,
                                                          html_id=f"{table.table_name}",
                                                          html_name=f"{table.table_name}",
                                                          css_class=f"")
            self._form_select_tags.append(str(select_element))

    def build_input_tag(self):
        data_headers = self.table_object.data_headers

        for data_header in data_headers:
            label_tag = HTMLElementFactory.LabelTag(data_header, data_header)
            input_tag = HTMLElementFactory.InputTag("text", data_header, data_header, "---")
            self._form_input_tags.append(str(label_tag))
            self._form_input_tags.append(str(input_tag))

    def get_html(self):
        # Create Form
        html = f'''<form action='/general_add' method='POST'>'''
        html += f'''<h3>New Item for {self.table_object.table_name}<h3>'''
        html += f'''{' '.join(self._form_input_tags)}'''
        html += f'''{' '.join(self._form_select_tags)}'''
        html += f'''<input type="hidden" name="table_name" value="{self.table_object.table_name}"></input>'''
        html += f'''<input type="hidden" name="id_column" value="{self.table_object.pk_headers[0]}"></input>'''
        html += f'''<input type="hidden" name="id" value="-1"></input>'''
        html += "<br><input type='submit' value='Submit'>"
        html += "</form>"
        html += f'''<p><a href="/">[ Back ]</a></p>'''
        return html


    def __str__(self):
        # Create Form
        html = self.get_html()
        with open(f"update_page_for_{self.table_object.table_name}.html", "w") as f:
            f.write(html)
        return html


if __name__ == '__main__':
    app = UpdateForm('../DB/databases/test_db3.db', 'Users', target_row_id=10)
    print(app)