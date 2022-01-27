import csv
import json

import xmltodict
import xlrd
from collections import OrderedDict
import pandas as pd
from abc import ABC,abstractmethod


class Interface_Converter(ABC):
    @abstractmethod
    def convertcsv(self):
        pass
    @abstractmethod
    def convertXML(self):
        pass
    @abstractmethod
    def convertxsl(self):
        pass



class Converter(Interface_Converter):
    def convertcsv(self,csvFilePath, jsonFilePath):
        data={}
        with open(csvFilePath, encoding='utf-8') as mycsv:
              csvReader = csv.DictReader(mycsv)
              for rows in csvReader:
                    key = rows['']
                    data[key]=rows
        with open(jsonFilePath,'w', encoding='utf-8') as jsonf:
             jsonf.write(json.dumps(data, indent=4))

    def convertXML(self,xmlfile,jsonFilePath):
        with open(xmlfile) as xml_file:
             data_dict = xmltodict.parse(xml_file.read())
             xml_file.close()
             json_data = json.dumps(data_dict)
             with open(jsonFilePath, "w") as json_file:
                 json_file.write(json_data)
                 json_file.close()

    def convertxsl(self,xslfile,jsonFilePath):
        wb=xlrd.open_workbook(xslfile)
        sh=wb.sheet_by_index(0)
        data_List=[]
        for rownum in range(1,sh.nrows):
            data=OrderedDict()
            row_values=sh.row_values(rownum)
            data['First Name']=row_values[0]
            data['Last Name'] = row_values[1]
            data['Gender'] = row_values[2]
            data['Country'] = row_values[3]
            data['Age'] = row_values[4]
            data['Date'] = row_values[5]
            data['Id'] = row_values[6]



            data_List.append(data)
        j=json.dumps(data_List)
        with open(jsonFilePath,'w') as f:
            f.write(j)

        
csvFilePath = r'databaseCSV.csv'
jsonFilePath = r'pythonJSON.json'
xmlfilepath=r'xmlfilee.xml'
xslfilepath=r'file_example_XLS_10.xls'
    
csvfile=Converter()
xmlfile=Converter()
xslfile=Converter()


csvfile.convertcsv(csvFilePath, jsonFilePath)
# xmlfile.convertXML(xmlfilepath,jsonFilePath)
# xslfile.convertxsl(xslfilepath,jsonFilePath)

# making dataframe 
df = pd.read_csv("databaseCSV.csv") 
   
# output the dataframe
# print(df[df.vote_average==8.7])

x=input('enter title : ')
def getvalue(key,value):
    return df[key==value]
print(getvalue(df.title,x))



    





 







        

     
        
    
        
