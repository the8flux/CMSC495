import configparser

from flask import Flask, render_template, request

class WebApp:
    def __init__(self):
        ################
        version = "0.1"
        ################

        self.app = Flask(__name__)

        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.config.set('systemSettings', 'version', version)

        #################
        # Testing lists #
        #################
        self.inventoryItems = [{"InventoryItemID":1,"CatalogItemID":1,"StockQuantity":10,"ItemSerialNumber":"123ABC","SellPrice":10000}, 
                               {"InventoryItemID":2,"CatalogItemID":2,"StockQuantity":100,"ItemSerialNumber":"456DEF","SellPrice":1000},
                               {"InventoryItemID":3,"CatalogItemID":3,"StockQuantity":1000,"ItemSerialNumber":"789GHI","SellPrice":100},
                               {"InventoryItemID":4,"CatalogItemID":4,"StockQuantity":10000,"ItemSerialNumber":"999ZYX","SellPrice":10}]
        self.catagories = [{"ItemCatagoryID":1,"ItemCatagoryTitle":"Electronics","ItemCatagoryDescription":"Electronic gadgets"},
                           {"ItemCatagoryID":2,"ItemCatagoryTitle":"Home","ItemCatagoryDescription":"Goes in the home"},
                           {"ItemCatagoryID":3,"ItemCatagoryTitle":"Food","ItemCatagoryDescription":"Nom nom"},
                           {"ItemCatagoryID":4,"ItemCatagoryTitle":"Clothing","ItemCatagoryDescription":"You wear it!"}]
        self.manufacturers = [{"ManufacturerID":1,"ManufacturerName":"Intel","ManufacturerDescription":"Team Blue"},
                              {"ManufacturerID":2,"ManufacturerName":"AMD","ManufacturerDescription":"Team Red"},
                              {"ManufacturerID":3,"ManufacturerName":"Nvidia","ManufacturerDescription":"Team Green"},
                              {"ManufacturerID":4,"ManufacturerName":"Microsoft","ManufacturerDescription":"Windows"}]
        self.catalogItems = [{"CatalogItemID":1,"ManufacturerID":1,"CatalogItemName":"i9 9990XE","ItemCatagoryID":1,"BuyCost":1000},
                             {"CatalogItemID":2,"ManufacturerID":2,"CatalogItemName":"R9 7950X3D","ItemCatagoryID":1,"BuyCost":750},
                             {"CatalogItemID":3,"ManufacturerID":3,"CatalogItemName":"RTX 4090","ItemCatagoryID":1,"BuyCost":1500},
                             {"CatalogItemID":4,"ManufacturerID":4,"CatalogItemName":"Surface Pro","ItemCatagoryID":1,"BuyCost":2000}]

        @self.app.route('/')
        def index():
            return render_template('index.html', config=self.config)

        @self.app.route('/add_inventoryitem', methods = ['GET','POST'])
        def add_inventoryitem():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to add to db)
                self.inventoryItems.append({"InventoryItemID":len(self.inventoryItems)+1,
                                            "CatalogItemID":request.form.get("CatalogItem"),
                                            "StockQuantity":request.form.get("StockQuantity"),
                                            "ItemSerialNumber":request.form.get("ItemSerialNumber"),
                                            "SellPrice":request.form.get("SellPrice")})
                ## END add to local list
                return render_template('update_inventoryitem.html', config=self.config, inventoryItems=self.inventoryItems, catalogItems=self.catalogItems)
            else:
                return render_template('add_inventoryitem.html', config=self.config, catalogItems=self.catalogItems)
            
        @self.app.route('/add_catalogitem', methods = ['GET','POST'])
        def add_catalogitem():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to add to db)
                self.catalogItems.append({"CatalogItemID":len(self.catalogItems)+1,
                                            "ManufacturerID":request.form.get("Manufacturer"),
                                            "CatalogItemName":request.form.get("CatalogItemName"),
                                            "ItemCatagoryID":request.form.get("ItemCatagory"),
                                            "BuyCost":request.form.get("BuyCost")})
                ## END add to local list
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers, catalogItems=self.catalogItems, catagories=self.catagories)
            else:
                return render_template('add_catalogitem.html', config=self.config, manufacturers=self.manufacturers, catagories=self.catagories)

        @self.app.route('/add_itemcatagory', methods = ['GET','POST'])
        def add_itemcatagory():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to add to db)
                self.catagories.append({"ItemCatagoryID":len(self.catagories)+1,
                                            "ItemCatagoryTitle":request.form.get("ItemCatagoryTitle"),
                                            "ItemCatagoryDescription":request.form.get("ItemCatagoryDescription")})
                ## END add to local list
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catagories)
            else:
                return render_template('add_itemcatagory.html', config=self.config)

        # /\ /\ /\ ADD pages
        # \/ \/ \/ UPDATE pages

        @self.app.route('/update_inventoryitem', methods = ['GET','POST'])
        def update_inventoryitem():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.inventoryItems:
                    if i["InventoryItemID"] == int(request.form.get("inventoryItem")):
                        self.ind = self.inventoryItems.index(i)
                self.inventoryItems[self.ind] |= {"CatalogItemID":request.form.get('CatalogItem')}
                self.inventoryItems[self.ind] |= {"StockQuantity":request.form.get('StockQuantity')}
                self.inventoryItems[self.ind] |= {"ItemSerialNumber":request.form.get('ItemSerialNumber')}
                self.inventoryItems[self.ind] |= {"SellPrice":request.form.get('SellPrice')}
                ## END add to local list
                return render_template('update_inventoryitem.html', config=self.config, inventoryItems=self.inventoryItems, catalogItems=self.catalogItems)
            else:
                return render_template('update_inventoryitem.html', config=self.config, inventoryItems=self.inventoryItems, catalogItems=self.catalogItems)
            
        @self.app.route('/update_catalogitem', methods = ['GET','POST'])
        def update_catalogitem():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.catalogItems:
                    if i["CatalogItemID"] == int(request.form.get("CatalogItem")):
                        self.ind = self.catalogItems.index(i)
                self.catalogItems[self.ind] |= {"ManufacturerID":request.form.get('Manufacturer')}
                self.catalogItems[self.ind] |= {"CatalogItemName":request.form.get('CatalogItemName')}
                self.catalogItems[self.ind] |= {"ItemCatagoryID":request.form.get('ItemCatagory')}
                self.catalogItems[self.ind] |= {"BuyCost":request.form.get('BuyCost')}
                ## END add to local list
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers, catalogItems=self.catalogItems, catagories=self.catagories)
            else:
                return render_template('update_catalogitem.html', config=self.config, manufacturers=self.manufacturers, catalogItems=self.catalogItems, catagories=self.catagories)

        @self.app.route('/update_itemcatagory', methods = ['GET','POST'])
        def update_itemcatagory():
            if request.method == "POST":
                ## BEGIN add to local list (change this to call something to edit data in db)
                for i in self.catagories:
                    if i["ItemCatagoryID"] == int(request.form.get("ItemCatagory")):
                        self.ind = self.catagories.index(i)
                self.catagories[self.ind] |= {"ItemCatagoryTitle":request.form.get('ItemCatagoryTitle')}
                self.catagories[self.ind] |= {"ItemCatagoryDescription":request.form.get('ItemCatagoryDescription')}
                ## END add to local list
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catagories)
            else:
                return render_template('update_itemcatagory.html', config=self.config, catagories=self.catagories)
        

        @self.app.route('/error/<string:e>')
        def error(e):
            return render_template('error.html', error=e)

        if __name__ == "__main__":
            app.run(host="127.0.0.1", debug=False)