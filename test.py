import csv
import json
from abc import ABC, abstractmethod
from collections import OrderedDict
import distutils
from distutils import util
import pandas as pd
from sqlalchemy import column, null
import xlrd
import xmltodict

#make interface The general form of the Classes
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


 # inherite interface and implement methods 
class Converter(Interface_Converter):
    #method convertcsv to json 
    def convertcsv(self,csvFilePath, jsonFilePath):
        fieldnames = ("index","id","title","release_date", "overview","popularity","vote_average","vote_count","video")
        entries = []
        with open(csvFilePath, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames)
            for row in reader:
               entry = OrderedDict()
               for field in fieldnames:
                     entry[field] = row[field]
               entries.append(entry)

        output = {
           "movies": entries
        }

        with open(jsonFilePath, 'w') as jsonfile:
             json.dump(entries[1:], jsonfile)
             jsonfile.write('\n')

    #method convertxml to json    
    def convertXML(self,xmlfile,jsonFilePath):
        with open(xmlfile) as xml_file:
             data_dict = xmltodict.parse(xml_file.read())
             xml_file.close()
             json_data = json.dumps(data_dict)
             with open(jsonFilePath, "w",encoding='utf-8') as json_file:
                 json_file.write(json_data)
                 json_file.close()

    #method convertxls to json
    def convertxsl(self,xlsfile,jsonFilePath):
        wb=xlrd.open_workbook(xlsfile)
        sh=wb.sheet_by_index(0)
        data_List=[]
        for rownum in range(1,sh.nrows):
            data=OrderedDict()
            row_values=sh.row_values(rownum)
            data['First_Name']=row_values[0]
            data['Last_Name'] = row_values[1]
            data['Gender'] = row_values[2]
            data['Country'] = row_values[3]
            data['Age'] = row_values[4]
            data['Date'] = row_values[5]
            data['Id'] = row_values[6]
        data_List.append(data)
        j=json.dumps(data_List)
        with open(jsonFilePath,'w') as f:
            f.write(j)

#names of file path        
csvFilePath = r'dataset.csv'
jsonFilePath = r'pythonJSON.json'
xmlfilepath=r'xmlfilee.xml'
xlsfilepath=r'file_example_XLS_10.xls'
 #make object of convert class   
csvfile=Converter()
xmlfile=Converter()
xslfile=Converter()

#use object csfile and pass you csvfile path and json file path to convert to JSON
csvfile.convertcsv(csvFilePath, jsonFilePath)

# use object xmlfile and pass you xmlfile path and json file path to convert to JSON
xmlfile.convertXML(xmlfilepath,jsonFilePath)   

# use object xlsfile and pass you xlsfile path and json file path to convert to JSON
xslfile.convertxsl(xlsfilepath,jsonFilePath)

# making dataframe 

df = pd.read_csv("dataset.csv") 
df= df.iloc[: , 1:]




   
# select column title which need to access
print(df.columns)
q= input('Which column title u access from !? ').lower()

def getvalue(key, value):
    return df[key==value]

if q == 'id':
    x= int(input('\n Enter movie id: '))
    if x in df['id'].values:
        print(getvalue(df.id, x))
    else:
        raise ValueError("\n The movie id which you entered is incorrect!")

elif q == 'title':
    x= input('\n Enter movie title: ')
    if x in df['title'].values:
        print(getvalue(df.title, x))
    else:
        raise ValueError("\n The movie title which you entered is incorrect!")

elif q == 'release_date':
    x= input('Enter movie release_date: ')
    if x in df['release_date'].values:
        print(getvalue(df.release_date, x))
    else:
        raise ValueError("\n The movie release_date which you entered is incorrect!")

elif q == 'overview':
    x= input('\n Enter movie overview: ')
    if x in df['overview'].values:
        print(getvalue(df.overview, x))
    else:
        raise ValueError("\n The movie overview which you entered is incorrect!")

elif q == 'popularity':
    x= float(input('\n Enter movie popularity: '))
    if x in df['popularity'].values:
        print(getvalue(df.popularity, x))
    else:
        raise ValueError("\n The movie popularity which you entered is incorrect!")


elif q == 'vote_average':
    x= float(input('\n Enter movie vote_average: '))
    if x in df['vote_average'].values:
        print(getvalue(df.vote_average, x))
    else:
        raise ValueError("\n The movie vote_average which you entered is incorrect!")

elif q == 'vote_count':
    x= int(input('\n Enter movie vote_count: '))
    if x in df['vote_count'].values:
        print(getvalue(df.vote_count, x))
    else:
        raise ValueError("\n The movie vote_count which you entered is incorrect!")

elif q == 'video':
    x= bool(distutils.util.strtobool(input('\n Enter movie video: ').capitalize()))
    if x in df['video'].values:
        print(getvalue(df.video, x))
    else:
        raise ValueError("\n The movie video which you entered is incorrect!")

else:
    raise ValueError("\n The column name which you entered is incorrect!")





    





 







        

     
        
    
        
