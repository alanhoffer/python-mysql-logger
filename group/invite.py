import pymysql
import variables as var


class invite:
    def __init__(self):
        self.id = 0
        self.userid = 0
        self.groupid = 0
        self.senderid = 0
        self.accepted = False
        self.mysql = pymysql.connect(host='localhost', user='root', password='15441109', db='apitool_test')
        
    def send(self,userid,groupid,senderid=0):
        cursor = self.mysql.cursor()
        cursor.execute('SELECT * FROM accounts WHERE id = %s', (userid))
        account = cursor.fetchone()
        
        cursor.execute('SELECT * FROM group WHERE id = %s', (groupid))
        group = cursor.fetchone()
        
        if account and group:
            print(var.INVITE_MESSAGE)
            cursor.execute('INSERT INTO invite (userid,groupid,accepted) VALUES (%s,%s,%s)', (userid,groupid,False))
            cursor.commit()
            return True
        else:
            print(var.INVITE_ERROR)
    
    def accept(self,id):
        cursor = self.mysql.cursor()
        cursor.execute('SELECT * FROM invite WHERE id = %s', (id))
        invite = cursor.fetchone()
        if invite:
            cursor.execute('UPDATE invite SET accepted = %s WHERE id=%s', (True,id))
            cursor.commit()
            print('Invite accepted')
            return True
        else:
            print('Invite does not exist')
            return False
    
    def decline(self,id):
        cursor = self.mysql.cursor()
        cursor.execute('SELECT * FROM invite WHERE id = %s', (id))
        invite = cursor.fetchone()
        if invite:
            cursor.execute('DELETE FROM invite WHERE id=%s', (id))
            cursor.commit()
            print('Invite declined')
            return True
        else:
            print('Invite does not exist')
            return False