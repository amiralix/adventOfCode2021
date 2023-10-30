import requests

class FidaInquiry:
    def __init__(self) -> None:
         pass
    
    def inquiry4Real(self,fidaCode):
        #    url_fida_core_inquiry = 'http://192.168.34.59:9010/api/fida/v1/real-person/inquiry'
            url_fida_core_inquiry = 'http://customer.bmiapis.ir/api/icms/v1/fida/inquiry/foreign/person/real'
            headers = {'Content-Type': 'application/json' ,'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTg3MzQyMjY5NzMsIm5iZiI6MTY5ODY0NzgyNjk3Mywicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiMzU5NGI5N2MtYzk4YS0zYjQ4LWJiYzItMjUyYmI2MTVjZmFjIiwic3NuIjoiNjUxOTQyODU1OCIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.6kiRssfCKWTs-igTMorsvYr1JVsUsN3SMfYP7WoxFck'}
            data={ "fidaCode":fidaCode,"online":'false',"acceptDays":180, "callerUnitCode":"rayan-icms-client","branchCode":"1031","callerNationalIdentifier":"0011001100"}
            response = requests.post(url_fida_core_inquiry ,headers=headers ,json=data, verify=False)
            if response.status_code == 200:
                print(response.status_code , response.json())
                return response.json()
            else: print(response.status_code , response.json())
            return response



