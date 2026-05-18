import os
import shutil 
from database import Tunnel
from login_screen import Login_Screen

class Logic:
    def __init__(self, path, current_user):
        self.path = path
        self.tunnel = Tunnel()
        self.current_user = current_user
    
    def info_getter(self):
        # this method will fetch the rules and the target path from the database and store them in the instance variables
        self.tunnel.fetch_rules()
        self.rules = self.tunnel.rules
        self.folders = []
        self.extensions = []
        for i in self.rules:
            self.folders.append(i['PATH'])
            self.extensions.append(i['EXTENSION'])
        
    def builder(self, path):
        os.chdir(path)
        for i in self.folders:
            os.makedirs(i)
        print("DONE!")

    def filename_getter(self):
        pass

    def mover(self):
        pass