/*

            OMEGA Team
            UMGC CMSC 495

            Build Database Tables
*/

BEGIN;

/* Drop_ tables_ to_ rebuild_ */
DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Customers;
DROP TABLE IF EXISTS Manufacturers;
DROP TABLE IF EXISTS Address;
DROP TABLE IF EXISTS UserType;
DROP TABLE IF EXISTS ItemCategories;
DROP TABLE IF EXISTS CatalogItems;
DROP TABLE IF EXISTS InventoryItems;
DROP TABLE IF EXISTS PriceAdjustment;
DROP TABLE IF EXISTS LineItems;
DROP TABLE IF EXISTS Invoices;


--*******************************************************************
/*
*
*   Building Tables_
*
*
*/


CREATE TABLE ItemCategories (
    ItemCategoryID INTEGER PRIMARY KEY,
    ItemCategoryTitle TEXT,
    ItemCategoryDescription TEXT
);

CREATE TABLE PriceAdjustment (
  PriceAdjustmentID INTEGER PRIMARY KEY,
  Title TEXT,
  ReasonDescription TEXT,
  IsFixed BOOLEAN,
  FixedAmount DECIMAL(10,2),
  IsPercent BOOLEAN,
  Percent INTEGER
);


-- Creating user_ type_ Table_
CREATE TABLE UserType (
  UserTypeID INTEGER PRIMARY KEY,
  Description TEXT
);

-- Creating CataLogItems Table_
CREATE TABLE CatalogItems (
  CatalogItemID INTEGER PRIMARY KEY,
  ManufacturerID INTEGER,
  CatalogItemName TEXT,
  ItemCategoryID INTEGER,
  BuyCost DECIMAL(10,2),
  FOREIGN KEY (ManufacturerID) REFERENCES Manufacturer(ManufacturerID),
  FOREIGN KEY (ItemCategoryID) REFERENCES ItemCategories(ItemCategoryID)
);

-- Creating ItemInventory Table_
CREATE TABLE InventoryItems (
  InventoryItemID INTEGER PRIMARY KEY,
  CatalogItemID INTEGER,
  StockQuantity INTEGER,
  ItemSerialNumber TEXT,
  SellPrice DECIMAL(10,2),
  FOREIGN KEY (CatalogItemID) REFERENCES Catalog(CatalogItemID)
);


-- Creating Address Table_
CREATE TABLE Address (
  AddressID INTEGER PRIMARY KEY,
  StreetAddress TEXT NOT NULL DEFAULT 'None',
  City TEXT NOT NULL DEFAULT 'None',
  State TEXT NOT NULL DEFAULT 'None' ,
  Country TEXT NOT NULL DEFAULT 'None' ,
  PostalCode TEXT NOT NULL DEFAULT 'None'
);

-- Creating Manufacturer Table
CREATE TABLE Manufacturers (
  ManufacturerID INTEGER PRIMARY KEY,
  ManufacturerName TEXT NOT NULL,
  ManufacturerDescription TEXT,
  AddressID INTEGER,
  FOREIGN KEY(AddressID) REFERENCES Address(AddressID)
);

-- Creating Customer Table
CREATE TABLE Customers (
  CustomerID INTEGER PRIMARY KEY,
  AddressID INTEGER,
  CustomerName TEXT NOT NULL,
  FOREIGN KEY (AddressID) REFERENCES Address(AddressID)
);

CREATE TABLE Users (
  UserID INTEGER PRIMARY KEY,
  AddressID INTEGER DEFAULT 0 REFERENCES Address(AddressID) ON DELETE CASCADE,
  CustomerID INTEGER DEFAULT 0 REFERENCES Customer(CustomerID),
  ManufacturerID INTEGER DEFAULT 0 REFERENCES Manufacturer(ManufacturerID),
  FirstName TEXT NOT NULL,
  LastName TEXT NOT NULL,
  Telephone TEXT NOT NULL,
  Email TEXT NOT NULL,
  UserTypeID INTEGER REFERENCES UserType(UserTypeID),
  UserLogon TEXT NOT NULL,
  UserPasswordHash TEXT DEFAULT 'password'
);

CREATE TABLE LineItems (
  LineItemID INTEGER PRIMARY KEY,
  InvoiceID INTEGER,
  InventoryItemID INTEGER,
  CostAdjustmentID INTEGER,
  SellPrice DECIMAL(10,2),
  Quantity INTEGER,
  FOREIGN KEY (InvoiceID) REFERENCES Invoices(InvoiceID),
  FOREIGN KEY (InventoryItemID) REFERENCES Inventory(InventoryItemID),
  FOREIGN KEY (CostAdjustmentID) REFERENCES PriceAdjustment(PriceAdjustmentID)
);


CREATE TABLE Invoices (
  InvoiceID INTEGER PRIMARY KEY,
  CustomerID INTEGER,
  CostAdjustmentID INTEGER,
  DateInvoiced DATE,
  DateInvoiceDue DATE,
  InvoiceSubTotal DECIMAL(10,2),
  TaxPercent INTEGER,
  TaxAmount DECIMAL(10,2),
  InvoiceTotalDue DECIMAL(10,2),
  FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
  FOREIGN KEY (CostAdjustmentID) REFERENCES PriceAdjustment(PriceAdjustmentID)
);






BEGIN;
/*
*
* Creating Basic Views
*
*
*/



-- List Customer ID and Customer Name
DROP VIEW IF EXISTS VIEW_GUICustomers;
CREATE VIEW VIEW_GUICustomers AS
    SELECT Customers.CustomerID,
           Customers.CustomerName
      FROM Customers;

