import pandas as pd
from persiantools.jdatetime import JalaliDateTime
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import math
from colorama import Fore, Back, Style
from  NocrOprInqClass import NocrOprInqClass
import time
import numpy as np

file = open("d:/resultShahab.txt","a") 
data = pd.read_csv("d:/new21.csv")
for rows in range(0,len(data)):
    str_melli_code = str(data.NATCODE[rows])
    str_melli_code = str_melli_code.rjust(10,'0')
    strGregBirth = data.BIRTH_DATE[rows]
    strPersianBirth = str(data.DOPbirthDate[rows])
    if( type(strGregBirth) == np.float64 ):
        strGregBirth = JalaliDate(year=int(strPersianBirth[0:4]) , month=int(strPersianBirth[4:6]) , day=int(strPersianBirth[6:8])).to_gregorian().isoformat()   
    else:
        strGregBirth = str(data.BIRTH_DATE[rows])
    nocrResponse = NocrOprInqClass.inquiry(mellicode=str_melli_code, bdate=strGregBirth[0:10])
    if nocrResponse != False:
        nocrJsonResponse = nocrResponse.json()
        if (nocrJsonResponse['response']['lifeState']['code'] == 'LIVING'):
            idNo = nocrJsonResponse['response']['certificateNumber']
            shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=idNo,inquiryType='false')
    #            if shahabinq['nahabResponse']['shahabInfo']['shahabCode'] 
        #       time.sleep(1)
        #       shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=idNo,inquiryType='false')
        else:
            file.write(f"{str_melli_code} , {nocrJsonResponse['response']['lifeState']['code']}")
    else:
        print(f"NOCR inquiry failed for {str_melli_code}")
