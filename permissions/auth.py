import pymysql
from modules.logger import log
import variables as var
import modules.emails as emails



class auth:
    def __init__(self,session, log):
        self.session = session
        self.log = log
        self.mysql = pymysql.connect(host='localhost', user='root', password='15441109', db='apitool_test')
        self.cursor = self.mysql.cursor()

    
    def login(self,username, password):
        if self.session.getSession():
            print(var.LOGIN_EXISTS)
            return False
        else:
            if self.mysql:
                self.cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username,password))
                account = self.cursor.fetchone()
                if account:
                    self.session.setSession(account[0])
                    self.log.info(auth.login.__qualname__, var.LOGIN_MESSAGE)
                else:
                    print(var.LOGIN_ERROR)
            return True 
                
    
    def logout(self):
        if self.session.getSession():
            self.session.delSession()
            self.log.info(auth.logout.__qualname__, var.LOGOUT_MESSAGE)
            return True
        else:
            print(var.LOGIN_NOTEXISTS)
            
    def create_user(self,username, password, email,name,lastname,city,permissions='User'):
        if self.session.getSession():
            print(var.LOGIN_EXISTS)
            return False
        else:
            if self.mysql:
                print(var.DB_CONNECTED)
                self.cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
                account = self.cursor.fetchone()
                if account:
                    print(var.ACCOUNT_EXISTS)
                else:
                    self.cursor.execute('INSERT INTO accounts (username, password, email, name, lastname, city, permissions) VALUES (%s, %s, %s,%s, %s, %s, %s)',
                                   (username, password, email, name, lastname, city, permissions))
                    self.mysql.commit()
                    self.log.info(auth.create_user.__qualname__, var.ACCOUNT_MESSAGE)
            return True
        
    def forgot_password(self,email):
        if self.mysql:
            cursor = self.mysql.cursor()
            print(var.DB_CONNECTED)
            print(var.DB_SEARCH, email)
            cursor.execute('SELECT * FROM accounts WHERE email = %s', (email,))
            account = cursor.fetchone()
            if account:
                print(var.ACCOUNT_EXISTS)
                emails.sendmail(account[3], 'Your password is: ' + account[2])
                self.log.info(auth.forgot_password.__qualname__, var.EMAIL_FORGOT)
            else:
                print(var.ACCOUNT_NOTEXISTS)
            return True
        else:
            return False

    # def delete_user(self,username):
    #     cursor = self.mysql.cursor()
    #     cursor.execute('SELECT * FROM accounts WHERE username = %s AND permissions = %s', (username, 'Admin'))
    #     account = cursor.fetchone()
    #     if account:
    #         if self.mysql:
    #             cursor = self.mysql.cursor()
    #             print('Connected to db')
    #             print('Deleting Account ', username)
    #             cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
    #             account = cursor.fetchone()
    #             if account:
    #                 print('Account found')
    #                 cursor.execute('DELETE FROM accounts WHERE username = %s', (username,))
    #                 self.mysql.commit()
    #                 print('User deleted')
    #         return True
    #     else:
    #         print('You dont have permissions to delete this user')
    #         return False    
        