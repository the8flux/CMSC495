from pprint import pprint
import datetime

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class EventViewer:
    """
    Omega Team

    A simple class to display and log to a quick logfile database events

    Attributes:

    """

    def __init__(self):
        """

        """

    @staticmethod
    def log(source, event, **kwargs):
        """
         Print and Log Event
        :param source:
        :param event:
        :return:
        """
        pprint_flag = False
        pprint_flag_override = False

        if kwargs.get('pprint') is not None:
            if pprint_flag == 'True':
                pprint_flag = True

        if pprint_flag_override:
            pprint_flag = True;

        output = "{},  {}, {}\n".format(datetime.datetime.now(), source, event)
        if pprint_flag:
            pprint(output)
        with open('db_event_viewer.log', 'a') as file:
            # Write some text to the file
            file.write(output)
