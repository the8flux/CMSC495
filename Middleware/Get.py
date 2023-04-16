from DB.DBSelect import DBSelect
from Middleware.schema.Tables import *


class Get:
    def __init__(self, db_name):
        self._db = DBSelect(db_name)

    def addresses(self):
        return [Address(*address) for address in self._db.Address()]

    def catalog_items(self):
        return [CatalogItems(*catalog_item) for catalog_item in self._db.CatalogItems()]

    def customers(self):
        return [Customers(*customer) for customer in self._db.Customers()]

    def inventory_items(self):
        return [InventoryItems(*inventory_item) for inventory_item in self._db.InventoryItems()]

    def invoices(self):
        return [Invoices(*invoice) for invoice in self._db.Invoices()]

    def item_categories(self):
        return [ItemCategories(*item_category) for item_category in self._db.ItemCategories()]

    def line_items(self):
        return [LineItems(*line_item) for line_item in self._db.LineItems()]

    def manufacturers(self):
        return [Manufacturers(*manufacturer) for manufacturer in self._db.Manufacturers()]

    def price_adjustments(self):
        return [PriceAdjustment(*price_adjustment) for price_adjustment in self._db.PriceAdjustment()]

    def user_type(self):
        return [UserType(*user_type) for user_type in self._db.UserType()]

    def catalog_items(self):
        return [CatalogItems(*catalog_item) for catalog_item in self._db.CatalogItems()]
