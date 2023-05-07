import pprint

import DB.DBExtract
import DB.DBSelect
import DB.DBUpdate
import DB.DBInsert
import DB.DBInfo
import configparser

from flask import Flask, render_template, request, redirect, url_for

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

        # #################
        # # Testing lists #
        # #################
        # self.inventoryItems = [
        #     {"InventoryItemID": 1, "CatalogItemID": 1, "StockQuantity": 10, "ItemSerialNumber": "123ABC",
        #      "SellPrice": 10000},
        #     {"InventoryItemID": 2, "CatalogItemID": 2, "StockQuantity": 100, "ItemSerialNumber": "456DEF",
        #      "SellPrice": 1000},
        #     {"InventoryItemID": 3, "CatalogItemID": 3, "StockQuantity": 1000, "ItemSerialNumber": "789GHI",
        #      "SellPrice": 100},
        #     {"InventoryItemID": 4, "CatalogItemID": 4, "StockQuantity": 10000, "ItemSerialNumber": "999ZYX",
        #      "SellPrice": 10}]
        #
        # self.catalog_items = [
        #     {"ItemCatagoryID": 1, "ItemCatagoryTitle": "Electronics", "ItemCatagoryDescription": "Electronic gadgets"},
        #     {"ItemCatagoryID": 2, "ItemCatagoryTitle": "Home", "ItemCatagoryDescription": "Goes in the home"},
        #     {"ItemCatagoryID": 3, "ItemCatagoryTitle": "Food", "ItemCatagoryDescription": "Nom nom"},
        #     {"ItemCatagoryID": 4, "ItemCatagoryTitle": "Clothing", "ItemCatagoryDescription": "You wear it!"}]
        # self.manufacturers = [
        #     {"ManufacturerID": 1, "ManufacturerName": "Intel", "ManufacturerDescription": "Team Blue"},
        #     {"ManufacturerID": 2, "ManufacturerName": "AMD", "ManufacturerDescription": "Team Red"},
        #     {"ManufacturerID": 3, "ManufacturerName": "Nvidia", "ManufacturerDescription": "Team Green"},
        #     {"ManufacturerID": 4, "ManufacturerName": "Microsoft", "ManufacturerDescription": "Windows"}]
        # self.catalog_items = [
        #     {"CatalogItemID": 1, "ManufacturerID": 1, "CatalogItemName": "i9 9990XE", "ItemCatagoryID": 1,
        #      "BuyCost": 1000},
        #     {"CatalogItemID": 2, "ManufacturerID": 2, "CatalogItemName": "R9 7950X3D", "ItemCatagoryID": 1,
        #      "BuyCost": 750},
        #     {"CatalogItemID": 3, "ManufacturerID": 3, "CatalogItemName": "RTX 4090", "ItemCatagoryID": 1,
        #      "BuyCost": 1500},
        #     {"CatalogItemID": 4, "ManufacturerID": 4, "CatalogItemName": "Surface Pro", "ItemCatagoryID": 1,
        #      "BuyCost": 2000}]

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
            db_info = FrontEnd.QueryBuilder.TableInfo(self.db_name, table_name)
            self.current_record = db_info.get_row(record_id)

        def get_post_keys():
            return request.form.keys()

        def get_post_key(**kwargs):
            key = kwargs.get('key', None)
            default = kwargs.get('default', None)
            if key:
                return request.form.get(key)
            else:
                return default

        def get_get_key(**kwargs):
            key = kwargs.get('key', None)
            print(f"key={key}")
            default = kwargs.get('default', None)
            url = request.url
            parsed_url = urlparse(url)
            try:
                if key:
                    return_value = parse_qs(parsed_url.query)[key][0]
                    print(return_value)
                    return return_value
                return parse_qs(parsed_url.query)
            except:
                return default

        def switch_update(table_name):

            updater = DB.DBUpdate.DBUpdate(self.db_name)
            if table_name == 'ItemCategories':
                updater.update_item_category(get_post_key(key='id'),
                                            get_post_key(key='ItemCategoryTitle'),
                                            get_post_key(key='ItemCategoryDescription'))


            elif table_name == 'PriceAdjustment':
                # updater.update_price_adjustment()
                pass

            elif table_name == 'UserType':
                updater.update_user_type(get_post_key(key='id'),get_post_key(key='Description'))



            elif table_name == 'CatalogItems':
                updater.update_catalog_item(get_post_key(key='id'),
                                            get_post_key(key='Manufacturers'),
                                            get_post_key(key='CatalogItemName'),
                                            get_post_key(key='ItemCategories'),
                                            get_post_key(key='BuyCost'))


            elif table_name == 'InventoryItems':
                # updater.update_inventory_item()
                pass

            elif table_name == 'Address':
                updater.update_address(get_post_key(key='id'),
                                                get_post_key(key='StreetAddress'),
                                                get_post_key(key='City'),
                                                get_post_key(key='State'),
                                                get_post_key(key='Country'),
                                                get_post_key(key='PostalCode'))


            elif table_name == 'Manufacturers':
                updater.update_manufacturer(get_post_key(key='id'),
                                            get_post_key(key='ManufacturerName'),
                                            get_post_key(key='ManufacturerDescription'),
                                            get_post_key(key='Address'))



            elif table_name == 'Customers':
                updater.update_customers(get_post_key(key='id'),
                                       get_post_key(key='Address'),
                                       get_post_key(key='CustomerName'))



            elif table_name == 'Users':
                #updater.update_users(get_post_key(key='id'),
                #                        get_post_key(key='StreetAddress'),
                #                        get_post_key(key='City'),
                #                        get_post_key(key='State'),
                #                        get_post_key(key='Country'),
                #                        get_post_key(key='PostalCode')))
                pass

        def switch_add(table_name):
            adder = DB.DBInsert.DBInsert(self.db_name)
            if table_name == 'ItemCategories':
                last_row_id = adder.add_item_category(get_post_key(key='id'), get_post_key(key='ItemCategoryTitle'),
                                        get_post_key(key='ItemCategoryDescription'))
                return last_row_id


            elif table_name == 'PriceAdjustment':
                last_row_id = 0 # updater.update_price_adjustment()
                return last_row_id


            elif table_name == 'UserType':
                last_row_id = adder.add_user_type(get_post_key(key='id'), get_post_key(key='Description'))
                return last_row_id



            elif table_name == 'CatalogItems':
                last_row_id = adder.add_catalog_item(get_post_key(key='id'), get_post_key(key='Manufacturers'),
                                       get_post_key(key='CatalogItemName'), get_post_key(key='ItemCategories'),
                                       get_post_key(key='BuyCost'))
                return last_row_id


            elif table_name == 'InventoryItems':
                # updater.update_inventory_item()
                pass

            elif table_name == 'Address':
                last_row_id = adder.add_address(get_post_key(key='id'), get_post_key(key='StreetAddress'), get_post_key(key='City'),
                                  get_post_key(key='State'), get_post_key(key='Country'),
                                  get_post_key(key='PostalCode'))
                return last_row_id


            elif table_name == 'Manufacturers':
                last_row_id = adder.add_manufacturer(get_post_key(key='id'), get_post_key(key='ManufacturerName'),
                                       get_post_key(key='ManufacturerDescription'), get_post_key(key='Address'))
                return last_row_id



            elif table_name == 'Customers':
                last_row_id = adder.add_customers(get_post_key(key='id'), get_post_key(key='Address'),
                                    get_post_key(key='CustomerName'))
                return last_row_id



            elif table_name == 'Users':
                #last_row_id = adder.add_users(get_post_key(key='id'),
                #                        get_post_key(key='StreetAddress'),
                #                        get_post_key(key='City'),
                #                        get_post_key(key='State'),
                #                        get_post_key(key='Country'),
                #                        get_post_key(key='PostalCode')))
                #return last_row_id
                pass


        def switch_view(view_name) -> dict:
            viewer = DB.DBSelect.DBSelect(self.db_name)
            db_info = DB.DBInfo.DBInfo(self.db_name)
            headers = list()
            rows = list()

            if view_name == 'VIEW_CustomersAddress':
                headers = db_info.get_table_headers(view_name)
                rows = viewer.VIEW_CustomersAddress()

            elif view_name == 'VIEW_ManufacturersCatalogItems':
                headers = db_info.get_table_headers(view_name)
                rows = viewer.VIEW_ManufacturersCatalogItems()

            return {'headers': headers, 'rows': rows}













        @self.app.route('/', methods=['GET', 'POST'])
        def index():
            # update_frontend_table_info()

            tables = list()
            result_set = DB.DBExtract.DBExtract(self.db_name).get_table_names()
            for table in result_set:
                tables.append(table[0])

            # tables = ["Address", "CatalogItems", "Customers", "ItemCategories", "Manufacturers",
            #           "Users", "UserType"]
            tables.remove("PriceAdjustment")
            tables.remove("LineItems")
            tables.remove("Invoices")
            tables.remove("InventoryItems")




            if request.method == "POST":
                if request.form['table']:
                    if request.form['action'] == 'add':
                        return redirect(url_for('general_add', table_name=request.form['table']))
                    if request.form['action'] == 'update':
                        return redirect(url_for('add_general_update', table_name=request.form['table'], target_row_id=1))
            return render_template('index.html', config=self.config, css_class=self.css_class ,tables=tables)#, inventoryItems=self.inventoryItems)

        @self.app.route('/general_view',  methods=['GET', 'POST'])
        def view_general():
            view_name = get_get_key(key='view_name', default='Customers')
            view_data = switch_view(view_name)

            return render_template('general_read.html', config=self.config, view_name=view_name,
                                   headers=view_data['headers'],
                                   rows=view_data['rows'])





        @self.app.route('/general_update', methods=['GET', 'POST'])
        def add_general_update():
            table_name = get_get_key(key='table_name', default=None)
            target_row_id = int(get_get_key(key='target_row_id', default=-1))

            if request.method == "POST":
                table_name = request.form.get("table_name")
                target_row_id = int(request.form.get("id"))
                table_post_keys = get_post_keys()
                print(f"Table: {table_name} \n Post Keys {table_post_keys} ")
                print(get_post_key(key='ck_delete'))
                if get_post_key(key='ck_delete') == 'delete':
                    updater = DB.DBUpdate.DBUpdate(self.db_name)
                    id_col = get_post_key(key='id_column')
                    id_val = get_post_key(key='id')
                    result = updater.delete_item(table_name, id_col, id_val)
                    return render_template('general_del.html', config=self.config,
                                           table_name=table_name,
                                           css_class=self.css_class,
                                           result=result)


                switch_update(table_name)


                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name,
                                                                   table_name=table_name,
                                                                   target_row_id=target_row_id)

                select_records = form_element.get_update_selection_div()

                return render_template('general_update.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element,
                                       select_records=select_records)


            elif request.method == "GET" and table_name is not None and target_row_id is not None:

                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name,
                                                                   table_name=table_name,
                                                                   target_row_id=target_row_id)
                select_records = form_element.get_update_selection_div()
                return render_template('general_update.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element,
                                       select_records=select_records)

            else:

                form_element = FrontEnd.HTMLFormFactory.AddForm(db_name=self.db_name,
                                                                table_name=table_name,
                                                                target_row_id=target_row_id)

                return render_template('general_add.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)

        @self.app.route('/general_add', methods=['GET', 'POST'])
        def general_add():
            table_name = get_get_key(key='table_name', default='Customers')
            target_row_id = get_get_key(key='target_row_id', default=10)



            print(f"Get Key: {table_name}")
            if request.method == "POST":
                table_name = request.form.get("table_name")
                print(f"Post Key: {table_name}")

                target_row_id = switch_add(table_name)

                form_element = FrontEnd.HTMLFormFactory.UpdateForm(db_name=self.db_name, table_name=table_name,
                                                                   target_row_id=target_row_id)
                select_records = form_element.get_update_selection_div()

                return render_template('/general_update.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element,
                                       select_records=select_records)
            else:
                form_element = FrontEnd.HTMLFormFactory.AddForm(db_name=self.db_name, table_name=table_name,
                                                                target_row_id=target_row_id)
                return render_template('/general_add.html', config=self.config,
                                       table_name=table_name,
                                       css_class=self.css_class,
                                       form_element=form_element)





































































        ###################################################################################
        #
        # @self.app.route('/add_inventoryitem', methods=['GET', 'POST'])
        # def add_inventoryitem():
        #     update_frontend_table_info()
        #
        #     if request.method == "POST":
        #
        #         # form_html_element = FrontEnd.
        #
        #         ## BEGIN add to local list (change this to call something to add to db)
        #         self.inventoryItems.append({"InventoryItemID": len(self.inventoryItems) + 1,
        #                                     "CatalogItemID": request.form.get("CatalogItem"),
        #                                     "StockQuantity": request.form.get("StockQuantity"),
        #                                     "ItemSerialNumber": request.form.get("ItemSerialNumber"),
        #                                     "SellPrice": request.form.get("SellPrice")})
        #         ## END add to local list
        #         return render_template('update_inventoryitem.html', config=self.config,
        #                                manufacturer_select_tag=self.manufacturer_select_tag,
        #                                inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)
        #     else:
        #         return render_template('add_inventoryitem.html', config=self.config,
        #                                manufacturer_select_tag=self.manufacturer_select_tag,
        #                                catalogItems=self.catalog_items)
        #
        # @self.app.route('/add_catalogitem', methods=['GET', 'POST'])
        # def add_catalogitem():
        #     update_frontend_table_info()
        #     if request.method == "POST":
        #         ## BEGIN add to local list (change this to call something to add to db)
        #         self.catalog_items.append({"CatalogItemID": len(self.catalog_items) + 1,
        #                                    "ManufacturerID": request.form.get("Manufacturer"),
        #                                    "CatalogItemName": request.form.get("CatalogItemName"),
        #                                    "ItemCatagoryID": request.form.get("ItemCatagory"),
        #                                    "BuyCost": request.form.get("BuyCost")})
        #         ## END add to local list
        #         return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
        #                                catalogItems=self.catalog_items, catagories=self.catalog_items)
        #     else:
        #         return render_template('add_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
        #                                catagories=self.catalog_items)
        #
        # @self.app.route('/add_itemcatagory', methods=['GET', 'POST'])
        # def add_itemcatagory():
        #     update_frontend_table_info()
        #
        #     if request.method == "POST":
        #         ## BEGIN add to local list (change this to call something to add to db)
        #         self.catalog_items.append({"ItemCatagoryID": len(self.catalog_items) + 1,
        #                                    "ItemCatagoryTitle": request.form.get("ItemCatagoryTitle"),
        #                                    "ItemCatagoryDescription": request.form.get("ItemCatagoryDescription")})
        #         ## END add to local list
        #         return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)
        #     else:
        #         return render_template('add_itemcatagory.html', config=self.config)
        #
        # # /\ /\ /\ ADD pages
        # # \/ \/ \/ UPDATE pages
        #
        # @self.app.route('/update_inventoryitem', methods=['GET', 'POST'])
        # def update_inventoryitem():
        #
        #     update_frontend_table_info()
        #     if request.method == "POST":
        #         ## BEGIN add to local list (change this to call something to edit data in db)
        #         for i in self.inventoryItems:
        #             if i["InventoryItemID"] == int(request.form.get("inventoryItem")):
        #                 self.ind = self.inventoryItems.index(i)
        #         self.inventoryItems[self.ind] |= {"CatalogItemID": request.form.get('CatalogItem')}
        #         self.inventoryItems[self.ind] |= {"StockQuantity": request.form.get('StockQuantity')}
        #         self.inventoryItems[self.ind] |= {"ItemSerialNumber": request.form.get('ItemSerialNumber')}
        #         self.inventoryItems[self.ind] |= {"SellPrice": request.form.get('SellPrice')}
        #         ## END add to local list
        #         return render_template('update_inventoryitem.html', config=self.config,
        #                                inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)
        #     else:
        #         return render_template('update_inventoryitem.html', config=self.config,
        #                                inventoryItems=self.inventoryItems, catalogItems=self.catalog_items)
        #
        # @self.app.route('/update_catalogitem', methods=['GET', 'POST'])
        # def update_catalogitem():
        #     update_frontend_table_info()
        #
        #     if request.method == "POST":
        #         ## BEGIN add to local list (change this to call something to edit data in db)
        #         for i in self.catalog_items:
        #             if i["CatalogItemID"] == int(request.form.get("CatalogItem")):
        #                 self.ind = self.catalog_items.index(i)
        #         self.catalog_items[self.ind] |= {"ManufacturerID": request.form.get('Manufacturer')}
        #         self.catalog_items[self.ind] |= {"CatalogItemName": request.form.get('CatalogItemName')}
        #         self.catalog_items[self.ind] |= {"ItemCatagoryID": request.form.get('ItemCatagory')}
        #         self.catalog_items[self.ind] |= {"BuyCost": request.form.get('BuyCost')}
        #         ## END add to local list
        #         return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
        #                                catalogItems=self.catalog_items, catagories=self.catalog_items)
        #     else:
        #         return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers,
        #                                catalogItems=self.catalog_items, catagories=self.catalog_items)
        #
        # @self.app.route('/update_itemcatagory', methods=['GET', 'POST'])
        # def update_itemcatagory():
        #     update_frontend_table_info()
        #     if request.method == "POST":
        #         ## BEGIN add to local list (change this to call something to edit data in db)
        #         for i in self.catalog_items:
        #             if i["ItemCatagoryID"] == int(request.form.get("ItemCatagory")):
        #                 self.ind = self.catalog_items.index(i)
        #         self.catalog_items[self.ind] |= {"ItemCatagoryTitle": request.form.get('ItemCatagoryTitle')}
        #         self.catalog_items[self.ind] |= {"ItemCatagoryDescription": request.form.get('ItemCatagoryDescription')}
        #         ## END add to local list
        #         return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)
        #     else:
        #         return render_template('update_itemcatagory.html', config=self.config, catagories=self.catalog_items)

        @self.app.route('/error/<string:e>')
        def error(e):
            return render_template('error.html', error=e)

        if __name__ == "__main__":
            self.app.run(host="127.0.0.1", debug=False)
