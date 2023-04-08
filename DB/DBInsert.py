from DB import DBExecute

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""
class DBInsert:
    """


    """

    def __init__(self, db_name):
        """
        Omega Team

        Initializes a new DBInsert object.

        Args:
            db_name (str): The name of the database file.
        """
        self.db = DBExecute(db_name)
