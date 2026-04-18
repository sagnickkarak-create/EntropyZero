import mysql.connector as mysql

class Tunnel:
    def __init__(self):
        try:
            self.db=mysql.connect(host='localhost',
                    user='root',
                    password='12345',
                    database='entropyzero')
            self.cursor = self.db.cursor()
        except Exception as error :
            print(f'CONNECTION FAILED : {error}')
            raise error
    
    def add_user(self, username, password, path):
        try:
            self.cursor.execute('insert into users(username, password, target_root) values(%s,%s,%s);', (username, password, path))
            self.db.commit()
        except Exception as error:
            raise error

    def check_user(self, username, password):
        try:
            query = 'select password from users where username = %s'
            self.cursor.execute(query, (username,))
            result=self.cursor.fetchone()
            if result:
                if result[0] == password:
                    return True
                else :
                    return False
            else :
                return False
        except Exception as error:
            raise error
        
    def close_connection(self):
        if self.cursor : # checks if it exists
            self.cursor.close()
        if self.db : # checks if it exists
            self.db.close()
            


