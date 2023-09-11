import pandas as pd
from persiantools.jdatetime import JalaliDateTime
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import math
from colorama import Fore, Back, Style
from  NocrOprInqClass import NocrOprInqClass
import time
import numpy as np

file = open("d:/result.txt","a")
data = pd.read_csv("d:/600Shahab.csv")
for rows in range(0,len(data)):
    str_melli_code = str(data.melliCode[rows])
    str_melli_code = str_melli_code.rjust(10,'0')
    strGregBirth = str(data.Bdate[rows])
    strIdDocNo =  data.IDENTITY_CODE[rows]
    if (strIdDocNo.astype(np.float64)):
        strIdDocNo = 0
    else :strIdDocNo = str(data.IDENTITY_CODE[rows])
    shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=int(float(strIdDocNo)), inquiryType='false')
    if (shahabinq is not None and shahabinq[0] == 200 and shahabinq[1]['response']['personInfo']['shahabCode'] is None ):
        time.sleep(1)
        shahabinq = shahabInquiry.inquiry(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=int(float(strIdDocNo)), inquiryType='true')
    else: continue
