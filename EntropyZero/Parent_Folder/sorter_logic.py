import os
import shutil 
from database import Tunnel

class FolderBuilder:
    def __init__(self, path):
        self.path = path
        self.tunnel = Tunnel()
    
    def info_getter(self):
        self.tunnel.fetch_rules()
        self.rules = self.tunnel.rules
        self.folders = []
        self.extensions = []
        for i in self.rules:
            self.folders.append(i['PATH'])
            self.extensions.append(i['EXTENSION'])
        
    def builder(self):
        os.chdir(path)
        for i in self.folders:
            os.makedirs(i)
        print("DONE!")

    def mover(self):
        pass

if __name__=='__main__':
    path = r'G:/TEST/' # TEST is a temporary folder that I made for testing
    FB = FolderBuilder(path)
    FB.info_getter()
    FB.builder()