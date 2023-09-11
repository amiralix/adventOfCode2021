import requests
import threading
from persiantools.jdatetime import JalaliDate
from colorama import Fore, Back, Style

class shahabInquiry:
    def __init__(self) -> None:
        pass

    def inquiryInMemory(self):
        headers = {'Content-Type': 'application/json','Authorization':f'bearer {self.token}'}     
        dataOnline={"nationalCode":self.natCode,"birthDate":self.bDate,"issueNumber":str(self.shenasnameNo),"online":"true"}
        dataOffline={"nationalCode":self.natCode,"birthDate":self.bDate,"issueNumber":str(self.shenasnameNo),"online":"false"}
        try:
            response = requests.post(self.api_url ,headers=headers ,json=dataOffline, verify=False , timeout=5)
            '''if response.status_code == 200:
                print(f'first Inquiry for  successful natcode {self.natCode}')
                #time.sleep(1)
                #response = requests.post(self.api_url ,headers=headers ,json=dataOffline, verify=False , timeout=5)
            else:
                response = requests.post(self.api_url ,headers=headers ,json=dataOffline, verify=False , timeout=5)'''
            if response.status_code != 200:
                print(Fore.RED , self.natCode , response.content)
        except Exception as myEX:
            print(myEX)

    def inquiry4Items(natCode, bdate, shenasnameNo, inquiryType, access_token):
        try:   
            #api_url = 'http://192.168.234.194:9080/api/icms/v1/iranian/individual/shahab/inquiry'
            api_url =  'http://192.168.34.37:9033/api/nahab/v1/iranian/individual/shahab/inquiry'
            headers = {'Content-Type': 'application/json','Authorization':f'Bearer {access_token}'}     
            data={"postalCode":"","callerUnitCode":"rayan-icms-client","branchCode":"1031",
                        "userIdentificationNo":"0011001100","nationalCode":natCode,"birthDate":bdate,
                                "issueNumber":int(float(shenasnameNo)),"online":inquiryType}
            #data={"nationalCode":natCode,"birthDate":bdate,"issueNumber":int(float(shenasnameNo)),"online":inquiryType}
            #print(data)
            response = requests.post(api_url ,headers=headers ,json=data, verify=False , timeout=50)
            if response.status_code == 200:
                print(Fore.WHITE ,f'ok {natCode}')#by {threading.current_thread().name}')
                #print(response)
                return response.status_code, response.json()
            else: 
                #print(Fore.RED , f'SHAHAB for natcode {natCode} failed for {response.status_code} ' )
                print(Fore.RED ,f'NOK for {natCode}')# by {threading.get_native_id()} because of {response.status_code}')
                #print(response)
                return response.status_code, response.json()
        except :
            print(f"exception occured in calling ")
      
    '''
    def inquiryFida(fidaCode ,idNumber , birthdate , birthCountry , inquiryType):
            api_url = 'http://192.168.34.176:32321/api/icms/v1/foreign/individual/shahab/inquiry'
            headers = {'Content-Type': 'application/json','Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoia2V5IiwiZXhwIjoxNjkxODcyMDMwOTc2LCJuYmYiOjE2OTE3ODU2MzA5NzYsInJvbGUiOiIiLCJzZXJpYWwiOiJjNjA3MTNlNS0yOTI2LTNkYWUtOWVlMy02OWU5MjVkYTUxZDYiLCJzc24iOiIxMjMiLCJjbGllbnRfaWQiOiIxMjMiLCJzY29wZXMiOlsiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiYWNjb3VudC1zdXBlciIsInN2Yy1tZ210LWFnZy1hY2MtcGFydC1wZXJjLWluZm8iLCJzdmMtbWdtdC1zdG10LXN1cC1pbmZvIiwiY3VzdG9tZXItc3VwZXIiLCJpY21zLW5vY3ItdHJhY2tpbmctaW5xdWlyeSIsInJlY2VpdmUtc21zIl19.mCP670onmfprmbqJPQR4_H5JVYcv1bTaT7CwGCOsvG0'}     
            data={"foreignNationalCode":fidaCode,"identificationDocumentNumber":idNumber,"birthDate":birthdate,"birthCounrtyId":birthCountry,"online":inquiryType}
            response = requests.post(api_url ,headers=headers ,json=data, verify=False , timeout=50)
            if response.status_code == 200:
                print(f'SHAHAB Inquiry for  successful fidfaCode {natCode}')
            #   time.sleep(1)
            #  response = requests.post(self.api_url ,headers=headers ,json=dataOffline, verify=False , timeout=5)
                return response.json
            else: 
                print(f'SHAHAB for natcode {natCode} failed for {response.status_code} ' )
       '''     
    

