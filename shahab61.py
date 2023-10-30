import pandas as pd
from persiantools.jdatetime import JalaliDateTime
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import math
from colorama import Fore, Back, Style
from  NocrOprInqClass import NocrOprInqClass
import time
import numpy as np

with open("d:/result190.txt","a") as file:
    data = pd.read_csv("d:/14.txt")
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
        splittedBirthDate = strGregBirth.split('-')
        if (len(splittedBirthDate[1]) == 1) : splittedBirthDate[1] = splittedBirthDate[1].rjust(2,'0')
        if (len(splittedBirthDate[2]) == 1 ): splittedBirthDate[2] = splittedBirthDate[2].rjust(2,'0')
        formattedBirthDate = "{}-{}-{}".format(*splittedBirthDate)
        nocrResponse = NocrOprInqClass.inquiry(mellicode=str_melli_code[1:11], bdate=formattedBirthDate)
        if nocrResponse.status_code == 200 :
            nocrJsonResponse = nocrResponse.json()
            if (nocrJsonResponse['response']['lifeState']['code'] == 'LIVING'):
                idNo = nocrJsonResponse['response']['certificateNumber']
                accessToken = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoia2V5IiwiZXhwIjoxNjk3NzEzMTkxNTk3LCJuYmYiOjE2OTc2MjY3OTE1OTcsInJvbGUiOiIiLCJzZXJpYWwiOiJlZWZjOWFhZi02ZDg3LTMyMDEtYWQ5ZS01OTM1YmQ5MWVlOGEiLCJzc24iOiIxMjMiLCJjbGllbnRfaWQiOiIxMjMiLCJzY29wZXMiOlsiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiYWNjb3VudC1zdXBlciIsInN2Yy1tZ210LWFnZy1hY2MtcGFydC1wZXJjLWluZm8iLCJzdmMtbWdtdC1zdG10LXN1cC1pbmZvIiwiY3VzdG9tZXItc3VwZXIiLCJpY21zLW5vY3ItdHJhY2tpbmctaW5xdWlyeSIsInJlY2VpdmUtc21zIl19.SzrVDc0QICtEj7xmVIGnDgdqsbGch2j7Cr4U56AqUeU'
                shahabinq = shahabInquiry.inquiry4Items(natCode=str_melli_code[1:11],bdate=formattedBirthDate,shenasnameNo=idNo,inquiryType='false',access_token=accessToken) # type: ignore
                if shahabinq[0] == 200 :
                    if (shahabinq[1])['response']['personInfo']['shahabCode'] is None :
                        time.sleep(1)
                        shahabinq = shahabInquiry.inquiry4Items(natCode=str_melli_code[1:11] , bdate=formattedBirthDate , shenasnameNo=idNo,inquiryType='false' ,access_token=accessToken) # type: ignore
                        if shahabinq[0] == 200:
                                file.write(f"{str_melli_code} , {shahabinq[1]['response']['personInfo']['shahabCode']}\n")    
                    else : continue
                else:
                    shahabinq = shahabInquiry.inquiry4Items(natCode=str_melli_code[1:11] , bdate=formattedBirthDate , shenasnameNo=idNo,inquiryType='false' , access_token=accessToken )
                    pass        
            else:
                file.write(f"{str_melli_code} , {nocrJsonResponse['response']['lifeState']['code']} , {nocrJsonResponse['response']['deathDate']}\n")
                pass
#            file.write(f"{str_melli_code} , {nocrResponse.status_code}\n")
        

