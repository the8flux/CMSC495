import configparser

from flask import Flask, render_template, request

################
version = "0.1"
################

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
config.set('systemSettings', 'version', version)

#################
# Testing lists #
#################
customers = ["Steve", "Joe", "Bob", "Sophia"]
users = ["Steve", "Joe", "Bob", "Sophia"]
inventoryItems = ["Phone", "Laptop", "Charger", "Tablet"]
priceAdjustments = ["Black Friday", "Christmas", "Holiday", "25%"]
invoices = ["0001", "0002", "0003", "0004"]
catagories = ["Electronics", "Home", "Food", "Clothing"]
manufacturers = ["Intel", "AMD", "Nvidia", "LG"]
lineItems = ["Macbook Pro", "Galaxy Fold", "100w", "Surface Pro"]
catalogItems = ["Macbook Pro", "Galaxy Fold", "100w", "Surface Pro"]
userTypes = ["Admin", "Customer", "Seller", "Manufacturer"]
addresses = ["123 Main Street", "456 Antoher Road", "789 Something Lane", "010 That Road"]

@app.route('/')
def index():
    return render_template('index.html', config=config)

@app.route('/create', methods = ['POST'])
def create():
    form_data = request.form
    print(form_data) # This data comes from submitting a form
    return render_template('create.html', config=config, form_data=form_data)

@app.route('/add_user')
def add_user():
    return render_template('add_user.html', config=config, customers=customers, addresses=addresses, userTypes=userTypes)

@app.route('/add_customer')
def add_customer():
    return render_template('add_customer.html', config=config, addresses=addresses)

@app.route('/add_invoice')
def add_invoice():
    return render_template('add_invoice.html', config=config, priceAdjustments=priceAdjustments, customers=customers)

@app.route('/add_lineitem')
def add_lineitem():
    return render_template('add_lineitem.html', config=config, invoices=invoices, priceAdjustments=priceAdjustments, customers=customers, inventoryItems=inventoryItems)

@app.route('/add_priceadjustment')
def add_priceadjustment():
    return render_template('add_priceadjustment.html', config=config)

@app.route('/add_inventoryitem')
def add_inventoryitem():
    return render_template('add_inventoryitem.html', config=config, catalogItems=catalogItems)
    
@app.route('/add_catalogitem')
def add_catalogitem():
    return render_template('add_catalogitem.html', config=config, manufacturers=manufacturers, catagories=catagories)

@app.route('/add_itemcatagory')
def add_itemcatagory():
    return render_template('add_itemcatagory.html', config=config)
   
@app.route('/add_usertype')
def add_usertype():
    return render_template('add_usertype.html', config=config)

@app.route('/add_address')
def add_address():
    return render_template('add_address.html', config=config)

@app.route('/add_manufacturer')
def add_manufacturer():
    return render_template('add_manufacturer.html', config=config)

# /\ /\ /\ ADD pages
# \/ \/ \/ UPDATE pages

@app.route('/update_invoice')
def update_invoice():
    return render_template('update_invoice.html', config=config, invoices=invoices, priceAdjustments=priceAdjustments, customers=customers)

@app.route('/update_lineitem')
def update_lineitem():
    return render_template('update_lineitem.html', config=config, invoices=invoices, priceAdjustments=priceAdjustments, customers=customers, inventoryItems=inventoryItems, lineItems=lineItems)

@app.route('/update_priceadjustment')
def update_priceadjustment():
    return render_template('update_priceadjustment.html', config=config, priceAdjustments=priceAdjustments)

@app.route('/update_inventoryitem')
def update_inventoryitem():
    return render_template('update_inventoryitem.html', config=config, inventoryItems=inventoryItems, catalogItems=catalogItems)
    
@app.route('/update_catalogitem')
def update_catalogitem():
    return render_template('update_catalogitem.html', config=config, manufacturers=manufacturers, catalogItems=catalogItems, catagories=catagories)

@app.route('/update_itemcatagory')
def update_itemcatagory():
    return render_template('update_itemcatagory.html', config=config, catagories=catagories)
   
@app.route('/update_usertype')
def update_usertype():
    return render_template('update_usertype.html', config=config, userTypes=userTypes)

@app.route('/update_address')
def update_address():
    return render_template('update_address.html', config=config, addresses=addresses)

@app.route('/update_manufacturer')
def update_manufacturer():
    return render_template('update_manufacturer.html', config=config, manufacturers=manufacturers)

@app.route('/update_customer')
def update_customer():
    return render_template('update_customer.html', config=config, customers=customers, addresses=addresses)

@app.route('/update_user')
def update_user():
    return render_template('update_user.html', config=config, users=users, addresses=addresses, customers=customers, userTypes=userTypes, manufacturers=manufacturers)

@app.route('/error/<string:e>')
def error(e):
    return render_template('error.html', error=e)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=False)