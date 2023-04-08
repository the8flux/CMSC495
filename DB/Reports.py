import sqlite3
from DB import DBSelect
from DB import EventViewer
import pprint

"""
        CMSC 495 7385: CURRENT TRENDS AND PROJECTS IN COMPUTER SCIENCE
        UNIVERSITY OF MARYLAND GLOBAL CAMPUS
        DR. CHRISTOPHER GORHAM

        Ravi Mali	240-784-6523
        Robert Branson	406-548-4845
        William Adair	619-967-3065
        Glenn Phillips 	443-915-0172
"""


class Reports:


    def __init__(self, db_name):
        """
        Initializes a new Reports object.

        Args:
            db_name (str): The name of the database file.
        """
        self._report = ""
        self._report_header = ""
        self._report_style = ""
        self._report_footer = ""
        self._report_body = ""
        self._report_content = ""

        self.db_connection = DBSelect.DBSelect(db_name)



    def _init_report_style(self, **kwargs):
        self._report_style = """
                    <style>
                      /* Define colors */
                      .color-1 {
                        color: #333366;
                      }
                
                      .color-2 {
                        color: #336699;
                      }
                
                      .color-3 {
                        color: #0099CC;
                      }
                
                      /* Define div styles */
                      .view-div {
                        # max-width: 3000px;
                        margin: 0 auto;
                        padding: 20px;
                        border: 1px solid #ddd;
                        box-shadow: 2px 2px 2px #ddd;
                      }
                
                      .view-div h2 {
                        margin-top: 0;
                        font-size: 24px;
                        font-weight: bold;
                        text-align: center;
                        text-transform: uppercase;
                        letter-spacing: 2px;
                      }
                
                      .view-div table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                      }
                
                      .view-div table th,
                      .view-div table td {
                        padding: 10px;
                        text-align: center;
                        border: 1px solid #ddd;
                      }
                
                      .view-div table th {
                        background-color: #333366;
                        color: white;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                      }
                
                      .view-div table tr:nth-child(even) {
                        background-color: #f2f2f2;
                      }
                    </style>"""

    def _init_report_header(self, report_title):
        self._report_header = """           
        <!DOCTYPE html>
                <html>
                  <head>
                    <title>"""

        self._report_header += report_title
        self._report_header += """</title>"""
        self._report_header += self._report_style
        self._report_header += """</head>"""

    def _init_body(self, title):
        self._report_body += """<body>"""
        self._report_body += """<div class="view-div">"""
        self._report_body += "<h2>{}</h2>".format(title)



    def _init_report_footer(self):

        self._report_footer = """</body></html>"""


    def _build_report(self):
        """

        :return:
        """
        self._report = ""
        self._report += self._report_header
        self._report += self._report_body
        self._report += self._report_content
        self._report += self._report_footer
        return self._report


    def init_build_report_content_selector(self,**kwargs):
        pass



    def getInvoice(self):
        pass



    def VIEW_UserCusomers(self):
        result_set = self.db_connection.VIEW_UserCustomers()
        table_rows = list()
        title = "User Customers View"
        file_name = "VIEW_UserCustomers.html"
        table_row = """ <table>
                        <thead>
                        <tr>
                        <th class="color-2">ID</th>
                        <th class="color-1">First Name</th>
                        <th class="color-2">Last Name</th>
                        <th class="color-1">Email</th>
                        <th class="color-2">Telephone</th>
                        <th class="color-1">User Logon</th>
                        <th class="color-2">User Type</th>
                        <th class="color-1">Customer Name</th>
                      </tr></thead>"""

        for row in result_set:

            table_row = " ".join([table_row, "<tr>"])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[0])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[1])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[2])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[3])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[4])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[5])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[6])])
            table_row = " ".join([table_row, "<td>{}</td>".format(row[7])])
            table_row = " ".join([table_row, "</tr>\n"])
            table_rows.append(table_row)
            table_row = ""

        table_rows_str = " ".join(table_rows)
        #table_rows_str = "{}{} ".format(table_rows_str, "</thead>")
        self._report_content = table_rows_str
        self._init_report_style()
        self._init_report_header(title)
        self._init_body(title)
        self._init_report_footer()
        self._build_report()

        Reports.save_file(file_name, self._report)
        return self._report






    @classmethod
    def save_file(cls, filename, content):
        with open(f"{filename}"+".html", 'w') as f:
            f.write(content)

    @classmethod
    def log_it(cls, msg):
        EventViewerSource = "StaticHTMLViews"
        formatted_result_set = "{0}{1}".format("Result Set Found...\n\t", pprint.pformat(msg))
        EventViewer.EventViewer.log(EventViewerSource, formatted_result_set)


def VIEW_UserCustomers_test(self):
    """



    :return:
    """

    html_part_1 = """
            <!DOCTYPE html>
                <html>
                  <head>
                    <title>User Customers View</title>
                    <style>
                      /* Define colors */
                      .color-1 {
                        color: #333366;
                      }

                      .color-2 {
                        color: #336699;
                      }

                      .color-3 {
                        color: #0099CC;
                      }

                      /* Define div styles */
                      .view-div {
                        # max-width: 3000px;
                        margin: 0 auto;
                        padding: 20px;
                        border: 1px solid #ddd;
                        box-shadow: 2px 2px 2px #ddd;
                      }

                      .view-div h2 {
                        margin-top: 0;
                        font-size: 24px;
                        font-weight: bold;
                        text-align: center;
                        text-transform: uppercase;
                        letter-spacing: 2px;
                      }

                      .view-div table {
                        width: 100%;
                        border-collapse: collapse;
                        margin-top: 20px;
                      }

                      .view-div table th,
                      .view-div table td {
                        padding: 10px;
                        text-align: center;
                        border: 1px solid #ddd;
                      }

                      .view-div table th {
                        background-color: #333366;
                        color: white;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                      }

                      .view-div table tr:nth-child(even) {
                        background-color: #f2f2f2;
                      }
                    </style>
                  </head>
                  <body>
                    <div class="view-div">
                      <h2>User Customers View</h2>
                      <table>
                        <thead>
                          <tr>
                            <th class="color-2">ID</th>
                            <th class="color-1">First Name</th>
                            <th class="color-2">Last Name</th>
                            <th class="color-1">Email</th>
                            <th class="color-2">Telephone</th>
                            <th class="color-1">User Logon</th>
                            <th class="color-2">User Type</th>
                            <th class="color-1">Customer Name</th>
                          </tr>
                        </thead>
                        <tbody>

                          """
    html_part_2 = """

                          <!-- Additional rows here -->
                        </tbody>
                      </table>
                    </div>
                  </body>
                </html>
        """

    view = DBSelect.DBSelect("./databases/test_db3.db")
    result_set = view.VIEW_UserCustomers()
    table_rows = list()

    for row in result_set:
        table_row = ""
        table_row = " ".join([table_row, "<tr>"])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[0])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[1])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[2])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[3])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[4])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[5])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[6])])
        table_row = " ".join([table_row, "<td>{}</td>".format(row[7])])
        table_row = " ".join([table_row, "</tr>\n"])
        table_rows.append(table_row)

    table_rows_str = " ".join(table_rows)
    html_page = " "
    html_page = " ".join([html_page, html_part_1])
    html_page = " ".join([html_page, table_rows_str])
    html_page = " ".join([html_page, html_part_2])

    Reports.log_it(html_page)
    Reports.save_file("VIEW_UserCustomers", html_page)
    return html_page

