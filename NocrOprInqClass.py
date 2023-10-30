import requests
from persiantools.jdatetime import JalaliDate
from colorama import Fore
import concurrent.futures
import numpy as np


class NocrOprInqClass:
    def __init__(self , nationalCode , birthdate):
        self.natCode = nationalCode
        self.bDate = birthdate
        api_url = 'https://192.168.234.194:9080/api/icms/v1/individual/tracking/inquiry'
        file = 'd:/error_pishgaman.txt'

    def inquiry(self):
        headers = {'Content-Type': 'application/json' ,
        'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoia2V5IiwiZXhwIjoxNjk1NTg4MzY1NDc0LCJuYmYiOjE2OTU1MDE5NjU0NzQsInJvbGUiOiIiLCJzZXJpYWwiOiI5MjY3YzY5YS0zMjg2LTM1MzYtOWUyYS1iYWQxODEyNjE1NTQiLCJzc24iOiIxMjMiLCJjbGllbnRfaWQiOiIxMjMiLCJzY29wZXMiOlsiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiYWNjb3VudC1zdXBlciIsInN2Yy1tZ210LWFnZy1hY2MtcGFydC1wZXJjLWluZm8iLCJzdmMtbWdtdC1zdG10LXN1cC1pbmZvIiwiY3VzdG9tZXItc3VwZXIiLCJpY21zLW5vY3ItdHJhY2tpbmctaW5xdWlyeSIsInJlY2VpdmUtc21zIl19.-K-OIbO_xYZiFOQXOCVC0X7i-xRvT78GVqmY9DNBTXs'}
        data={"nationalIdentifier":self.natCode,"birthDate":self.bDate,"online":"true","acceptDays":"1"}
        response = requests.post(self.api_url,headers=headers,json=data , verify=False , timeout=50)
        return response

    def oldInquiry(mellicode ,bdate , token):
        api_url = 'https://customer.bmiapis.ir/api/icms/v1/individual/inquiry'
        headers = {'Content-Type': 'application/json' ,'Authorization':f'Bearer {token}'}     
        data={"nationalIdentifier":mellicode,"birthDate":bdate,"online":'true',"acceptDays":"30"}
        try:
            response = requests.post(api_url ,headers=headers ,json=data, verify=True , timeout=50)
            if response.status_code == 200:
                #print(Fore.WHITE ,f'Old Inquiry for natcode {mellicode} successful' )
                #print(Fore.WHITE ,response.json()['response']['signature'] )
                jsonResponse = response.json()
                if (jsonResponse['response'] is not None):
                    print(jsonResponse['response']['nationalIdentifier'] ,jsonResponse['response']['birthDate'] ,jsonResponse['response']['certificateNumber']  )
                else : print(jsonResponse)
                return response
            else: 
                #print(Fore.RED,'for', {mellicode} ,{bdate} ,'response NOCR is ',response.json()['error']['code'] ,response.json()['error']['errors'] )
                print(response.json())
                return response
        except Exception as myEX:
            print(myEX)

    def inquiry(mellicode ,bdate,token):
        api_url = 'https://customer.bmiapis.ir/api/icms/v1/individual/tracking/inquiry'
        headers = {'Content-Type': 'application/json' ,'Authorization':f'Bearer {token}'}     
        data={"nationalIdentifier":mellicode,"birthDate":bdate,"online":'False',"acceptDays":"30"}
        try:
            response = requests.post(api_url ,headers=headers ,json=data, verify=True , timeout=50)
            if response.status_code == 200:
                print(Fore.WHITE ,f'NOCR 3Tfor natcode {mellicode} successful' )
                #print(Fore.WHITE ,response.json()['response']['signature'] )
                return response
            else: 
                #print(f'for natcode {mellicode} failed by {threading.get_native_id()} because of {response.status_code}' )
                #print(f'for natcode {mellicode} failed because of {response.status_code}' )
                #print('for natcode ',mellicode,'failed because of',response.json()['error']['code'] )
                print(Fore.RED,'for', {mellicode} ,{bdate} ,'response NOCR is ',response.json()['error']['code'] ,response.json()['error']['errors'] )
                return response
        except Exception as myEX:
            print(myEX)


    def fileInq():
        with open("D:/inq.csv") as file:
            input = file.readlines()
        input = [input[x].strip() for x in range(len(input))]
        headers = {'Content-Type': 'application/json' ,
        'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTU5MDI1NTI1NTgsIm5iZiI6MTY5NTgxNjE1MjU1OCwicm9sZSI6IiIsInNlcmlhbCI6IjdjY2Q5ZmQ1LWJiMjctMzFmMC04MGRlLTU0NzYyM2YzODYyYiIsInNzbiI6IjEzNzIiLCJjbGllbnRfaWQiOiIxMzcyIiwic2NvcGVzIjpbInNlcnZpY2VzLW5vY3ItdHJhY2tpbmctaW5xdWlyeSJdfQ==.8EXdrcUD6tHrisLzZTaSKzrxFHQ4M65iaPFlKtSyxZo'}
        for i in range(len(input)):
            if (input[i][0] != ','):
                nationalIdentifier = input[i][1:11]
                birthDate = input[i][14:24]
                '''yearBirthDate = birthDate[0]
                monthBirthDate = birthDate[1]
                dayBirthDate =  birthDate[2]
                bb = "{}-{}-{}"
                if len(monthBirthDate) == 1 : monthBirthDate = monthBirthDate.zfill(2)
                if len(dayBirthDate) == 1 : dayBirthDate = dayBirthDate.zfill(2)
                bdate = bb.format(yearBirthDate,monthBirthDate,dayBirthDate )'''
                data={"nationalIdentifier":nationalIdentifier,"birthDate":birthDate,
                      "online":"true","acceptDays":"1","callerUnitCode":"0011001100",
                      "callerUnitCode":"rayan-icms-client","branchCode":"60"}
                response = requests.post('http://192.168.34.37:1410/api/nocr/v1/person/tracking/inquiry'
                                         ,headers=headers,json=data , verify=False)
                if (response.status_code == 200 ):
                    print(i , "is successful for ", nationalIdentifier , response.json() )
                    #with open("D:/3success_result.csv","a") as filesuccess:
                     #   filesuccess.write(f'{input[i][0:10]};{input[i][11:22]};{response.status_code};{response.content} \n')
                else: 
                    print(f" {i} error because of {response.json()} for {nationalIdentifier} ")
                    #with open("D:/error_result.csv","a") as errorfile:
                     #   errorfile.write(f'{input[i][0:10]};{input[i][11:22]};{response.status_code};{response.content}\n')
        #filesuccess.close()
        #errorfile.close()

