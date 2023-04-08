from DB import DBSelect
from DB import DBInfo
from DB import Reports

if __name__ == '__main__':
    # throwAway = DBSelect.DBSelect("./databases/test_db3.db")
    # throwAway = DBInfo.DBInfo("./databases/test_db3.db")
    throwAway = Reports.Reports("./databases/test_db3.db")
    print(throwAway.VIEW_UserCusomers())


