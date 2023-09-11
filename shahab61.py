import pandas as pd
from persiantools.jdatetime import JalaliDateTime
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import math
from colorama import Fore, Back, Style
from  NocrOprInqClass import NocrOprInqClass
import time
import numpy as np

with open("d:/resuktNew001.txt","a") as file:
    data = pd.read_csv("d:/ip_real_iranian_47233351 - Copy.csv")
    #check if birthdate is gregorian or persian . true means gregorian birth date
    english_date_default_flag = True
    for rows in range(0,len(data)):
        str_melli_code = str(data.natCode[rows])
        str_melli_code = str_melli_code.rjust(10,'0')
        if english_date_default_flag == False :
            strPersianBirth = str(data.Bdate[rows])
            #if (type (strPersianBirth) == float.64)
            strGregBirth = JalaliDate(year=int(strPersianBirth[0:4]) , month=int(strPersianBirth[5:7]) , day=int(strPersianBirth[8:10])).to_gregorian().isoformat()
        else:
            strGregBirth = str(data.birthDate[rows])    
            
        nocrResponse = NocrOprInqClass.inquiry(mellicode=str_melli_code[0:11], bdate=strGregBirth[0:10])
        if nocrResponse.status_code == 200 :
            nocrJsonResponse = nocrResponse.json()
            if (nocrJsonResponse['response']['lifeState']['code'] == 'LIVING'):
                idNo = nocrJsonResponse['response']['certificateNumber']
                shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=idNo, inquiryType='false')
                if shahabinq[0] == 200 :
                    if (shahabinq[1])['response']['personInfo']['shahabCode'] is None :
                        time.sleep(1)
                        shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=idNo,inquiryType='false')
                        if shahabinq[0] == 200:
                                file.write(f"{str_melli_code} , {shahabinq[1]['response']['personInfo']['shahabCode']}\n")    
                    else : continue
                else:
                    shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=idNo,inquiryType='false')
                    pass        
            else:
                file.write(f"{str_melli_code} , {nocrJsonResponse['response']['lifeState']['code']}\n")
                pass
            file.write(f"{str_melli_code} , {nocrResponse.status_code}\n")
        

