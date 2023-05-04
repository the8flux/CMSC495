from DB import DBSelect
from DB import DBExtract
from FrontEnd_old import HTMLFormFactory
from FrontEnd_old import HTMLElementFactory



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
        self._extract = DBExtract.DBExtract('../DB/databases/test_db3.db')







        return super().get_table(query)



