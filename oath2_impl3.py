import requests
import json
import jwt
import base64
import datetime 
from shahabInquiry3 import *
from FidaInquiry import *
# SSO server configuration

class TokenManager3:   
    token = ''  
#    def __init__(self):
 #       self.token = self.getToken()

    def getToken(self):
        if (self.token_has_expired()):
            self.refresh_token()
        return self.token

    def getNew_token(self):      
        # Step 1: Redirect the user to the SSO server for authorization
        authorization = 'rayan-icms-client:cB1rF1sD3hI8hB5fC5hD3tD1fC5bC6eF1qQ1lB7gF9'
        auth_base64 = (base64.b64encode(authorization.encode())).decode('utf-8')
        headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':f'Basic {auth_base64}'}
        data={"grant_type":'client_credentials',"scope":'icms-nahab-inquiry'}
        response = requests.post(url= 'http://192.168.107.2:9080/identity/oauth2/auth/token' ,headers= headers , data=data , timeout=50)
        if response.status_code == 200:
            Tokken = (json.loads((response._content).decode('utf-8')))['access_token']   
            return Tokken
        else : pass       
    
    def getNew_tokenScope(self,scope):      
        # Step 1: Redirect the user to the SSO server for authorization
        authorization = 'rayan-icms-client:cB1rF1sD3hI8hB5fC5hD3tD1fC5bC6eF1qQ1lB7gF9'
        auth_base64 = (base64.b64encode(authorization.encode())).decode('utf-8')
        headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':f'Basic {auth_base64}'}
        data={"grant_type":'client_credentials',"scope":f'{scope}'}
        response = requests.post(url= 'http://192.168.107.2:9080/identity/oauth2/auth/token' ,headers= headers , data=data)
        if response.status_code == 200:
            Tokken = (json.loads((response._content).decode('utf-8')))['access_token']   
            return Tokken
        else : pass     
    
    def token_has_expired(self):
        try:
            decoded_token = jwt.decode( self.token, algorithms="HS256" , options={"verify_signature": False})
            exp_timestamp = decoded_token['exp']
            exp_datetime = datetime.datetime.fromtimestamp(exp_timestamp/1000)
            current_datetime = datetime.datetime.now()
            return current_datetime > exp_datetime
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return True

        '''
    def token_expired_check(token):
        try:
            decoded_token = jwt.decode(token, verify=False)
            exp_timestamp = decoded_token['exp']
            exp_datetime = datetime.datetime.fromtimestamp(exp_timestamp)
            current_datetime = datetime.datetime.now()
            return current_datetime > exp_datetime
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return True
        '''
    def refresh_token(self):
        self.token = self.getNew_token()    

    def call_service(self , natCode ,bdate , shenasnameNo, inquiryType,access_token):
        return shahabInquiry3().inquiry4Items(natCode,bdate,shenasnameNo,inquiryType,access_token)    
        
    def call_service_legal(self , natCode ,bdate , regNo, inquiryType,access_token):
        return shahabInquiry3.inquiryIraninanLegal(natCode ,bdate , regNo,inquiryType,access_token=access_token)    
        
    def call_service_real_foreign(self ,foreignNationalCode ,identificationDocumentNumber,birthCounrtyId ,birthDate ,inquiryType):
        fidaInquiryResponse = FidaInquiry().inquiry4Real(fidaCode=foreignNationalCode , inquiryType=inquiryType , access_token= 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTg3NDU3OTA4ODEsIm5iZiI6MTY5ODY1OTM5MDg4MSwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiNDI5Y2RkNmYtNTBiNS0zNjBhLWI4NjItYzg2MWEyOTU4MWFjIiwic3NuIjoiMTM4MDgxMTM0MSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtc2liYS1jdXN0b21lciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsIm5vY3ItZGVjZWFzZWQtaW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.VWCdIgukSjsnmaqe1OjA03DADaae0JalCqRgMI0QeJc')    
        #if fidaInquiryResponse[0] == '200':
        return shahabInquiry3().inquiryForeignReal(foreignNationalCode, identificationDocumentNumber , birthCounrtyId ,birthDate , inquiryType, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkFVVEhfQ09ERSIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTg3MjUxMzQ1NDIsIm5iZiI6MTY5ODYzODczNDU0Miwicm9sZSI6InJheWFuLWljbXMtY2xpZW50LWxpbmUyIiwic2VyaWFsIjoiNjRiMGUwMjEtNmNiYy0zNGUxLTg5M2EtMjM4NGUxNTFmOTFlIiwic3NuIjoiNTg1OTg4NzU0MSIsImNsaWVudF9pZCI6IjEzNzIiLCJzY29wZXMiOlsic2N2LW1nbXQtYmFzaWMtZmlkYSIsImZpZGEtbGVnYWwtc2NvcGUiLCJpY21zLWZpZGEtbGVnYWwiLCJjdXN0b21lciIsImljbXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsImljbXMtaW5kaXZpZHVhbC1yZXF1aXJlbWVudCIsImZpZGEtcmVhbC1zY29wZSIsInN2Yy1tZ210LWZpZGEiLCJzdmMtbWdtdC1hY2MtY3VzdC1udW1zLWFjYy1udW1zIiwic3ZjLXNoYWhrYXItaW5xdWlyeSIsImljbXMtZm91bmRhdGlvbi1jYmkiLCJpY21zLXNpYmEtY3VzdG9tZXIiLCJjdXN0b21lci1yZWdpc3RlciIsImljbXMtbmFoYWItaW5xdWlyeSIsImljbXMtbGVnYWwtaW5xdWlyeSIsInBvc3QtYXBwLXNjb3BlIiwiaWNtcy1mb3VuZGF0aW9uLWlucXVpcnkiLCJpY21zLXBvb3lhLWN1c3RvbWVyIiwic3ZjLXNoYWhrYXItZG9tYWluIiwiY2l2aWwtcmVnaXN0cmF0aW9uLWlucXVpcnkiLCJzdmMtbWdtdC1wZXJzb24taW5xdWlyeSIsInNlcnZpY2VzLW5haGFiLWlucXVpcnkiLCJub2NyLWRlY2Vhc2VkLWlucXVpcnkiLCJpY21zLWJhbS1lbnJvbGxtZW50Iiwic3ZjLW1nbXQtYnJhbmNoLWluZm8tY2hnIiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1pbnF1aXJ5LXNjb3BlIiwic2N2LW1nbXQtZmlkYSIsImljbXMtZmlkYS1yZWFsIiwiYWNjb3VudCIsImljbXMtc2VydmljZS1iYXNpYy1yZWFkIiwibGVnYWwtcGVyc29uLXNjb3BlIiwib3JnYW5pemF0aW9uLWZ1bmRpbmctaW5xdWlyeS1zY29wZSIsInNlcnZpY2VzLXNoYWhhYi1pc3N1ZSIsImljbXMtdmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5IiwiaWNtcy1wb3N0LWlucXVpcnkiLCJkZWNlYXNlZC1wZW9wbGUtaW5xdWlyeSJdfQ==.YPMz4jr28MVHhUQea78TVFmn6KpT4WQnvfadpfGfk9Q')     # type: ignore
        #else: print("unsuccessful fida inquiry")




'''In this code, the `authenticate_with_sso` function handles the Authorization Code Flow with the SSO server. It prompts the user to visit the authorization URL, enter the authorization code, and then exchanges it for an access token.
If the authentication with the SSO server fails, the code falls back to the `authenticate_with_secondary` function, where you can implement your own secondary authentication logic. In this example, it simply checks if the provided username and password match the fallback credentials.
You can add your own code and logic after obtaining the authentication token from either the SSO server or the secondary method.
''' 