import os
import shutil 
from database import Tunnel
from sorter_screen import Sorter_Screen 

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

    def filename_getter(self, path):
        # this method gets the name of the file and the extensions separately from the target folder
        os.chdir(path)
        self.entities = list(set(os.listdir())-set(['Documents', 'Media', 'Programming', 'System & Compressed']))
        self.files_dict = {}
        for entity in self.entities :
            file, extension = entity.split('.')[0], '.'+entity.split('.')[1]
            self.files_dict[file]=extension

    def destination_path_builder(self, path):
        self.destination_dict = {}
        for file in self.files_dict.keys() :
            extension = self.files_dict.get(file)
            for rule in self.tunnel.rules :
                if rule['EXTENSION'] == extension :
                    target = self.tunnel.rules[self.tunnel.rules.index(rule)]['PATH']
            joined_target = os.path.join(path, target)
            clean_target = os.path.normpath(joined_target)
            self.destination_dict[file] = clean_target

    def mover(self, path):
        try :
            source_path = []
            for file in self.entities :
                source_path.append(os.path.normpath(os.path.join(path, file)))
            target_path = []
            for path in self.destination_dict.values() :
                target_path.append(os.path.normpath(path+'\\'))
            for i in range(len(source_path)):
                shutil.move(source_path[i], target_path[i])
                yield self.entities[i], target_path[i]
        
        except Exception as e :
            yield "FAILURE", e