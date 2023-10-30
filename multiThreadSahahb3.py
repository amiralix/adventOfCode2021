import pandas as pd
from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import concurrent.futures
import numpy as np
import datetime
from threading import Thread
from oath2_impl3 import *
from FidaInquiry import FidaInquiry

def runn():
    data = pd.read_csv('D:/18.txt')
    order = '1'
    start = datetime.datetime.now()
    recordsNumber = len(data)
    myArgs = np.zeros((recordsNumber,3), dtype=list)
    print(f"reading File with {recordsNumber} rows ...")
    for rows in range(0 ,recordsNumber):
            myArgs[rows][0]= str(data.natCode[rows]).rjust(10,'0')
            myArgs[rows][1]= str(data.birthDate[rows])
            monthBirthDateExtracted = myArgs[rows][1].split('-')
            if len(monthBirthDateExtracted[1]) == 1:
                monthBirthDateExtracted[1] = monthBirthDateExtracted[1].rjust(2,'0')
            if len(monthBirthDateExtracted[2]) == 1:
                monthBirthDateExtracted[2] = monthBirthDateExtracted[2].rjust(2,'0')
            jalaliMyDate = JalaliDate(int(monthBirthDateExtracted[0]), int(monthBirthDateExtracted[1]), int(monthBirthDateExtracted[2])).to_gregorian()
            jalaliMyDate = jalaliMyDate.isoformat()
            myArgs[rows][1] = jalaliMyDate
            #myArgs[rows][1] = "{}-{}-{}".format(*myArgs[rows][1])
            myArgs[rows][2]= str(data.idDoc[rows])
            if (myArgs[rows][2] == myArgs[rows][0][1:11] ):
                myArgs[rows][2] = 0
            if (myArgs[rows][2] == 'nan'):
                myArgs[rows][2] = 0
            try:
                myArgs[rows][2] = int(float(myArgs[rows][2]))
            except:
                myArgs[rows][2] = 0
    token_manager = TokenManager3()
    if int(float(str(order))) == 0 : 
        with concurrent.futures.ThreadPoolExecutor(max_workers =150) as executor:
                    futures = [executor.submit(token_manager.call_service,
                            myArgs[row][0][1:11], #nationalCode
                            myArgs[row][1][0:10], #birthDate
                            int(float(myArgs[row][2])), #iDdoc
                            'false',
                            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTg3NDU3OTA4ODEsIm5iZiI6MTY5ODY1OTM5MDg4MSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiNDI5Y2RkNmYtNTBiNS0zNjBhLWI4NjItYzg2MWEyOTU4MWFjIiwic3NuIjoiMTM4MDgxMTM0MSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.VWCdIgukSjsnmaqe1OjA03DADaae0JalCqRgMI0QeJc')
                            for row in range(0,recordsNumber)]
    else:
        with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:
                    futures = [executor.submit(token_manager.call_service,
                            myArgs[row][0][1:11], #nationalCode
                            myArgs[row][1][0:10], #birthDate
                            int(float(myArgs[row][2])), #iDdoc
                            'false',
                            'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTg3NDU3OTA4ODEsIm5iZiI6MTY5ODY1OTM5MDg4MSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiNDI5Y2RkNmYtNTBiNS0zNjBhLWI4NjItYzg2MWEyOTU4MWFjIiwic3NuIjoiMTM4MDgxMTM0MSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.VWCdIgukSjsnmaqe1OjA03DADaae0JalCqRgMI0QeJc')
                            for row in range(recordsNumber-1,0,-1)]
    end = datetime.datetime.now()
    for future in futures:
            if (future._state == 'FINISHED'):
                print(str(future._result))
            else : pass       
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
        defaultAddress = 'C:/NAHAB_TB_COMPARE_NOCR_result2.csv'
        fileAddress = input("enter file path default is C:/NAHAB_TB_COMPARE_NOCR_result2.csv\n")
        if fileAddress == '':
            fileAddress = defaultAddress
        start = datetime.datetime.now()
        with open(fileAddress, 'r') as file:
            lineLIst = file.readlines()
        print(f"reading File with {len(lineLIst)} rows ...")      
        token_manager = TokenManager3()
        with concurrent.futures.ThreadPoolExecutor(max_workers=25) as executor:
            [executor.submit(
                    token_manager.call_service,
                        str(lineLIst[rows][0:10]).rjust(10,'0'),
                            str(lineLIst[rows][11:21]),
                                int(lineLIst[rows][38:len(lineLIst[rows])]),
                                    'false',
                                        token_manager.getToken()
                                            )
                                                for rows in range(len(lineLIst)-1,1,-1)
            ]
        end = datetime.datetime.now()
        print(f"running Threads took {end - start}")

        
        
        
def runn_legal():
    fileAddress = input("enter file path default is D:/.csv\n")
    if len(fileAddress) == 0:
        fileAddress = 'D:/19.txt'
    data = pd.read_csv(fileAddress)
    order = 0
    order = input("enter file read order from beginning 0 from end 1\n")
    start = datetime.datetime.now()
    recordsNumber = len(data)
    myArgs = np.zeros((recordsNumber,3), dtype=list)
    print(f"reading File with {recordsNumber} rows ...")
    for rows in range(0 ,recordsNumber):
            myArgs[rows][0]= str(data.natCode[rows]).rjust(11,'0')
            #print(myArgs[rows][0])
            myArgs[rows][1]= str(data.birthDate[rows])
            monthBirthDateExtracted = myArgs[rows][1].split('-')
            if len(monthBirthDateExtracted[1]) == 1:
                monthBirthDateExtracted[1] = monthBirthDateExtracted[1].rjust(2,'0')
            if len(monthBirthDateExtracted[2]) == 1:
                monthBirthDateExtracted[2] = monthBirthDateExtracted[2].rjust(2,'0')
            jalaliMyDate = JalaliDate(int(monthBirthDateExtracted[0]), int(monthBirthDateExtracted[1]), int(monthBirthDateExtracted[2])).to_gregorian()
            jalaliMyDate = jalaliMyDate.isoformat()
            myArgs[rows][1] = jalaliMyDate
            #myArgs[rows][1] = "{}-{}-{}".format(*myArgs[rows][1])
            myArgs[rows][2]= str(data.regNo[rows])
            if (myArgs[rows][2] == myArgs[rows][0][1:11] ):
                myArgs[rows][2] = 0
            if (myArgs[rows][2] == 'nan'):
                myArgs[rows][2] = 0
    token_manager = TokenManager3()
    with concurrent.futures.ThreadPoolExecutor(max_workers =10) as executor:
                    futures = [executor.submit(token_manager.call_service_legal,
                            myArgs[row][0][1:12], #nationalCode
                            myArgs[row][1][0:10], #birthDate
                            int(float(myArgs[row][2])), #regNo
                            'false',
                            token_manager.getToken())
                            for row in range(0,recordsNumber)]
    end = datetime.datetime.now()
    for future in futures:
            if (future._state == 'FINISHED'):
                print(str(future._result))
            else : pass       
    print(f"running Threads took {end - start}")



def runn_real_foreign():
    #fileAddress = input("enter file path default is D:/.csv\n")
    #if len(fileAddress) == 0:
    #    fileAddress = 'D:/20.txt'
    data = pd.read_csv('D:/20.txt')
    order = '0'
    start = datetime.datetime.now()
    recordsNumber = len(data)
    myArgs = np.zeros((recordsNumber,4), dtype=list)
    print(f"reading File with {recordsNumber} rows ...")
    for rows in range(0 ,recordsNumber):
            myArgs[rows][0]= str(data.fidaCode[rows])
            myArgs[rows][2]= str(data.bdate[rows])
            monthBirthDateExtracted = myArgs[rows][2].split('-')
            if len(monthBirthDateExtracted[1]) == 1:
                monthBirthDateExtracted[1] = monthBirthDateExtracted[1].rjust(2,'0')
            if len(monthBirthDateExtracted[2]) == 1:
                monthBirthDateExtracted[2] = monthBirthDateExtracted[2].rjust(2,'0')
            jalaliMyDate = JalaliDate(int(monthBirthDateExtracted[0]), int(monthBirthDateExtracted[1]), int(monthBirthDateExtracted[2])).to_gregorian()
            jalaliMyDate = jalaliMyDate.isoformat()
            myArgs[rows][2] = jalaliMyDate
            myArgs[rows][1]= str(data.idDocNumber[rows])
            if (myArgs[rows][2] == 'nan'):
                myArgs[rows][2] = 0
            myArgs[rows][3]= str(data.country[rows])
    with concurrent.futures.ThreadPoolExecutor(max_workers =10) as executor:
            futures = [executor.submit(TokenManager3().call_service_real_foreign,
                            myArgs[row][0],
                            myArgs[row][1],
                            myArgs[row][3],
                            myArgs[row][2],
                            'false')
                            for row in range(0,recordsNumber)] 
                    
    end = datetime.datetime.now()  
    for future in futures:
            if (future._state == 'FINISHED'): # type: ignore
                print(str(future._result)) # type: ignore
            else : pass       
    print(f"running Threads took {end - start}")





if __name__ == '__main__':
    #runn_readline()
    personType = input("please enter person Nahab Type 1:real_iranian 2:legal_iranian 3:real_foreigner 4:legal_foreigner\n")
    if (personType == '1' ):
        runn()
    elif personType == '2':
        runn_legal()
    elif personType == '3':
        runn_real_foreign()
    elif personType == '4':    
        pass
    else : pass
