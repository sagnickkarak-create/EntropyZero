import os
import shutil 
from database import Tunnel

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
        os.mkdir(os.path.normpath(os.path.join(path, 'Others')))
        
    def filename_getter(self, path):
        # this method gets the name of the file and the extensions separately from the target folder
        os.chdir(path)
        self.entities = list(set(os.listdir())-set(['Documents', 'Media', 'Programming', 'System & Compressed', 'Others']))
        #Filter out all hidden Mac files immediately(modified for Sree's  Mac)
        self.entities = [entity for entity in self.entities if not entity.startswith('.')]
        
        self.files_dict = {}
        for entity in self.entities :
            file, extension = os.path.splitext(entity)
            self.files_dict[file]=extension

    def destination_path_builder(self, path):
        self.destination_dict = {}
        for file in self.files_dict.keys() :
            target = 'Others'
            extension = self.files_dict.get(file)
            for rule in self.tunnel.rules :
                if rule['EXTENSION'] == extension :
                    target = self.tunnel.rules[self.tunnel.rules.index(rule)]['PATH']
            joined_target = os.path.join(path, target)
            clean_target = os.path.normpath(joined_target)
            self.destination_dict[file] = clean_target

    def mover(self, path):
        for entity in self.entities:
            try :
                file, extension = os.path.splitext(entity)
                source_path = os.path.normpath(os.path.join(path, entity))
                target_path = self.destination_dict[file]              
                shutil.move(source_path, target_path)
                yield entity, target_path
        
            except Exception as e :
                yield "FAILURE", e