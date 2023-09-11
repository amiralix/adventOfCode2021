import requests
import threading
from persiantools.jdatetime import JalaliDate
from colorama import Fore

class NocrOprInqClass:
    def __init__(self , nationalCode , birthdate):
        self.natCode = nationalCode
        self.bDate = birthdate
        api_url = 'https://customer.bmiapis.ir/api/icms/v1/individual/tracking/inquiry'
        file = 'd:/error_pishgaman.txt'

    def inquiry(self):
        headers = {'Content-Type': 'application/json' ,
        'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTE2NDE0NTU5MDgsIm5iZiI6MTY5MTU1NTA1NTkwOCwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiZTQwMTBlZjMtZDA1Zi0zNzNlLWFiMjItZTllYzVjNjRiMDhkIiwic3NuIjoiNDQzMjY4NTg3NSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.8wLqlgm4Mr7hUbyCfG9wJEt1chQGT6D2CfoWp1tcMkE'}
        data={"nationalIdentifier":self.natCode,"birthDate":self.bDate,"online":"true","acceptDays":"1"}
        response = requests.post(self.api_url,headers=headers,json=data , verify=False , timeout=50)
        return response

    def inquiry(mellicode ,bdate):
        api_url = 'http://192.168.34.176:32321/api/icms/v1/individual/tracking/inquiry'
        headers = {'Content-Type': 'application/json' ,'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTI1MTY0OTU1NTcsIm5iZiI6MTY5MjQzMDA5NTU1Nywicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWFkbWluaXN0cmF0b3IiLCJzZXJpYWwiOiI1MjcxODJhZi0zOTgyLTM1NWItOTdlOS02NjI3ZWMwM2U1OTAiLCJzc24iOiI0NjA5MzgwNjc2IiwiY2xpZW50X2lkIjoiMTM3MiIsInNjb3BlcyI6WyJzY3YtbWdtdC1iYXNpYy1maWRhIiwiZmlkYS1sZWdhbC1zY29wZSIsImljbXMtZmlkYS1sZWdhbCIsImN1c3RvbWVyIiwiaWNtcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzZXJ2aWNlcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLXNjb3BlIiwiaWNtcy1pbmRpdmlkdWFsLXJlcXVpcmVtZW50IiwiZmlkYS1yZWFsLXNjb3BlIiwic3ZjLW1nbXQtZmlkYSIsInN2Yy1tZ210LWFjYy1jdXN0LW51bXMtYWNjLW51bXMiLCJzdmMtc2hhaGthci1pbnF1aXJ5IiwiaWNtcy1mb3VuZGF0aW9uLWNiaSIsImljbXMtc2liYS1jdXN0b21lciIsImN1c3RvbWVyLXJlZ2lzdGVyIiwiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiaWNtcy1sZWdhbC1pbnF1aXJ5IiwicG9zdC1hcHAtc2NvcGUiLCJpY21zLWZvdW5kYXRpb24taW5xdWlyeSIsImljbXMtcG9veWEtY3VzdG9tZXIiLCJzdmMtc2hhaGthci1kb21haW4iLCJjaXZpbC1yZWdpc3RyYXRpb24taW5xdWlyeSIsInN2Yy1tZ210LXBlcnNvbi1pbnF1aXJ5Iiwic2VydmljZXMtbmFoYWItaW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsImljbXMtYmFtLWVucm9sbG1lbnQiLCJzdmMtbWdtdC1icmFuY2gtaW5mby1jaGciLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLWlucXVpcnktc2NvcGUiLCJzY3YtbWdtdC1maWRhIiwiaWNtcy1maWRhLXJlYWwiLCJhY2NvdW50IiwiaWNtcy1zZXJ2aWNlLWJhc2ljLXJlYWQiLCJsZWdhbC1wZXJzb24tc2NvcGUiLCJvcmdhbml6YXRpb24tZnVuZGluZy1pbnF1aXJ5LXNjb3BlIiwic2VydmljZXMtc2hhaGFiLWlzc3VlIiwiaWNtcy12YWxpZGF0aW9uLWFkdmFuY2VkLWlucXVpcnkiLCJpY21zLXBvc3QtaW5xdWlyeSIsImRlY2Vhc2VkLXBlb3BsZS1pbnF1aXJ5Il19.FEW88syiOxG9XrRs-qnlJwVsITz0tXRgGj-0GFJCeoE'}     
        data={"nationalIdentifier":mellicode,"birthDate":bdate,"online":'false',"acceptDays":"180"}
        response = requests.post(api_url ,headers=headers ,json=data, verify=False , timeout=50)
        if response.status_code == 200:
            print(Fore.WHITE ,f'for natcode {mellicode} successful' )
            return response
        else: 
            #print(f'for natcode {mellicode} failed by {threading.get_native_id()} because of {response.status_code}' )
            #print(f'for natcode {mellicode} failed because of {response.status_code}' )
            #print('for natcode ',mellicode,'failed because of',response.json()['error']['code'] )
            print(Fore.RED,'for', {mellicode} ,{bdate} ,'response NOCR is ',response.json()['error']['code'] ,response.json()['error']['errors'] )
            return response
            

    def fileInq(self):
        with open("D:/inq.csv") as file:
            input = file.readlines()
        input = [input[x].strip() for x in range(len(input))]
        headers = {'Content-Type': 'application/json' ,
        'Authorization':'bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTA4MDM4MDU0NDUsIm5iZiI6MTY5MDcxNzQwNTQ0NSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUxIiwic2VyaWFsIjoiNDgwODI5NGEtMjU0Ni0zZTMyLThmNjEtMzQwY2I5YzZjMmRlIiwic3NuIjoiMDQyMDUyNTQwOCIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJpY21zLXNpYmEtY3VzdG9tZXIiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJub2NyLWRlY2Vhc2VkLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.wUDUKhbaeDSeSQbLK7ojafEwe1hfR77NSdYhADALA64'}
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
    