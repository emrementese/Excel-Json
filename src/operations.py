# -*- coding: utf-8 -*-
'''
Created by Emre MENTESE on 10/08/2022
Coding with Python.
'''

import pandas
import warnings
from typing import Union
from datetime import datetime
import json
import os

class FileOperations:
    warnings.simplefilter("ignore")

    def __init__(self):
        self.classname = "FileOperations Pointer"

    def __str__(self) -> str:
       return self.classname

    def write_log(self,text,space):
        '''
        * Logging for erros.
        '''
        with open("logs/error.log","a",encoding="UTF-8") as file:
            log = f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')} - {space} - " + text
            file.write(log + "\n")
        return True

    def read_excel(self,path:str) -> Union[bool,dict]:
        '''
        * Read your excel file.
        - Input
            * File Path (String)
        - Outputs
            * Excel data --> Python dictionary
        '''
        try:
            data = []
            excel_file = pandas.read_excel(path,engine="openpyxl")
            #print(excel_file.corr())
            data_count = len(excel_file[excel_file.columns[0]].values)
            data_dict = excel_file[excel_file.columns].to_dict()
            for lines in range(0,data_count):
                line = {}
                for columns in excel_file.columns:
                    line[columns] = data_dict[columns][lines]
                
                data.append(line)
            return data

        except Exception as e:
            self.write_log(text = str(e) ,space = "Read Excel")
            return False

    def write_excel(self,path:str,data,sheet_name:str) -> bool:
        '''
        * Write your data in json file.
        - Input
            * Data (read document for type)
            * sheet_name String (excel project name)
            * File Path (String)
        - Outputs
            * if functions is a sucess, return True
        '''
        try:
            df = pandas.DataFrame(data)
            excel_file = pandas.ExcelWriter(path,engine="xlsxwriter")
            df.to_excel(excel_file, sheet_name=sheet_name, index=False)
            excel_file.save()
            return True
        except Exception as e:
            self.write_log(text = str(e) ,space = "Write Excel")
            return False
    
    def write_json(self,path:str,data) -> bool:
        '''
        * Write your data in json file.
        - Input
            * Data (any)
            * File Path (String)
        - Outputs
            * if functions is a sucess, return True
        '''
        try:
            with open(path,"w",encoding="UTF-8") as file:
                file.write(json.dumps(data))
            return True
        except Exception as e:
            self.write_log(text = str(e) ,space = "Write Json")
            return False

    def read_json(self,path:str) -> dict:
        '''
        * Read your data in json file.
        - Input
            * File Path (String)
        - Outputs
            * readed data: Python dictionary
        '''
        try:
            with open(path,"r",encoding="UTF-8") as file:
                data = file.read()
                return json.loads(data)
        except Exception as e:
            self.write_log(text = str(e) ,space = "Read Json")
            return False

    def create_file(self,path:str) -> bool:
        '''
        * Create a file.
        - Input
            * File Path (String)
        '''
        with open(path,"x") as file:
            pass

    def create_folder(self,path:str) -> bool:
        '''
        * Create a folder.
        - Input
            * Folder Path (String)
        '''
        os.system(f"mkdir {path}")