""""
    def fileInq(self):
        with open("D:/inq.csv") as file:
            input = file.readlines()
        input = [input[x].strip() for x in range(len(input))]
        headers = {'Content-Type': 'application/json' ,
        'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2ODcyNTcwNzk5OTMsIm5iZiI6MTY4NzE3MDY3OTk5Mywicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWFkbWluaXN0cmF0b3IiLCJzZXJpYWwiOiI1ZDFjMmQyOC0xYTM4LTM3NjQtYTFhNy1jZmI2MTYzOTlkNDIiLCJzc24iOiIwMDY3NTQ1ODgyIiwiY2xpZW50X2lkIjoiMTM3MiIsInNjb3BlcyI6WyJzY3YtbWdtdC1iYXNpYy1maWRhIiwiZmlkYS1sZWdhbC1zY29wZSIsImljbXMtZmlkYS1sZWdhbCIsImN1c3RvbWVyIiwiaWNtcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzZXJ2aWNlcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLXNjb3BlIiwiaWNtcy1pbmRpdmlkdWFsLXJlcXVpcmVtZW50IiwiZmlkYS1yZWFsLXNjb3BlIiwic3ZjLW1nbXQtZmlkYSIsInN2Yy1tZ210LWFjYy1jdXN0LW51bXMtYWNjLW51bXMiLCJzdmMtc2hhaGthci1pbnF1aXJ5IiwiaWNtcy1mb3VuZGF0aW9uLWNiaSIsImN1c3RvbWVyLXJlZ2lzdGVyIiwiaWNtcy1zaWJhLWN1c3RvbWVyIiwiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiaWNtcy1sZWdhbC1pbnF1aXJ5IiwicG9zdC1hcHAtc2NvcGUiLCJpY21zLWZvdW5kYXRpb24taW5xdWlyeSIsImljbXMtcG9veWEtY3VzdG9tZXIiLCJzdmMtc2hhaGthci1kb21haW4iLCJjaXZpbC1yZWdpc3RyYXRpb24taW5xdWlyeSIsInN2Yy1tZ210LXBlcnNvbi1pbnF1aXJ5Iiwibm9jci1kZWNlYXNlZC1pbnF1aXJ5Iiwic2VydmljZXMtbmFoYWItaW5xdWlyeSIsImljbXMtYmFtLWVucm9sbG1lbnQiLCJzdmMtbWdtdC1icmFuY2gtaW5mby1jaGciLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLWlucXVpcnktc2NvcGUiLCJzY3YtbWdtdC1maWRhIiwiaWNtcy1maWRhLXJlYWwiLCJhY2NvdW50IiwiaWNtcy1zZXJ2aWNlLWJhc2ljLXJlYWQiLCJsZWdhbC1wZXJzb24tc2NvcGUiLCJvcmdhbml6YXRpb24tZnVuZGluZy1pbnF1aXJ5LXNjb3BlIiwic2VydmljZXMtc2hhaGFiLWlzc3VlIiwiaWNtcy12YWxpZGF0aW9uLWFkdmFuY2VkLWlucXVpcnkiLCJpY21zLXBvc3QtaW5xdWlyeSIsImRlY2Vhc2VkLXBlb3BsZS1pbnF1aXJ5Il19.X4_vdXnKNXyXzxNtTtTytt8RAiMHERaEFKKYu414MDk'}
        for i in range(len(input)):
            if (input[i][0] != ','):
                data={"nationalIdentifier":input[i][0:10],"birthDate":input[i][11:22],"online":"true","acceptDays":"1"}
                response = requests.post(self.api_url,headers=headers,json=data , verify=False)
                if (response.status_code == 200 ):
                    print(i , "is successful for ", input[i][0:10])
                    with open("D:/3success_result.csv","a") as filesuccess:
                        filesuccess.write(f'{input[i][0:10]};{input[i][11:22]};{response.status_code};{response.content} \n')
                else:
                    print("i is error" , i)
                    with open("D:/error_result.csv","a") as errorfile:
                        errorfile.write(f'{input[i][0:10]};{input[i][11:22]};{response.status_code};{response.content}\n')
        filesuccess.close()
        errorfile.close()

    def fileInqGregorian():
            valuesDict= dict()
            api_url = 'https://customer.bmiapis.ir/api/icms/v1/individual/tracking/inquiry'
            with open("D:/new 4.txt") as file:
                input = file.readlines()
            input = [input[x].strip() for x in range(len(input))]
            headers = {'Content-Type': 'application/json' ,
            'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2ODc2NzE1NzgzODksIm5iZiI6MTY4NzU4NTE3ODM4OSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiNTY4ZjJlNjAtNTg5ZS0zNzZlLTg5ZmMtN2E4YTg5NGVhYjIzIiwic3NuIjoiMzExMDIwNzQxOSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJpY21zLXNpYmEtY3VzdG9tZXIiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJub2NyLWRlY2Vhc2VkLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.1jTsd6JpJzdOp4c0oDP_ToWsnjSmfl7Mq6-sW5B8tDc'}
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
    """  
        
    