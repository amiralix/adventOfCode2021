import pandas as pd
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import concurrent.futures
import numpy as np
import datetime
import time
from oath2_impl import *

def runn():
#    data = pd.read_csv("d:/ip_real_iranian_47233351 - Copy.csv")
    #data = pd.read_csv("d:/new77.txt")
    #data = pd.read_csv("d:/icms_real_iranian_shahab_code_null.csv")
    data = pd.read_csv("d:/NAHAB_TB_COMPARE_NOCR_result_edited2.csv")
    start = datetime.datetime.now()
    recordsNumber = len(data)
    myArgs = np.zeros((recordsNumber,3), dtype=list, order='F')
    print(f"reading File with {recordsNumber} rows ...")
    for rows in range(0,recordsNumber):
            myArgs[rows][0]= str(data.natCode[rows]).rjust(10,'0')
            myArgs[rows][1]= str(data.birthDate[rows])
            myArgs[rows][2]= str(data.idDoc[rows])
            if (myArgs[rows][2] == 'nan'):
                myArgs[rows][2] = 0
     
    token_manager = TokenManager()
    with concurrent.futures.ThreadPoolExecutor(max_workers=7) as executor:
             futures = [executor.submit(token_manager.call_service,myArgs[row][0],myArgs[row][1][0:10],int(float(myArgs[row][2])),'true',token_manager.getToken()) for row in range(0,recordsNumber)]

    end = datetime.datetime.now()
    print(f"running Threads took {end - start}")
    ''' time.sleep(1)
    start = datetime.datetime.now()
    print("start to write results to file ...")          
    with open(f"d:/icms_real_iranian_{str(start)[0:10]}_{str(start)[11:13]}_{str(start)[14:16]}_{str(start)[17:19]}_result.txt","w+", encoding="utf-8") as file:
        for future in futures:
            if (future._state == 'FINISHED'):
                file.write(str(future._result))
            else : pass       
    end = datetime.datetime.now()
    print(f"writing results to file took{end - start}")
    print("write to file succeed !!!")  
'''
if __name__ == '__main__':
    runn()
        
