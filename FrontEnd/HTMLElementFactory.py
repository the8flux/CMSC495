"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class LabelTag:
    '''
        Creates a HTML Label Tag Object
    '''

    def __init__(self, label_for: str, label_text: str):
        '''

        :param label_for:
        :param label_text:
        '''
        self.object_result_string = LabelTag._create_label(label_for, label_text)

    @staticmethod
    def _create_label(label_for: str, label_text: str):
        '''
            Returns a Label; Element string
        :param label_for:
        :param label_text:
        :return:
        '''
        return "<label for={}>{}:</label><br>\n".format(label_for, label_text)

    def __str__(self):
        '''
         Returns Label Element HTML string from object
        :return:
        '''
        return self.object_result_string


class InputTag:
    def __init__(self, input_type: str, input_id: str, input_name: str, input_text: str):
        '''

        :param label_for:
        :param label_text:
        '''
        self.object_result_string = InputTag._create_input(input_type, input_id, input_name, input_text)

    @staticmethod
    def _create_input(input_type: str, input_id: str, input_name: str, input_text: str):
        '''
            Returns a Label; Element string
        :param label_for:
        :param input_text:
        :return:
        '''
        return f'''<input type={input_type} id="{input_id}" name="{input_name}" value="{input_text}"></input><br>''' + "\n"

    def __str__(self):
        '''
         Returns Label Element HTML string from object
        :return:
        '''
        return self.object_result_string




class SelectTag:
    '''
        Creates a HTML Select Element Object
    '''
    select_start_tag = '''<select class="{}" name="{}" id="{}">\n'''
    select_stop_tag = '''</select><br><br>'''

    def __init__(self, key_value_tuple_list: list, **kwargs):
        '''

        :param key_value_tuple_list:
        :param kwargs:
        '''
        self.selected = kwargs.get('selected', -1)

        self.key_value_tuple_list = key_value_tuple_list
        if not isinstance(self.selected, int):
            self.selected = int(self.selected)
        self.css_class = kwargs.get('css_class', "")
        self.html_name = kwargs.get('html_name', "")
        self.html_id = kwargs.get('html_id', "")
        self.object_result_string = self._build_select_element()

    def _build_select_element(self):
        '''

        :return:
        '''
        return_result = SelectTag.select_start_tag.format(self.css_class, self.html_name, self.html_id)

        for tuple_item in self.key_value_tuple_list:
            return_result += SelectTag._build_options(tuple_item, self.selected)

        return_result += SelectTag.select_stop_tag
        return return_result

    @staticmethod
    def _build_options(tuple_key_value: tuple, selected: int):
        '''

        :param tuple_key_value:
        :param selected:
        :return:
        '''
        return SelectTag._create_option(tuple_key_value[0], tuple_key_value[1], selected)

    @staticmethod
    def _create_option(key: str, value: str, selected: int):
        '''

        :param key:
        :param value:
        :param selected:
        :return:
        '''
        selected_str = ''
        if selected == key:
            selected_str = "selected"
        return '''\n<option value="{}" {}>{}</option>'''.format(key, selected_str, value)

    def __str__(self):
        '''
         Returns HTML Select Element String
        :return:
        '''
        return self.object_result_string
