from DB import DBSelect


class GUIControlData(DBSelect.DBSelect):
    """
    A static class with static methods to provide read only data to GUI Controls

    Attributes:
        db_name (str): The name of the database file.
        connection (sqlite3.Connection): The database connection object.
        cursor (sqlite3.Cursor): The database cursor object.
    """

    def __init__(self):
        super().__init__('../DB/databases/test_db3.db')

    @staticmethod
    def _create_select(list_f_tuples_key_value, **kwargs):
        selected = kwargs.get('selected', '')
        has_label = kwargs.get('has_label', 'False')
        label_prompt = kwargs.get('label_prompt', '---')
        css_class = kwargs.get('css_class', "")
        html_name = kwargs.get('html_name', "")
        html_id = kwargs.get('id', "")
        label_element = ''
        if has_label != 'False':
            label_element = "<label for={}>{}:</label><br>\n".format(html_name, label_prompt)

        select_start = '''<select class="{}" name="{}" id="{}">\n'''.format(css_class, html_name, html_id)
        select_stop = "</select>\n"
        options = ""
        html_selected_attribute = ''
        for key, value in list_f_tuples_key_value:
            if str(selected) == str(key):
                html_selected_attribute = 'selected'
            options += '''\n<option value="{}" {}>{}</option>'''.format(key, html_selected_attribute, value)
            html_selected_attribute = ''

        return_value = " ".join([label_element, select_start, options, select_stop])
        return return_value

    @staticmethod
    def _create_text_box(list_f_tuples_key_value, **kwargs):
        has_label = kwargs.get('has_label', 'False')
        label_prompt = kwargs.get('label_prompt', '---')
        css_class = kwargs.get('css_class', "")
        html_name = kwargs.get('html_name', "")
        html_id = kwargs.get('id', "")
        label_element = ''
        if has_label != 'False':
            label_element = "<label for={}>{}:</label><br>\n".format(html_name, label_prompt)

        input_element = '''<input type="text" id="{}" name="{}">{}<br>'''.format(html_id, html_name, html_name)

        return_value = "{}{}".format(label_element, input_element)

        return return_value



    def _switch(self, table):
        if table == None:
            return ""
        # elif table == "VIEW_GUIManufacturers":
        #     return super().VIEW_GUIManufacturers()
        # elif table == "VIEW_GUICustomers":
        #     return super().VIEW_GUICustomers()
        else:
            query = '''SELECT * FROM {}'''.format(table)
            return super().get_table(query)

    def get_select_element(self, **kwargs):
        table = kwargs.get('table', None)
        has_label = kwargs.get('has_label', 'False')
        label_prompt = kwargs.get('label_prompt', '---')
        css_class = kwargs.get('css_class', '')
        html_id = kwargs.get('html_id', '')
        html_name = kwargs.get('html_name', '')
        selected = kwargs.get('selected', '')
        result_set = self._switch(table)
        return_value = self._create_select(result_set, has_label=has_label, label_prompt=label_prompt, css_class=css_class,
                                           html_name=html_name, html_id=html_id, selected=selected)
        return return_value

    def get_textbox_element(self, **kwargs):
        table = kwargs.get('table', None)
        css_class = kwargs.get('css_class', '')
        html_id = kwargs.get('html_id', '')
        html_name = kwargs.get('html_name', '')
        pass


    def get_form_element(self, **kwargs):
        table = kwargs.get('table', None)
        has_label = kwargs.get('has_label', 'False')
        label_prompt = kwargs.get('label_prompt', '---')
        css_class = kwargs.get('css_class', '')
        html_id = kwargs.get('html_id', '')
        html_name = kwargs.get('html_name', '')
        html_class = kwargs.get('html_class', '')
        start_html = '''<div class={}>'''.format(html_class)

        pass


    # Define function to create HTML form based on field names
    def create_form_update(self, table_name, table_field_name, table_field_id):
        field_names = self.db.get_field_names(table_name)
        build_query = '''SELECT '''
        for field_name in field_names:
            build_query += "{}, ".format(field_name)
        build_query = build_query[:-2] # get rid of last comma

        build_query += ''' FROM {} '''.format(table_name)
        build_query += ''' WHERE {} = {};'''.format(table_field_name, table_field_id)

        #self.db.execute(build_query)
        result = self.db.fetch(build_query)
        print(result)

        html = f"<form action='submit_{table_name}.py' method='POST'>"
        for field_name in field_names:
            if str(field_name).endswith('ID'):
                table_fk = self.db.get_foreign_table(table_name, field_name)
                sub_query = "SELECT {}  FROM {} WHERE {} = {}".format(field_name,table_fk, table_field_id, table_field_id)

                html += self.get_select_element(table=table_fk, selected=)
            else:
                html += "<p> future textbox for {}".format(field_name)

        html += "<input type='submit' value='Submit'>"
        html += "</form>"
        # with open(f"out-{table_name}.html", "w") as f:
        #     f.write(html)
        return html