-- List Manufacturers ID and Manufactuers NAme
DROP VIEW IF EXISTS VIEW_GUIManufacturers;
CREATE VIEW VIEW_GUIManufacturers AS
    SELECT Manufacturers.ManufacturerID,
           Manufacturers.ManufacturerName
      FROM Manufacturers;


-- Creating Manufacturer Catalog Items View
DROP VIEW IF EXISTS VIEW_ManufacturersCatalogItems;
CREATE VIEW VIEW_ManufacturersCatalogItems AS
    SELECT Manufacturers.ManufacturerID,
            Manufacturers.ManufacturerName,
           CatalogItems.CatalogItemName,
           CatalogItems.BuyCost
      FROM CatalogItems
           INNER JOIN
           Manufacturers ON Manufacturers.ManufacturerID = CatalogItems.ManufacturerID
     ORDER BY Manufacturers.ManufacturerName ASC;


-- Creating Manufacturer Address View

DROP VIEW IF EXISTS VIEW_ManufacturersAddress;
CREATE VIEW VIEW_ManufacturersAddress AS
    SELECT Manufacturers.ManufacturerID,
           Manufacturers.ManufacturerName,
           Manufacturers.ManufacturerDescription,
           Address.StreetAddress,
           Address.City,
           Address.State,
           Address.PostalCode
      FROM Manufacturers
           INNER JOIN
           Address ON Manufacturers.AddressID = Address.AddressID;


DROP VIEW IF EXISTS VIEW_CustomersAddress;
CREATE VIEW VIEW_CustomersAddress AS
    SELECT Customers.CustomerID,
           Customers.CustomerName,
           Address.StreetAddress,
           Address.City,
           Address.State,
           Address.PostalCode,
           Address.Country
      FROM Customers
           INNER JOIN
           Address ON Customers.AddressID = Address.AddressID;


DROP VIEW IF EXISTS VIEW_UserAdmins;
CREATE VIEW VIEW_UserAdmins AS
    SELECT
            Users.UserID,
            Users.FirstName,
           Users.LastName,
           Users.Email,
           Users.Telephone,
           Users.UserLogon,
           UserType.Description
      FROM Users
           INNER JOIN
           UserType ON USerType.UserTypeID = Users.UserTypeID
     WHERE UserType.UserTypeID = 1
     ORDER BY Users.LastName ASC, Users.FirstName ASC;




DROP VIEW IF EXISTS VIEW_UserEmployees;

CREATE VIEW VIEW_UserEmployees AS
    SELECT Users.UserID,
            Users.FirstName,
           Users.LastName,
           Users.Email,
           Users.Telephone,
           Users.UserLogon,
           UserType.Description
      FROM Users
           INNER JOIN
           UserType ON USerType.UserTypeID = Users.UserTypeID
     WHERE UserType.UserTypeID = 2
     ORDER BY Users.LastName ASC, Users.FirstName ASC;



DROP VIEW IF EXISTS VIEW_UserManufacturers;
CREATE VIEW VIEW_UserManufacturers AS
    SELECT
            Users.UserID,
            Users.FirstName,
           Users.LastName,
           Users.Email,
           Users.Telephone,
           Users.UserLogon,
           UserType.Description,
           Manufacturers.ManufacturerName
      FROM Users
           INNER JOIN
           UserType ON USerType.UserTypeID = Users.UserTypeID
           LEFT JOIN
           Manufacturers ON Manufacturers.ManufacturerID = Users.ManufacturerID
     WHERE UserType.UserTypeID = 4
     ORDER BY Manufacturers.ManufacturerName ASC;



DROP VIEW IF EXISTS VIEW_ManufacturersUser;
CREATE VIEW VIEW_ManufacturersUser AS
    SELECT  Manufacturers.ManufacturerID,
            Manufacturers.ManufacturerName,
           Users.FirstName,
           Users.LastName
      FROM Manufacturers
           LEFT JOIN
           Users ON Manufacturers.ManufacturerID = Users.ManufacturerID
     ORDER BY Manufacturers.ManufacturerName ASC;



DROP VIEW IF EXISTS VIEW_ManufacturersCatalogItems;
CREATE VIEW VIEW_ManufacturersCatalogItems AS
    SELECT
           Manufacturers.ManufacturerID,
           Manufacturers.ManufacturerName,
           CatalogItems.CatalogItemName,
           CatalogItems.BuyCost,
           ItemCategories.ItemCategoryTitle,
           ItemCategories.ItemCategoryDescription
      FROM CatalogItems
           INNER JOIN
           Manufacturers ON Manufacturers.ManufacturerID = CatalogItems.ManufacturerID
           INNER JOIN
           ItemCategories ON ItemCategories.ItemCategoryID = CatalogItems.ItemCategoryID
     ORDER BY Manufacturers.ManufacturerName ASC,
              CatalogItems.CatalogItemName;


DROP VIEW IF EXISTS VIEW_UserCustomers;
CREATE VIEW VIEW_UserCustomers AS
    SELECT
            Users.UserID,
            Users.FirstName,
           Users.LastName,
           Users.Email,
           Users.Telephone,
           Users.UserLogon,
           UserType.Description,
           Customers.CustomerName
      FROM Users
           INNER JOIN
           UserType ON USerType.UserTypeID = Users.UserTypeID
           LEFT JOIN
           Customers ON Customers.CustomerID = Users.CustomerID
     WHERE UserType.UserTypeID = 3
     ORDER BY Users.LastName ASC, Users.FirstName ASC;

COMMIT;