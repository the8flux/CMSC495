# CMSC 495 Project
#
# author: Glenn Phillips
# Date:   Apr 18, 2023
#
# Scope:
'''

'''

import sys
import json
import csv
import bcrypt
from flask import Flask
from flask import redirect
from flask import request
from flask import session
from datetime import datetime
from datetime import timedelta
from FrontEnd import CSSLoader

user_info = {}
user_name = ''
user_data = {}


class WebApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.css = CSSLoader.CSSLoader().get_css()

        def loadUserDB():
            ''' Loads user DB from json file '''
            userDB = {}
            try:
                with open('./static/user.dat', 'r') as fh:
                    # fileData = fh.read().split()
                    userDB = json.load(fh)
            except:
                print('No user db present, Generating Test Users...')
                with open('static/user.dat', 'w') as fh:
                    testUsers = [['gphillips1', hashValue('test1111'), 'false', '0'],
                                 ['gphillips2', hashValue('test2222'), 'false', '0'],
                                 ['gphillips3', hashValue('test3333'), 'false', '0'],
                                 ['gphillips4', hashValue('test4444'), 'false', '0']]
                    for line in testUsers:
                        (user, hPword, timeout, timeoutCount) = line
                        userDB[user] = {'hPword': hPword,
                                        'timeout': timeout,
                                        'timeoutCount': timeoutCount}
                    json.dump(userDB, fh, sort_keys=True, indent=4)
                userDB = loadUserDB()
            return userDB

        def saveUserDB(userDB):
            ''' save userDB to file '''
            status = False;
            try:
                with open('static/user.dat', 'w') as fh:
                    json.dump(userDB, fh, sort_keys=True, indent=4)
                status = True;
            except:
                print('Db Save error.')

            return status

        def addUser(userInfo):
            ''' Add New User [Future]'''
            pass

        def isAccountLocked(user):
            userDB = loadUserDB()
            timeoutCount = userDB[user]['timeoutCount']
            timeout = userDB[user]['timeout']

            if (int(timeoutCount) > 15) and isAccountTimeLocked(user, timeout):
                print('Account Locked:#{}'.format(timeoutCount))
                return True
            else:
                return False

        def isAccountTimeLocked(user, timeout, timeLockSec=300):
            nowDateTime = datetime.now()
            timeoutDateTime = datetime.strptime(timeout, '%Y-%m-%dT%H:%M:%S.%f')
            timeDelta = (nowDateTime - timeoutDateTime)
            timeLock = timedelta(seconds=300)
            print(timeDelta, timeLock)
            if timeDelta < timeLock:
                print('Account Locked:T{}'.format(timeDelta))
                return True
            else:
                return False

        def unlockAccount(user):
            ''' unlock user account '''
            userDB = loadUserDB()
            userDB[user]['timeout'] = 'false'
            userDB[user]['timeoutCount'] = '0'
            saveUserDB(userDB)

        def updateUserNewPassword(user, password):
            ''' Update new password '''
            userDB = loadUserDB()
            userDB[user]['hPword'] = hashValue(password)
            saveUserDB(userDB)

        def updateUserInvalidPassword(user):
            ''' Invalid password signal in user account '''
            userDB = loadUserDB()
            userDB[user]['timeout'] = datetime.now().isoformat()
            userDB[user]['timeoutCount'] = str(int(userDB[user]['timeoutCount']) + 1)
            saveUserDB(userDB)

        def isValidUser(user):
            ''' Finds if User is in User DB File '''
            userDB = loadUserDB()
            return (user in userDB.keys())

        def getValidUser(user):
            ''' Gets Dict of user '''
            userDB = loadUserDB()
            return userDB[user]

        def hashValue(value):
            ''' salt my hash '''
            return (bcrypt.hashpw(value.encode(), bcrypt.gensalt())).decode('utf8')

        def isPasswordValid(password, hPword):
            ''' Are you who you say you are? '''
            return bcrypt.checkpw(password.encode(), hPword.encode())

        def isValidPasswordLength(password, MINCHAR=8, MAXCHAR=64):
            ''' Pass word lenth checker '''
            status = False
            if (len(password) >= MINCHAR) and (len(password) <= MAXCHAR):
                status = True
            return status

        # def isCommonPassword(value):
        #     ''' Find if value a common password '''
        #     passwords = ''
        #     with open('static/commonpassword.txt', 'r') as fh:
        #         passwords = fh.read().splitlines()
        #     return (value in passwords)

        def send2Logger(datetimeVar, IPVar, msgVar):
            ''' Log Some event '''
            with open('static/logger.out.txt', 'a', newline='') as fh:
                writer = csv.writer(fh)
                writer.writerow([datetimeVar, IPVar, msgVar])

        def presentLogonPage(html5CodeBody=''):
            ''' User Login page '''
            pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
            html5 = '''
            <!DOCTYPE html>
            <html>
              <head>
                <title>Omega Inventory System</title>
                <style>{}</style>
              </head>
              <body>
                <div class="view-div">
                  <h2 class="color-1">Omega Inventory System</h2>
                  <form action='/' method="POST">
                    <table>
                      <tr>
                        <th class="color-2" colspan="2">Login</th>
                      </tr>
                      <tr>
                        <td>Username:</td>
                        <td><input type=text name='usrName'></td>
                      </tr>
                      <tr>
                        <td>Password:</td>
                        <td>    <input type=password placeholder="********" 
                                pattern="{}" title="8-64 character password" name='usrPwd'>
                                </td>
                      </tr>
                      <tr>
                        <td colspan="2"><input type='submit' class='submit' name='exeLogon' value='Submit'></td>
                      </tr>
                    </table>
                  </form>
                  {}
                </div>
              </body>
            </html> 
             '''.format(self.css, pattern, html5CodeBody)
            return html5

        def presentPasswordUpdatePage(html5CodeBody=''):
            global user_name, user_info, user_data
            pattern = r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$'
            html5 = '''
            <!DOCTYPE html>
            <html>
            <head>
            <title>Update Password</title>
            <style>{}</style>
            </head>
            <body>
            <div class="view-div">
            <h2 class="color-1">{} Update Password</h2>
            <form action='/update/' method='POST'>
        
            <label>New Password<label><br>
            <input type=password placeholder="********" pattern="{}" 
                title="8-64 character password" name='usrPwd1'>
            <br>
            <label>Retype New Password</label><br>
            <input type=password placeholder="********" pattern="{}" 
                title="8-64 character password" name='usrPwd2'>
        
            <input type=hidden name='usrName' value='{}'>
        
            <input type='submit' class='submit' name='updatePwd' value='Update'>
            </form><br>
            {}
            </div>
            <div class="view-div">{}
            </div>
            </body>
            </html>
            '''.format(self.css ,user_name, pattern, pattern, user_name, html5CodeBody, self.div)
            return html5

        @self.app.route('/', methods=['POST', 'GET'])
        def projectIndex():
            global user_name, user_info, user_data
            msg = ''
            passwordResult = False
            try:
                if request.method == 'POST':
                    postData = request.form
                    for key in postData:
                        print(f'form {key} {postData[key]}')

                    userIP = request.environ['REMOTE_ADDR']
                    usrName = request.form.get('usrName')
                    now = datetime.now().isoformat()
                    # Start Page Routing
                    # User not found
                    if not isValidUser(usrName):
                        msg = '<br> User Not found, {}.'.format(usrName)
                        now = datetime.now().isoformat()
                        send2Logger(now, userIP, 'Invalid User,{}'.format(usrName))
                        return presentLogonPage(msg)
                    else:
                        userData = getValidUser(usrName)
                        user_info = userData
                        user_name = usrName
                    # User Locked out
                    if isAccountLocked(usrName):
                        print('{} Account is locked.'.format(usrName))
                        msg = '<br>{} User Account Locked.'.format(usrName)
                        return presentLogonPage(msg)

                    usrPass = request.form.get('usrPwd')
                    passwordResult = isPasswordValid(usrPass, userData['hPword'])
                    # Invalid Logon
                    if not passwordResult:
                        msg = '<br>{} Invalid Password'.format(usrName)
                        now = datetime.now().isoformat()
                        send2Logger(now, userIP, 'Invalid Password,{}'.format(usrName))
                        updateUserInvalidPassword(usrName)
                        return presentLogonPage(msg)

                    if passwordResult:
                        unlockAccount(usrName)
                        return redirect('/usr/')
            except Exception as e:
                # ignore exception when in production
                print(e, sys.exc_info(), '---')
                # pass
            return presentLogonPage()

        @self.app.route('/usr/')
        def presentSucessLogonPage(msg=''):
            global user_name
            html5 = '''
            <!DOCTYPE html>
            <html>
            <head>
            <title>Logon</title>
            <style>{}</style>
            </head>
            <body>
            <div class="view-div">
            <h2 class="color-1">Main Menu</h2>
            <label><u>{}</u> is logged in.<label><hr>
            <a href='/log'>View Access Log</a><br>
            <a href='/update'>Reset Password for {}</a><br>
            <a href='/logoff'>Log off as {}</a><br>
            <br>{}
            </div>
            </body>
            </html> 
            '''.format(self.css, user_name, user_name, user_name, msg)
            return html5

        @self.app.route('/logoff/')
        def projectLogoff():
            ''' Log off user '''
            global user_data, user_info, user_name
            user_data = None
            user_info = None
            user_name = None
            return redirect('/')

        @self.app.route('/update/', methods=['POST', 'GET'])
        def projectUpdate():
            msg = ''
            try:
                if request.method == 'GET':
                    return presentPasswordUpdatePage()
                if request.method == 'POST':
                    validPW = True
                    msg = ''
                    usrName = request.form.get('usrName')
                    usrPass1 = request.form.get('usrPwd1')
                    usrPass2 = request.form.get('usrPwd2')

                    if not (usrPass1 == usrPass2):
                        msg += "<br>Error: User Entered Password Mismatch"
                        validPW = False

                    if not isValidPasswordLength(usrPass1):
                        msg += "<br>Error: Password must be 8 - 64 Characters."
                        validPW = False

                    # if isCommonPassword(usrPass1):
                    #     msg += "<br>Error: Password to common to use."
                    #     validPW = False

                    if validPW:
                        updateUserNewPassword(usrName, usrPass1)
                        return presentSucessLogonPage('Password Updated.')
                    else:
                        msg += "<br> Please try again."
                        return presentPasswordUpdatePage(msg)
            except Exception as e:
                # ignore exception when in production
                print(e, sys.exc_info(), '---')
                # pass

            return presentSucessLogonPage('Error .')

        @self.app.route('/Test/', methods=['POST'])
        def projectTestIndex():
            user = 'gphillips3'
            userData = getValidUser('gphillips3')
            print(userData)
            password = 'test3'
            passwordResult = isPasswordValid(password, userData['hPword'])
            myReply = ' {} \n{} \n'.format(user, passwordResult)
            return myReply




