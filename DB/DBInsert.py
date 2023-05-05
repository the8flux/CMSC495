from DB import DBExecute
from DB import DBExecute
from DB import EventViewer
import pprint
import sqlite3

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
        self.db = DBExecute.DBExecute(db_name)

        self._EventViewerSource = "DBInsert"
        self.db = DBExecute.DBExecute(db_name)
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def _log_it(self, msg):
        """
         Logging Function
        :param msg:
        :return:
        """
        msg = "Result Set Found...\n\t"
        formatted_result_set = "{}".format(pprint.pformat(msg))
        EventViewer.EventViewer.log(self._EventViewerSource, "{0}{1}".format(msg, formatted_result_set))

    def _add(self, query, parameters):
        """
        Generalized Update for all methods in this class
        :param query:
        :param parameters:
        :return:
        """
        self._log_it("Trying to Update:\n\t{0}\n\t{1}".format(query, parameters))
        try:
            self.cursor.execute(query, parameters)
            self.connection.commit()
            self._log_it("Updated!")
        except Exception as e:
            self._log_it("UPDATE FAILED!!! \n\t{0}, {1}\n\t\t{2}".format(query, parameters, e))
        finally:
            pass

    def add_price_adjustment(self, no_id="NoID", title=None, reason_description=None,
                             is_fixed=None, fixed_amount=None, is_percent=None, percent=None):
        """
        Add PriceAdjustment Record

        :param no_id:
        :param title:
        :param reason_description:
        :param is_fixed:
        :param fixed_amount:
        :param is_percent:
        :param percent:
        :return:
        """
        query = "INSERT INTO PriceAdjustment "
        parameters = []
        values_position = " "

        if title is not None:
            query += "Title, "
            values_position += " ?, "
            parameters.append(title)
        if reason_description is not None:
            query += "ReasonDescription, "
            values_position += " ?, "
            parameters.append(reason_description)
        if is_fixed is not None:
            query += "IsFixed, "
            values_position += " ?, "
            parameters.append(is_fixed)
        if fixed_amount is not None:
            query += "FixedAmount, "
            values_position += " ?, "
            parameters.append(fixed_amount)
        if is_percent is not None:
            query += "IsPercent, "
            values_position += " ?, "
            parameters.append(is_percent)
        if percent is not None:
            query += "Percent, "
            values_position += " ?, "
            parameters.append(percent)

        # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)
        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_item_category(self, item_category_id='NoID', item_category_title=None, item_category_description=None):
        """
         Add Item Category
        :param item_category_id:
        :param item_category_title:
        :param item_category_description:
        :return:
        """
        query = "INSERT INTO ItemCategories ("
        parameters = []
        values_position = " "

        if item_category_title:
            query += "ItemCategoryTitle, "
            values_position += " ?, "
            parameters.append(item_category_title)

        if item_category_description:
            query += "ItemCategoryDescription, "
            values_position += " ?, "
            parameters.append(item_category_description)

            # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"


        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_user_type(self, user_type_id='NoID', description=None):
        """
          UserType Record
        :param user_type_id:
        :param description:
        :return:
        """

        query = "INSERT INTO UserType ( "
        parameters = []
        values_position = " "

        if description:
            query += " Description "
            parameters.append(description)
            values_position += " ? "

        query += f" ) VALUES ( {values_position} );"

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        self.cursor.execute(query, tuple(parameters))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_catalog_item(self, catalog_item_id='NoId', manufacturer_id=None, catalog_item_name=None,
                         item_category_id=None, buy_cost=None):
        """

        :param catalog_item_id:
        :param manufacturer_id:
        :param catalog_item_name:
        :param item_category_id:
        :param buy_cost:
        :return:
        """

        query = "INSERT INTO CatalogItems ("
        parameters = []
        values_position = "  "

        if manufacturer_id is not None:
            query += "ManufacturerID, "
            values_position += " ?, "
            parameters.append(manufacturer_id)
        if catalog_item_name is not None:
            query += "CatalogItemName, "
            values_position += " ?, "
            parameters.append(catalog_item_name)
        if item_category_id is not None:
            query += "ItemCategoryID, "
            values_position += " ?, "
            parameters.append(item_category_id)
        if buy_cost is not None:
            query += "BuyCost, "
            values_position += " ?, "
            parameters.append(buy_cost)

        # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]
        query += f" ) VALUES ( {values_position} );"


        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_inventory_item(self, item_id='NOID', catalog_item_id=None, stock_quantity=None, item_serial_number=None,
                           sell_price=None):
        """
        :param item_id:
        :param catalog_item_id:
        :param stock_quantity:
        :param item_serial_number:
        :param sell_price:
        :return:
        """

        query = "INSERT INTO InventoryItems ( "
        parameters = []
        values_position = " "

        if catalog_item_id is not None:
            query += "CatalogItemID, "
            values_position += " ?, "
            parameters.append(catalog_item_id)
        if stock_quantity is not None:
            query += "StockQuantity, "
            values_position += " ?, "
            parameters.append(stock_quantity)
        if item_serial_number is not None:
            query += "ItemSerialNumber, "
            values_position += " ?, "
            parameters.append(item_serial_number)
        if sell_price is not None:
            query += "SellPrice, "
            values_position += " ?, "
            parameters.append(sell_price)


            # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"


        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_address(self, address_id='NoID', street_address=None, city=None, state=None, country=None, postal_code=None):
        """

        :param address_id:
        :param street_address:
        :param city:
        :param state:
        :param country:
        :param postal_code:
        :return:
        """

        query = "INSERT INTO Address ( "
        parameters = []
        values_position = "  "

        if street_address is not None:
            query += "StreetAddress, "
            values_position += " ?, "
            parameters.append(street_address)
        if city is not None:
            query += "City, "
            values_position += " ?, "
            parameters.append(city)
        if state is not None:
            query += "State, "
            values_position += " ?, "
            parameters.append(state)
        if country is not None:
            query += "Country, "
            values_position += " ?, "
            parameters.append(country)
        if postal_code is not None:
            query += "PostalCode, "
            values_position += " ?, "
            parameters.append(postal_code)

            # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"
        print(query)
        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    #########
    def add_manufacturer(self, manufacturer_id='NoID', manufacturer_name=None, manufacturer_description=None, address_id=None):
        """

        :param manufacturer_id:
        :param manufacturer_name:
        :param manufacturer_description:
        :param address_id:
        :return:
        """

        query = "INSERT INTO Manufacturers ( "
        parameters = []
        values_position = " "

        if manufacturer_name:
            query += " ManufacturerName, "
            values_position += " ?, "
            parameters.append(manufacturer_name)
        if manufacturer_description:
            query += " ManufacturerDescription, "
            values_position += " ?, "
            parameters.append(manufacturer_description)
        if address_id:
            query += " AddressID, "
            values_position += " ?, "
            parameters.append(address_id)

            # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"

        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_customers(self, customer_id='NoID', address_id=None, customer_name=None):
        query = "INSERT INTO Customers ( "
        parameters = []
        values_position = " "

        if address_id:
            query += "AddressID, "
            values_position += " ?, "
            parameters.append(address_id)

        if customer_name:
            query += "CustomerName , "
            values_position += " ?, "
            parameters.append(customer_name)

        # Remove the trailing comma and space
        query = query[:-2]
        values_position = values_position[:-2]

        query += f" ) VALUES ( {values_position} );"

        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid
