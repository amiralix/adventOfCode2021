import pandas as pd
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import concurrent.futures
import numpy as np
import datetime
from threading import Thread
from oath2_impl3 import *

def runn():
    data = pd.read_csv(input("enter file path like D:/a.csv\n"))
    order = input("enter file read order from beginning 0 from end 1\n")
    #data = pd.read_csv("d:/new2.txt")
    start = datetime.datetime.now()
    recordsNumber = len(data)
    myArgs = np.zeros((recordsNumber,3), dtype=list)
    print(f"reading File with {recordsNumber} rows ...")
    for rows in range(0 ,recordsNumber):
            myArgs[rows][0]= str(data.natCode[rows]).rjust(10,'0')
            myArgs[rows][1]= str(data.birthDate[rows])
            myArgs[rows][2]= str(data.idDoc[rows])
            if (myArgs[rows][2] == 'nan'):
                myArgs[rows][2] = 0    
    token_manager = TokenManager3()
    if int(float(str(order))) == 0 : 
        with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
                    futures = [executor.submit(token_manager.call_service,myArgs[row][0],myArgs[row][1][0:10],int(float(myArgs[row][2])),'true',token_manager.getToken()) for row in range(0,recordsNumber)]
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=9) as executor:
                    futures = [executor.submit(token_manager.call_service,myArgs[row][0],myArgs[row][1][0:10],int(float(myArgs[row][2])),'true',token_manager.getToken()) for row in range(recordsNumber-1,0,-1)]
    end = datetime.datetime.now()
    print(f"running Threads took {end - start}")
    ''' time.sleep(1)
    start = datetime.datetime.now()
    print("start to write results to file ...")          
    with open(f"d:/icms_real_iranian_{str(start)[0:10]}_{str(start)[11:13]}_{str(start)[14:16]}_{str(start)[17:19]}_result.txt","w+", encoding="utf-8") as file:

    for future in futures:
            if (future._state == 'FINISHED'):
                print(str(future._result))
            else : pass       
    end = datetime.datetime.now()
    print(f"writing results to file took{end - start}")
    print("write to file succeed !!!")  
    ''' 
def runn_readline():
        fileAddress = input("enter file path like D:/a.csv\n")
        start = datetime.datetime.now()
        with open(fileAddress, 'r') as file:
            lineLIst = file.readlines()
        print(f"reading File with {len(lineLIst)} rows ...")
        token_manager = TokenManager3()
        with concurrent.futures.ThreadPoolExecutor(max_workers=13) as executor:
            [executor.submit(token_manager.call_service,str(lineLIst[rows][0:10]).rjust(10,'0'),str(lineLIst[rows][11:21]),int(lineLIst[rows][38:len(lineLIst[rows])]),'true',token_manager.getToken()) for rows in range(len(lineLIst)-1,1,-1)]
        end = datetime.datetime.now()
        print(f"running Threads took {end - start}")

if __name__ == '__main__':
    runn_readline()
    '''
    with open('D:/NAHAB_TB_COMPARE_NOCR_result2.csv', 'r') as file:
            lineLIst = file.readlines()
    print(f"read Done for {len(lineLIst)}")
    token_manager = TokenManager3()
    threads = [ 
          Thread(
                target=token_manager.call_service,
                        args=
                        ( (str(lineLIst[rows][0:10]).rjust(10,'0'))
                           ,(str(lineLIst[rows][11:21]))
                           ,(int(lineLIst[rows][38:len(lineLIst[rows])]))
                           ,'true'
                           ,token_manager.getToken()
                        ) 
                         ) for rows in range(1,len(lineLIst)
                ) 
                ]
    for thread in threads:
        thread.start()
# wait for threads to finish
    for thread in threads:
        thread.join()
# close the file
    file.close()
    '''
        
