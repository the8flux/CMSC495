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
        for key, value in list_f_tuples_key_value:
            options += '''\n<option value="{}">{}</option>'''.format(key, value)
        return_value = " ".join([label_element, select_start, options, select_stop])
        return return_value

    @staticmethod
    def _create_text_box(list_f_tuples_key_value, **kwargs):
        pass

    def _switch(self, table):
        if table == None:
            return ""
        elif table == "VIEW_GUIManufacturers":
            return super().VIEW_GUIManufacturers()
        elif table == "VIEW_GUICustomers":
            return super().VIEW_GUICustomers()

    def get_select_element(self, **kwargs):
        table = kwargs.get('table', None)
        has_label = kwargs.get('has_label', 'False')
        label_prompt = kwargs.get('label_prompt', '---')
        css_class = kwargs.get('css_class', '')
        html_id = kwargs.get('html_id', '')
        html_name = kwargs.get('html_name', '')
        result_set = self._switch(table)
        return_value = self._create_select(result_set, has_label=has_label, label_prompt=label_prompt, css_class=css_class,
                                           html_name=html_name, html_id=html_id)
        return return_value

    def get_textbox_element(self, **kwargs):
        table = kwargs.get('table', None)
        css_class = kwargs.get('css_class', '')
        html_id = kwargs.get('html_id', '')
        html_name = kwargs.get('html_name', '')
        pass
