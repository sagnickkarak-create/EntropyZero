import os
import shutil 
from database import Tunnel

class FolderBuilder:
    def __init__(self, path):
        self.path = path
        self.tunnel = Tunnel()
    
    def builder(self):
        self.tunnel.fetch_rules()
        self.rules = self.tunnel.rules
        for i in self.rules :
            print(i)

if __name__=='__main__':
    path = r'C:\Users\skull\Downloads'
    FB = FolderBuilder(path)
    FB.builder()
