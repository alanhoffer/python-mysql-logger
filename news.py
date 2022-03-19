from numpy import delete
import pymysql

class new:
    def __init__(self,session):
        self.session = session
        self.mysql = pymysql.connect(host='localhost', user='root', password='15441109', db='apitool_test')
        
    #create function to make new news with title and content and image and date and author
    def create(self,title,content,image,date,author):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM news WHERE title = %s', (title))
            news = cursor.fetchone()
            
            if news:
                print('News already exists pick another title')
            else:
                print('Creating news ', title)
                cursor = self.mysql.cursor()
                cursor.execute('INSERT INTO news (title, content, image, date, author) VALUES (%s,%s,%s,%s,%s)', (title,content,image,date,author))
                self.mysql.commit()
                print('News created')
    
    def delete(self,id):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM news WHERE id = %s', (id))
            news = cursor.fetchone()
            
            if news:
                print('Deleting news ', id)
                cursor = self.mysql.cursor()
                cursor.execute('DELETE FROM news WHERE id=%s', (id))
                self.mysql.commit()
                print('News deleted')
            else:
                print('News does not exist')
                
    def getallnews(self):
        if self.mysql:
            cursor = self.mysql.cursor()
            cursor.execute('SELECT * FROM news')
            news = cursor.fetchall()
            
            if news:
                print('Getting all news')
                print('News: ', news)
            else:
                print('No news')