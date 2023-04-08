import random



def CreateCatalogItems():
    random.seed();
    CatalogItemID = 1
    output = "INSERT INTO CatalogItem (CatalogItemID, ManufacturerID, CatalogItemName, ItemCategoryID, BuyCost) VALUES "
    for ManufacturerID in range(1, 51):
        for item in range(1, 51):
            formatter = "({},{},'{}',{},{}),\n"
            buy_cost = str(round(random.uniform(000.33, 999.99),2))


            catalog_item_name = "CATID"+ str(CatalogItemID) +  "_MANID" + str(ManufacturerID)+"_ITEM_#"+str(item)
            item_category_id = random.randint(1, 40)
            more = formatter.format(CatalogItemID, ManufacturerID, catalog_item_name, item_category_id, buy_cost)
            output = output + more
            CatalogItemID = 1 + CatalogItemID
    print(output)


if __name__ == '__main__':
    CreateCatalogItems()