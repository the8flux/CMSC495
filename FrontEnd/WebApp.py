import pprint

import DB.DBExtract
import DB.DBSelect
import configparser

from flask import Flask, render_template, request

import FrontEnd.QueryBuilder
import FrontEnd.HTMLElementFactory
import FrontEnd.HTMLFormFactory
import FrontEnd.CSSLoader
from urllib.parse import urlparse
from urllib.parse import parse_qs

class WebApp:
    def __init__(self):
        ################
        version = "0.1"
        ################

        self.app = Flask(__name__)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.config.set('systemSettings', 'version', version)
        self.css_class = FrontEnd.CSSLoader.CSSLoader().get_css()
        self.db_name = '../DB/databases/test_db3.db'

        self.tables = list()
        self.table = dict()
        self.current_record = dict()




        #################
        # Testing lists #
        #################
        self.inventoryItems = [
            {"InventoryItemID": 1, "CatalogItemID": 1, "StockQuantity": 10, "ItemSerialNumber": "123ABC",
             "SellPrice": 10000},
            {"InventoryItemID": 2, "CatalogItemID": 2, "StockQuantity": 100, "ItemSerialNumber": "456DEF",
             "SellPrice": 1000},
            {"InventoryItemID": 3, "CatalogItemID": 3, "StockQuantity": 1000, "ItemSerialNumber": "789GHI",
             "SellPrice": 100},
            {"InventoryItemID": 4, "CatalogItemID": 4, "StockQuantity": 10000, "ItemSerialNumber": "999ZYX",
             "SellPrice": 10}]

        self.catalog_items = [
            {"ItemCatagoryID": 1, "ItemCatagoryTitle": "Electronics", "ItemCatagoryDescription": "Electronic gadgets"},
            {"ItemCatagoryID": 2, "ItemCatagoryTitle": "Home", "ItemCatagoryDescription": "Goes in the home"},
            {"ItemCatagoryID": 3, "ItemCatagoryTitle": "Food", "ItemCatagoryDescription": "Nom nom"},
            {"ItemCatagoryID": 4, "ItemCatagoryTitle": "Clothing", "ItemCatagoryDescription": "You wear it!"}]
        self.manufacturers = [
            {"ManufacturerID": 1, "ManufacturerName": "Intel", "ManufacturerDescription": "Team Blue"},
            {"ManufacturerID": 2, "ManufacturerName": "AMD", "ManufacturerDescription": "Team Red"},
            {"ManufacturerID": 3, "ManufacturerName": "Nvidia", "ManufacturerDescription": "Team Green"},
            {"ManufacturerID": 4, "ManufacturerName": "Microsoft", "ManufacturerDescription": "Windows"}]
        self.catalog_items = [
            {"CatalogItemID": 1, "ManufacturerID": 1, "CatalogItemName": "i9 9990XE", "ItemCatagoryID": 1,
             "BuyCost": 1000},
            {"CatalogItemID": 2, "ManufacturerID": 2, "CatalogItemName": "R9 7950X3D", "ItemCatagoryID": 1,
             "BuyCost": 750},
            {"CatalogItemID": 3, "ManufacturerID": 3, "CatalogItemName": "RTX 4090", "ItemCatagoryID": 1,
             "BuyCost": 1500},
            {"CatalogItemID": 4, "ManufacturerID": 4, "CatalogItemName": "Surface Pro", "ItemCatagoryID": 1,
             "BuyCost": 2000}]


        def update_frontend_table_info():
            db_info = DB.DBExtract.DBExtract(self.db_name)
            tables_names = db_info.get_table_names()
            self.table = dict()
            for table_name in tables_names:
                self.table['table_name'] = table_name[0]
                self.table['table_info'] = FrontEnd.QueryBuilder.TableInfo(self.db_name, self.table['table_name'])
                self.table['table_data'] = self.table['table_info'].get_rows()
            self.tables.append(self.table)



            pprint.pprint(self.tables)

        def set_current_record(table_name, record_id):
            db_info = FrontEnd.QueryBuilder.TableInfo(self.db_name,table_name)
            self.current_record = db_info.get_row(record_id)


        def get_post_keys(**kwargs):
            return_value =  request.form.keys()
            key = kwargs.get('key', None)
            if key:
                return key
            return return_value


        def get_get_key(**kwargs):
            key = kwargs.get('key', None)
            url = request.url
            parsed_url = urlparse(url)
            try:
                if key:
                    return parse_qs(parsed_url.query)[key][0]
                return parse_qs(parsed_url.query)
            except:
                return None

        @self.app.route('/')
        def index():
            update_frontend_table_info()
            return render_template('index.html', config=self.config, inventoryItems=self.inventoryItems)


        @self.app.route('/general_update', methods=['GET', 'POST'])
        def add_general_update():
            table_name = get_get_key(key='table_name')
            print(f"Get Key: {table_name}")
            if request.method == "POST":
                table_name = request.form.get("table_name")
                if table_name is None:
                    table_name = 'Customers'
                print(f"Post Key: {table_name}")
                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name, table_name='Customers', target_row_id=10)

                ## BEGIN add to local list (change this to call something to add to db)
                self.inventoryItems.append({"InventoryItemID": len(self.inventoryItems) + 1,
                                            "CatalogItemID": request.form.get("CatalogItem"),
                                            "StockQuantity": request.form.get("StockQuantity"),
                                            "ItemSerialNumber": request.form.get("ItemSerialNumber"),
                                            "SellPrice": request.form.get("SellPrice")})
                ## END add to local list
                return render_template('general_update.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)
            else:
                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name, table_name='Customers', target_row_id=10)
                return render_template('general_add.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)
        @self.app.route('/general_add', methods=['GET', 'POST'])
        def general_add():
            table_name = get_get_key(key='table_name')
            print(f"Get Key: {table_name}")
            if request.method == "POST":
                if table_name is None:
                    table_name = 'Customers'
                table_name = request.form.get("table_name",'Customers')
                print(f"Post Key: {table_name}")
                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name, table_name='Customers', target_row_id=10)
                ## BEGIN add to local list (change this to call something to add to db)
                self.inventoryItems.append({"InventoryItemID": len(self.inventoryItems) + 1,
                                            "CatalogItemID": request.form.get("CatalogItem"),
                                            "StockQuantity": request.form.get("StockQuantity"),
                                            "ItemSerialNumber": request.form.get("ItemSerialNumber"),
                                            "SellPrice": request.form.get("SellPrice")})
                ## END add to local list
                return render_template('/general_update.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)
            else:
                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name, table_name='Customers', target_row_id=10)
                return render_template('/general_add.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)




###################################################################################


        @self.app.route('/add_inventoryitem', methods=['GET', 'POST'])
        def add_inventoryitem():
            update_frontend_table_info()

            if request.method == "POST":

                #form_html_element = FrontEnd.

                ## BEGIN add to local list (change this to call something to add to db)
                self.inventoryItems.append({"InventoryItemID": len(self.inventoryItems) + 1,
                                            "CatalogItemID": request.form.get("CatalogItem"),
                                            "StockQuantity": request.form.get("StockQuantity"),
                                            "ItemSerialNumber": request.form.get("ItemSerialNumber"),
                                            "SellPrice": request.form.get("SellPrice")})
                ## END add to local list
                return render_template('update_inventoryitem.html', config=self.config,manufacturer_select_tag=self.manufacturer_select_tag,
                                       inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)
            else:
                return render_template('add_inventoryitem.html', config=self.config, manufacturer_select_tag=self.manufacturer_select_tag, catalogItems=self.catalog_items)

        @self.app.route('/add_catalogitem', methods=['GET', 'POST'])
        def add_catalogitem():
            update_frontend_table_info()
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to add to db)
                self.catalog_items.append({"CatalogItemID": len(self.catalog_items) + 1,
                                          "ManufacturerID": request.form.get("Manufacturer"),
                                          "CatalogItemName": request.form.get("CatalogItemName"),
                                          "ItemCatagoryID": request.form.get("ItemCatagory"),
                                          "BuyCost": request.form.get("BuyCost")})
                ## END add to local list
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
                                       catalogItems=self.catalog_items, catagories=self.catalog_items)
            else:
                return render_template('add_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
                                       catagories=self.catalog_items)

        @self.app.route('/add_itemcatagory', methods=['GET', 'POST'])
        def add_itemcatagory():
            update_frontend_table_info()

            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to add to db)
                self.catalog_items.append({"ItemCatagoryID": len(self.catalog_items) + 1,
                                        "ItemCatagoryTitle": request.form.get("ItemCatagoryTitle"),
                                        "ItemCatagoryDescription": request.form.get("ItemCatagoryDescription")})
                ## END add to local list
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)
            else:
                return render_template('add_itemcatagory.html', config=self.config)

        # /\ /\ /\ ADD pages
        # \/ \/ \/ UPDATE pages

        @self.app.route('/update_inventoryitem', methods=['GET', 'POST'])
        def update_inventoryitem():

            update_frontend_table_info()
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.inventoryItems:
                    if i["InventoryItemID"] == int(request.form.get("inventoryItem")):
                        self.ind = self.inventoryItems.index(i)
                self.inventoryItems[self.ind] |= {"CatalogItemID": request.form.get('CatalogItem')}
                self.inventoryItems[self.ind] |= {"StockQuantity": request.form.get('StockQuantity')}
                self.inventoryItems[self.ind] |= {"ItemSerialNumber": request.form.get('ItemSerialNumber')}
                self.inventoryItems[self.ind] |= {"SellPrice": request.form.get('SellPrice')}
                ## END add to local list
                return render_template('update_inventoryitem.html', config=self.config,
                                       inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)
            else:
                return render_template('update_inventoryitem.html', config=self.config,
                                       inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)

        @self.app.route('/update_catalogitem', methods=['GET', 'POST'])
        def update_catalogitem():
            update_frontend_table_info()



            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.catalog_items:
                    if i["CatalogItemID"] == int(request.form.get("CatalogItem")):
                        self.ind = self.catalog_items.index(i)
                self.catalog_items[self.ind] |= {"ManufacturerID": request.form.get('Manufacturer')}
                self.catalog_items[self.ind] |= {"CatalogItemName": request.form.get('CatalogItemName')}
                self.catalog_items[self.ind] |= {"ItemCatagoryID": request.form.get('ItemCatagory')}
                self.catalog_items[self.ind] |= {"BuyCost": request.form.get('BuyCost')}
                ## END add to local list
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
                                       catalogItems=self.catalog_items, catagories=self.catalog_items)
            else:
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
                                       catalogItems=self.catalog_items, catagories=self.catalog_items)

        @self.app.route('/update_itemcatagory', methods=['GET', 'POST'])
        def update_itemcatagory():
            update_frontend_table_info()
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.catalog_items:
                    if i["ItemCatagoryID"] == int(request.form.get("ItemCatagory")):
                        self.ind = self.catalog_items.index(i)
                self.catalog_items[self.ind] |= {"ItemCatagoryTitle": request.form.get('ItemCatagoryTitle')}
                self.catalog_items[self.ind] |= {"ItemCatagoryDescription": request.form.get('ItemCatagoryDescription')}
                ## END add to local list
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)
            else:
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)

        @self.app.route('/error/<string:e>')
        def error(e):
            return render_template('error.html', error=e)

        if __name__ == "__main__":
            self.app.run(host="127.0.0.1", debug=False)
