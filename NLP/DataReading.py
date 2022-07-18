from pandas.core import flags
#Importing libraries 
import pandas as pd 
import re
import numpy as np
import os 
from textblob import TextBlob
import cv2
import pytesseract 
from PIL import Image
import pdfplumber
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Selenium\Tesseract\tesseract.exe' #Ruta del archivo ejecutable para la conversión de imagen a texto 
import glob
#Data reading 
data = pd.read_csv(r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Limpieza de datos\Database_empleos\New data\rawdata.csv')
extraDataSFEN = pd.read_csv(r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Limpieza de datos\Database_empleos\New data\ProfileITforRegresionSFEN.csv')
extraDataMLE = pd.read_csv(r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Limpieza de datos\Database_empleos\New data\ProfileITforRegresionMLE.csv')
#Data transforming 
class TransformdataCSV():
  def ReadContentCSVSFEN(self):
    Content = data["Content"].tolist()
    NewList = []
    for cont in Content:
        temp = []
        total = 0
        time1 = 0
        time2 = 0
        cont = str(cont).splitlines()
        for line in cont:
            if line not in temp:
                temp.append(line)
        cont = ''.join(temp)
        cont = str(cont).replace('\n','')
        Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", cont , flags= re.MULTILINE)
        try:
            Experience = Experience[0]
            exp = re.findall('Software engineer.{135,150}|Software Development Engineer.{135,150}|Software developer.{135,150}|Web developer.{135,150}|Java developer.{135,150}', Experience, flags = re.IGNORECASE)
            exp = ''.join(exp)
            months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
            months = ''.join(months)
            months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
            years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
            years = ''.join(years)
            years = re.findall('\d',years)
            for year in years:
                yearsD = int(year)
                if yearsD == 1:
                    yearsD = 12
                if yearsD == 2:
                    yearsD = 24
                time2 += int(yearsD)
            for time in months:
                time1 += int(time)
            total = time1 + time2 
            if total <= 36:
                NewList.append(cont)
        except:
            pass
        del temp
    return NewList
  def ReadContentCSVMLE(self):
    Content = data["Content"].tolist()
    NewList = []
    for cont in Content:
        temp = []
        total = 0
        time1 = 0
        time2 = 0
        cont = str(cont).splitlines()
        for line in cont:
            if line not in temp:
                temp.append(line)
        cont = ''.join(temp)
        cont = str(cont).replace('\n','')
        Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", cont , flags= re.MULTILINE)
        try:
            Experience = Experience[0]
            exp = re.findall('Machine Learning Engineer.{130}|Data Scientist.{130}|Data Engineer.{130}|AI Engineer.{130}', Experience, flags = re.IGNORECASE)
            exp = ''.join(exp)
            months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
            months = ''.join(months)
            months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
            years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
            years = ''.join(years)
            years = re.findall('\d',years)
            for year in years:
                yearsD = int(year)
                if yearsD == 1:
                    yearsD = 12
                if yearsD == 2:
                    yearsD = 24
                time2 += int(yearsD)
            for time in months:
                time1 += int(time)
            total = time1 + time2 
            if total <= 36:
                NewList.append(cont)
        except:
            pass
        del temp
    return NewList
  def ReadContentCSVCSE(self):
    Content = data["Content"].tolist()
    NewList = []
    for cont in Content:
        temp = []
        total = 0
        time1 = 0
        time2 = 0
        cont = str(cont).splitlines()
        for line in cont:
            if line not in temp:
                temp.append(line)
        cont = ''.join(temp)
        cont = str(cont).replace('\n','')
        Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", cont , flags= re.MULTILINE)
        try:
            Experience = Experience[0]
            exp = re.findall('Malware engineer.{130}|Threat Hunter.{130}|Digital Forensic Analyst.{130}|Malware analyst.{130}|Network Manager.{130}|Security Engineer.{130}', Experience, flags = re.IGNORECASE)
            exp = ''.join(exp)
            months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
            months = ''.join(months)
            months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
            years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
            years = ''.join(years)
            years = re.findall('\d',years)
            for year in years:
                yearsD = int(year)
                if yearsD == 1:
                    yearsD = 12
                if yearsD == 2:
                    yearsD = 24
                time2 += int(yearsD)
            for time in months:
                time1 += int(time)
            total = time1 + time2 
            if total <= 36:
                NewList.append(cont)
        except:
            pass
        del temp
    return NewList
  def ReadContentCSVDSC(self):
    Content = data["Content"].tolist()
    NewList = []
    for cont in Content:
        temp = []
        total = 0
        time1 = 0
        time2 = 0
        cont = str(cont).splitlines()
        for line in cont:
            if line not in temp:
                temp.append(line)
        cont = ''.join(temp)
        cont = str(cont).replace('\n','')
        Experience = re.findall(r"Experiencia(?P<ID>.*)Educación", cont , flags= re.MULTILINE)
        try:
            Experience = Experience[0]
            exp = re.findall('Data Scientist.{130}|Data Analyst.{130}|Data engineer.{130}', Experience, flags = re.IGNORECASE)
            exp = ''.join(exp)
            months = re.findall('\d.{1,2} meses|\d.mes', exp, flags=re.IGNORECASE)
            months = ''.join(months)
            months = re.findall('\d{1,2}', months, flags= re.IGNORECASE)
            years = re.findall('\d.años|\d.año', exp, flags=re.IGNORECASE)
            years = ''.join(years)
            years = re.findall('\d',years)
            for year in years:
                yearsD = int(year)
                if yearsD == 1:
                    yearsD = 12
                if yearsD == 2:
                    yearsD = 24
                time2 += int(yearsD)
            for time in months:
                time1 += int(time)
            total = time1 + time2 
            if total <= 36:
                NewList.append(cont)
        except:
            pass
        del temp
    return NewList
  def ReadPDFContent(self):
    path = r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Limpieza de datos\PDFs'
    myList = os.listdir(path)
    Text = str()
    Total_text = []
    for x in myList:     
      pdf = pdfplumber.open(path + '\\' + str(x))
      totalpages = len(pdf.pages)
      for i in range(0 ,totalpages):
        pageobj = pdf.pages[i]
        pageobj = pageobj.extract_text()
        pageobj = pageobj.replace('', '')
        Text += pageobj
      Total_text.append(Text) 
    return Total_text
  def ImageToText(self):
    path = r'C:\Users\Fernando.DESKTOP-608G9HT\Documents\Cosas personales Fer\Python\Limpieza de datos\Imagenes'
    myList = os.listdir(path)
    Text = str()
    Total_text = []
    for x in myList: 
      img = cv2.imread(path + '\\' + str(x))
      Text = pytesseract.image_to_string(img)
      Total_text.append(Text)
    return Total_text
  def LanguageValidation(self,text):
    translated = GoogleTranslator(translated = GoogleTranslator(source='auto', target='en').translate(text=text))
    return translated