import pymysql

class group:
    def __init__(self,session):
        self.session = session
        self.id = None
        self.name = None
        self.roll = None
        self.mysql = pymysql.connect(host='localhost', user='root', password='15441109', db='apitool_test')
        
    
    def create(self,name):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM apigroups WHERE name = %s', (name))
            group = cursor.fetchone()
            cursor.execute('SELECT * FROM apigroups WHERE memberid = %s', (self.session.getSession()))
            member = cursor.fetchone()
            
            if member:
                print('You already have group')
            elif group:
                print('Group already exists pick another name')
            else:
                print('Creating group ', name)
                cursor = self.mysql.cursor()
                cursor.execute('INSERT INTO apigroups (name, memberid, roll) VALUES (%s,%s,%s)', (name,self.session.getSession(),'leader'))
                self.mysql.commit()
                print('Group created')
                
    def delete(self,id):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM apigroup WHERE id = %s', (id))
            group = cursor.fetchone()
            
            if group:
                print('Deleting group ', id)
                cursor = self.mysql.cursor()
                cursor.execute('DELETE FROM apigroup WHERE id=%s', (id))
                self.mysql.commit()
                print('Group deleted')
            else:
                print('Group does not exist')
        
    def getmembers(self,id):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM apigroups WHERE id = %s', (id))
            group = cursor.fetchone()
            
            if group:
                print('Getting members of group ', id)
                cursor = self.mysql.cursor()
                cursor.execute('SELECT * FROM apigroups WHERE id = %s', (id))
                group = cursor.fetchone()
                print('Group members: ', group)
            else:
                print('Group does not exist')