"""
    def fileInqGregorian():
            valuesDict= dict()
            api_url = 'https://customer.bmiapis.ir/api/icms/v1/individual/tracking/inquiry'
            with open("D:/new 4.txt") as file:
                input = file.readlines()
            input = [input[x].strip() for x in range(len(input))]
            headers = {'Content-Type': 'application/json' ,
            'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTA4MDM4MDU0NDUsIm5iZiI6MTY5MDcxNzQwNTQ0NSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUxIiwic2VyaWFsIjoiNDgwODI5NGEtMjU0Ni0zZTMyLThmNjEtMzQwY2I5YzZjMmRlIiwic3NuIjoiMDQyMDUyNTQwOCIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJpY21zLXNpYmEtY3VzdG9tZXIiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJub2NyLWRlY2Vhc2VkLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.wUDUKhbaeDSeSQbLK7ojafEwe1hfR77NSdYhADALA64'}
            for i in range(len(input)):
                if (input[i][0] != ','):
                    nationalCode = input[i][1:11]
                    try:
                        year = int(input[i][14:18])
                        month = int(input[i][19:21])
                        day = int(input[i][22:24])
                        myDate = JalaliDate(year=year , month=month , day=day).to_gregorian().isoformat()
                        valuesDict[nationalCode] = myDate                    
                    except Exception as myEX:
                        print(myEX)
                        with open("D:/convertedTimeError.csv","a") as fileError:
                            fileError.write(f'{nationalCode,input[i][14:24]}\n')
            for key in valuesDict.keys():
                data={"nationalIdentifier":key,"birthDate":valuesDict[key],"online":"false","acceptDays":"31"}
                response = requests.post(api_url,headers=headers,json=data , verify=False)
                if (response.status_code == 200 ):
                    print(i , "is successful for ", nationalCode)
                    with open("D:/success_result.csv","a") as filesuccess:
                        filesuccess.write(f'{nationalCode};{response.status_code};{response.content} \n')
                        print(f'{nationalCode};{response.status_code};{response.content} \n')
                else:
                    print("i is error" , i)
                    with open("D:/error_result.csv","a") as errorfile:
                        errorfile.write(f'{nationalCode};{response.status_code};{response.content}\n')
                        print(f'{nationalCode};{response.status_code};{response.content}\n')
      
if __name__ == '__main__':
    # define host and port numbers to scan
    # test the ports
    NocrOprInqClass.fileInqGregorian()
        """   
if __name__ == '__main__':
    NocrOprInqClass.fileInq()
