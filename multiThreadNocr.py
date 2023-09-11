from socket import AF_INET
from socket import SOCK_STREAM
from socket import socket
from multiprocessing.pool import ThreadPool
from persiantools.jdatetime import JalaliDate
from NocrOprInqClass import *
import numpy as np
import concurrent.futures
import pandas as pd


def test_port_number(host , port):
    with socket(AF_INET , SOCK_STREAM) as sock:
        sock.settimeout(3)
        try:
            sock.connect((host, port))
            return True
        except:
            return False    
        
def runn():
    print(f'reading File...')  
    data = pd.read_csv("D:/new4.txt")
    valuesDict= dict()
    for rows in range(0,len(data)):
        nationalCode = str(data.melliCode[rows])
        birthdate = str(data.bDate[rows])
        year = str(birthdate[0:4])
        month = str(birthdate[5:7])
        day = str(birthdate[8:10])
        try:
            myDate = JalaliDate( year=int(year) , month=int(month) , day=int(day)).to_gregorian().isoformat()
        except Exception as myEX:
                        print(myEX)
                    #   with open("D:/convertedTimeError.csv","a") as fileError:
                    #       fileError.write(f'{nationalCode}\n')  
                        continue
        valuesDict[nationalCode.rjust(10,"0")] = myDate      
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # dispatch all tasks
        #auth_tok = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2ODc0MzI1NDE4MDEsIm5iZiI6MTY4NzM0NjE0MTgwMSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiN2ZjYTZlODQtYjI1Yy0zYTQ4LWE2YTAtYTE0OGY1MTExYzhmIiwic3NuIjoiNDk1OTY0NjIzMyIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJpY21zLXNpYmEtY3VzdG9tZXIiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJub2NyLWRlY2Vhc2VkLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.bZhRM4d2RuF5kzMCgZkYWsBt-W6yfjHKsN_I3zNHKlo'
        #results contains all return values
        futures = [
             executor.submit
                (NocrOprInqClass.inquiry,mellicode,valuesDict[mellicode]) 
                            for mellicode in valuesDict.keys()
                ]
        
        # report results in order
        #for future in concurrent.futures.as_completed(futures):
         ##       pass
                #print(f'>: success')
                #print(future.request() , future.result().status_code)
           # else:
            #    print(future.result()[0] , future.result()[1])
             #   print(f'>: fail')

if __name__ == '__main__':
    # define host and port numbers to scan
    # test the ports
    runn()
