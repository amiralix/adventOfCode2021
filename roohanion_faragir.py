import pandas as pd
import requests
from colorama import Fore, Back, Style

class rooahanioon_faragir:
    data = pd.read_csv("d:/fidaCodes.csv")
    file = open("d:/ErrorRoohanioonFaragir.txt","a")
    fida_shahab_inq_url = ''



    def inq(fidaCode):
        headers_fida = {'Content-Type': 'application/json' ,
           'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTE2NDU0MzM0ODksIm5iZiI6MTY5MTU1OTAzMzQ4OSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiMzA4MzM3NzAtOTM4My0zNmRjLWI5ZjUtM2I2MDM4YWFmYzgxIiwic3NuIjoiMDkzODA3NzE0NyIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.NF7jV69NjP6bBwIzmeJ8GPQqNw6yHGuJ5u1ibp1OvFA'}    
        fida_inq_url = 'http://192.168.34.176:32321/api/icms/v1/fida/inquiry/foreign/person/real'
        fida_json_request = {"fidaCode":fidaCode.rjust(12,"0"),"online":"false","acceptDays":"1"}
        fida_response = requests.post(fida_inq_url ,headers=headers_fida ,json=fida_json_request,verify=False )
        if fida_response.status_code == 200 :
                print(fida_json_request)
                print(Fore.WHITE, f"fida Inquiry successful  for ",fidaCode )
        else:
                print(Fore.RED, f"fida Inquiry unsuccessful  for ",fidaCode,fida_response)
                #file.write(f"{fidaCode}\n + {fida_response.status_code}" )
            #else:
            #   print(f"cif Inquiry successful  for ",fida_code)
        #    jsonResponse = cif_response.json()


    def shahbInq(fidaCode , idDoc , birthDate , birthCountry,inquirtType):
        fida_shahab_inq_url = 'http://192.168.34.62:32321/api/icms/v1/foreign/individual/shahab/inquiry'
        headers_shahab_fida = {'Content-Type': 'application/json' ,
           'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTE5OTY5MTE5NDAsIm5iZiI6MTY5MTkxMDUxMTk0MCwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWFkbWluaXN0cmF0b3IiLCJzZXJpYWwiOiI4Njk5OTk1OS1lY2UxLTM4ZmQtYjlhMS04MDYyMTNjOTk4NTYiLCJzc24iOiIwODcwMzUyMTU2IiwiY2xpZW50X2lkIjoiMTM3MiIsInNjb3BlcyI6WyJzY3YtbWdtdC1iYXNpYy1maWRhIiwiZmlkYS1sZWdhbC1zY29wZSIsImljbXMtZmlkYS1sZWdhbCIsImN1c3RvbWVyIiwiaWNtcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzZXJ2aWNlcy1ub2NyLXRyYWNraW5nLWlucXVpcnkiLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLXNjb3BlIiwiaWNtcy1pbmRpdmlkdWFsLXJlcXVpcmVtZW50IiwiZmlkYS1yZWFsLXNjb3BlIiwic3ZjLW1nbXQtZmlkYSIsInN2Yy1tZ210LWFjYy1jdXN0LW51bXMtYWNjLW51bXMiLCJzdmMtc2hhaGthci1pbnF1aXJ5IiwiaWNtcy1mb3VuZGF0aW9uLWNiaSIsImljbXMtc2liYS1jdXN0b21lciIsImN1c3RvbWVyLXJlZ2lzdGVyIiwiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiaWNtcy1sZWdhbC1pbnF1aXJ5IiwicG9zdC1hcHAtc2NvcGUiLCJpY21zLWZvdW5kYXRpb24taW5xdWlyeSIsImljbXMtcG9veWEtY3VzdG9tZXIiLCJzdmMtc2hhaGthci1kb21haW4iLCJjaXZpbC1yZWdpc3RyYXRpb24taW5xdWlyeSIsInN2Yy1tZ210LXBlcnNvbi1pbnF1aXJ5Iiwic2VydmljZXMtbmFoYWItaW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsImljbXMtYmFtLWVucm9sbG1lbnQiLCJzdmMtbWdtdC1icmFuY2gtaW5mby1jaGciLCJzdmMtY29udGFjdC12YWxpZGF0aW9uLWlucXVpcnktc2NvcGUiLCJzY3YtbWdtdC1maWRhIiwiaWNtcy1maWRhLXJlYWwiLCJhY2NvdW50IiwiaWNtcy1zZXJ2aWNlLWJhc2ljLXJlYWQiLCJsZWdhbC1wZXJzb24tc2NvcGUiLCJvcmdhbml6YXRpb24tZnVuZGluZy1pbnF1aXJ5LXNjb3BlIiwic2VydmljZXMtc2hhaGFiLWlzc3VlIiwiaWNtcy12YWxpZGF0aW9uLWFkdmFuY2VkLWlucXVpcnkiLCJpY21zLXBvc3QtaW5xdWlyeSIsImRlY2Vhc2VkLXBlb3BsZS1pbnF1aXJ5Il19.JUwihshyxwMXs54XkrP7RV4tatIarmBaJrR0nv-Skyk'}    
        if inquirtType == True:
                data = {"foreignNationalCode":fidaCode.rjust(12,"0"),
                                        "identificationDocumentNumber":idDoc,
                                        "birthDate":birthDate,
                                        "birthCounrtyId":birthCountry,
                                        "online":"true",
                                        "postalCode":""
                                }
        else: data = {"foreignNationalCode":fidaCode.rjust(12,"0"),
                                        "identificationDocumentNumber":idDoc,
                                        "birthDate":birthDate,
                                        "birthCounrtyId":birthCountry,
                                        "online":"false",
                                        "postalCode":""
                                }
        fida_shahab_response = requests.post(url=fida_shahab_inq_url ,headers=headers_shahab_fida ,json=data,verify=False )
        if fida_shahab_response.status_code == 200:
            print(f'SHAHAB Inquiry for  successful for fidaCode {fidaCode} ')
         #   time.sleep(1)
          #  response = requests.post(self.api_url ,headers=headers ,json=dataOffline, verify=False , timeout=5)
            return fida_shahab_response.status_code, fida_shahab_response.json()
        else: 
            print(f'SHAHAB for fidaCode {fidaCode} failed for {fida_shahab_response.status_code} ' )
            

        """"
        if fida_shahab_response.status_code == 200 :
                print(fida_shahab_response)
                print(Fore.WHITE, f"fida shahab Inquiry successful  for ",fidaCode )
        else:
                print(Fore.RED, f"fida shahab Inquiry unsuccessful  for ",fidaCode,fida_shahab_response)
        return fida_shahab_response.status_code
        """

