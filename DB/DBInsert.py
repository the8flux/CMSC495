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
        self.db = DBExecute(db_name)

        self._EventViewerSource = "DBUpdate"
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
        self._log_it("Trying to Update:\n\t{0}\n\t{1}".format(query,parameters))
        try:
            self.cursor.execute(query, parameters)
            self.connection.commit()
            self._log_it("Updated!")
        except Exception as e:
            self._log_it("UPDATE FAILED!!! \n\t{0}, {1}\n\t\t{2}".format(query, parameters, e))
        finally:
            pass


    def add_price_adjustment(self, price_adjustment_id, title=None, reason_description=None,
                                is_fixed=None, fixed_amount=None, is_percent=None, percent=None):
        """
         PriceAdjustment Record

        :param price_adjustment_id:
        :param title:
        :param reason_description:
        :param is_fixed:
        :param fixed_amount:
        :param is_percent:
        :param percent:
        :return:
        """
        query = "UPDATE PriceAdjustment SET "
        parameters = []

        if title is not None:
            query += "Title = ?, "
            parameters.append(title)
        if reason_description is not None:
            query += "ReasonDescription = ?, "
            parameters.append(reason_description)
        if is_fixed is not None:
            query += "IsFixed = ?, "
            parameters.append(is_fixed)
        if fixed_amount is not None:
            query += "FixedAmount = ?, "
            parameters.append(fixed_amount)
        if is_percent is not None:
            query += "IsPercent = ?, "
            parameters.append(is_percent)
        if percent is not None:
            query += "Percent = ?, "
            parameters.append(percent)

        # Remove the trailing comma and space
        query = query[:-2]

        query += " WHERE PriceAdjustmentID = ?;"
        parameters.append(price_adjustment_id)

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)
        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_item_category(self, item_category_id, item_category_title=None, item_category_description=None):
        """
         ItemCategory record

        :param item_category_id:
        :param item_category_title:
        :param item_category_description:
        :return:
        """
        query = "UPDATE ItemCategories SET "
        parameters = []

        if item_category_title:
            query += "ItemCategoryTitle=?, "
            parameters.append(item_category_title)

        if item_category_description:
            query += "ItemCategoryDescription=?, "
            parameters.append(item_category_description)

        # Remove the trailing comma and space from the query string
        query = query[:-2]

        query += " WHERE ItemCategoryID=?;"
        parameters.append(item_category_id)

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_user_type(self, user_type_id, description=None):
        """
          UserType Record
        :param user_type_id:
        :param description:
        :return:
        """
        query = "UPDATE UserType SET"
        parameters = []

        if description:
            query += " Description = ?,"
            parameters.append(description)

        query = query.rstrip(",") + " WHERE UserTypeID = ?;"
        parameters.append(user_type_id)

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        self.cursor.execute(query, tuple(parameters))
        self.connection.commit()
        return self.cursor.lastrowid

    def add_catalog_item(self, catalog_item_id, manufacturer_id=None, catalog_item_name=None,
                            item_category_id=None, buy_cost=None):
        """

        :param catalog_item_id:
        :param manufacturer_id:
        :param catalog_item_name:
        :param item_category_id:
        :param buy_cost:
        :return:
        """
        query = "UPDATE CatalogItems SET"
        parameters = []
        if manufacturer_id:
            parameters.append(f"ManufacturerID = {manufacturer_id}")
        if catalog_item_name:
            parameters.append(f"CatalogItemName = '{catalog_item_name}'")
        if item_category_id:
            parameters.append(f"ItemCategoryID = {item_category_id}")
        if buy_cost:
            parameters.append(f"BuyCost = {buy_cost}")

        if not parameters:
            print("No values to update.")
            return

        query += " " + ", ".join(parameters)
        query += f" WHERE CatalogItemID = {catalog_item_id}"

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_inventory_item(self, item_id, catalog_item_id=None, stock_quantity=None, item_serial_number=None,
                              sell_price=None):
        """

        :param item_id:
        :param catalog_item_id:
        :param stock_quantity:
        :param item_serial_number:
        :param sell_price:
        :return:
        """
        query = "UPDATE InventoryItems SET "
        parameters = []
        if catalog_item_id is not None:
            query += "CatalogItemID = ?, "
            parameters.append(catalog_item_id)
        if stock_quantity is not None:
            query += "StockQuantity = ?, "
            parameters.append(stock_quantity)
        if item_serial_number is not None:
            query += "ItemSerialNumber = ?, "
            parameters.append(item_serial_number)
        if sell_price is not None:
            query += "SellPrice = ?, "
            parameters.append(sell_price)
        query = query.rstrip(", ") + " WHERE InventoryItemID = ?"
        parameters.append(item_id)

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_address(self, address_id, street_address=None, city=None, state=None, country=None, postal_code=None):
        """

        :param address_id:
        :param street_address:
        :param city:
        :param state:
        :param country:
        :param postal_code:
        :return:
        """

        query = "UPDATE Address SET "
        parameters = []

        if street_address:
            query += "StreetAddress = ?, "
            parameters.append(street_address)
        if city:
            query += "City = ?, "
            parameters.append(city)
        if state:
            query += "State = ?, "
            parameters.append(state)
        if country:
            query += "Country = ?, "
            parameters.append(country)
        if postal_code:
            query += "PostalCode = ?, "
            parameters.append(postal_code)

        query = query[:-2]  # remove the last comma and space
        query += " WHERE AddressID = ?;"
        parameters.append(address_id)

        log_it = list()
        log_it.append(query)
        log_it.append(parameters)
        self._log_it(log_it)

        # self._update(query, parameters)
        self.cursor.execute(query, parameters)
        self.connection.commit()
        return self.cursor.lastrowid
#########
    def add_manufacturer(self, manufacturer_id, manufacturer_name=None, manufacturer_description=None, address_id=None):
        """

        :param manufacturer_id:
        :param manufacturer_name:
        :param manufacturer_description:
        :param address_id:
        :return:
        """
        query = "UPDATE Manufacturers SET"
        params = []
        if manufacturer_name:
            query += " ManufacturerName = ?,"
            params.append(manufacturer_name)
        if manufacturer_description:
            query += " ManufacturerDescription = ?,"
            params.append(manufacturer_description)
        if address_id:
            query += " AddressID = ?,"
            params.append(address_id)
        query = query.rstrip(",") + " WHERE ManufacturerID = ?;"
        params.append(manufacturer_id)
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.lastrowid

    def add_customers(self, customer_id, address_id=None, customer_name=None):
        query = "UPDATE Customers SET "
        params = []

        if address_id:
            query += "AddressID = ?, "
            params.append(address_id)

        if customer_name:
            query += "CustomerName = ?, "
            params.append(customer_name)

        # Remove trailing comma and space
        query = query.rstrip(", ")

        # Add WHERE clause to update only the specified customer
        query += " WHERE CustomerID = ?"
        params.append(customer_id)

        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.lastrowid