import csv
import json
from collections import Counter

def paisSelva():
    archivo_csv= open("areaselvatica.csv","r",encoding="utf-8")
    csvreader = csv.reader(archivo_csv, delimiter=",")

    archivo_json = open("archivoJsonS.txt","x")
    dic={}

    for linea in csvreader:
        if linea[61] !="":
            dic[linea[0]]=float(linea[61])
    dic = Counter(dic)

    json.dump(dic.most_common(11), archivo_json)

    archivo_csv.close()

    archivo_json.close()
    

def paisRural():

    archivo_csv = open("rural.csv","r",encoding="utf-8")
    csvreader = csv.reader(archivo_csv, delimiter=",")

    archivo_json = open("archivoJsonR.txt","x")

    for linea in csvreader:
        if linea[62] !="":
            if int(linea[62])>60000000:
                json.dump(linea[0], archivo_json)
    
    archivo_csv.close()

    archivo_json.close()
    