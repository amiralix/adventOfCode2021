import requests
import json
import jwt
import base64
import datetime 
from shahabInquiry3 import *

# SSO server configuration

class TokenManager3:   
    token = ''  
    def __init__(self):
        self.token = self.getToken()

    def getToken(self):
        if (self.token_has_expired()):
            self.refresh_token()
        return self.token

    def getNew_token(self):      
        # Step 1: Redirect the user to the SSO server for authorization
        authorization = 'rayan-icms-client:cB1rF1sD3hI8hB5fC5hD3tD1fC5bC6eF1qQ1lB7gF9'
        auth_base64 = (base64.b64encode(authorization.encode())).decode('utf-8')
        headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':f'Basic {auth_base64}'}
        data={"grant_type":'client_credentials',"scope":'civil-registration-inquiry'}
        response = requests.post(url= 'http://192.168.107.2:9080/identity/oauth2/auth/token' ,headers= headers , data=data)
        if response.status_code == 200:
            Tokken = (json.loads((response._content).decode('utf-8')))['access_token']   
            return Tokken
        else : pass       
    
    ''' 
    def getSaved_token(self):
       
       self.token =  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTMyMzYxNDY0MDYsIm5iZiI6MTY5MzE0OTc0NjQwNiwicm9sZSI6IiIsInNlcmlhbCI6ImVkM2MzNDU2LTlmOGQtMzY4OC1hOTU5LWUyNzFiYmNlYTQ4MiIsInNzbiI6IjEzNzIiLCJjbGllbnRfaWQiOiIxMzcyIiwic2NvcGVzIjpbInNjdi1tZ210LWJhc2ljLWZpZGEiLCJmaWRhLWxlZ2FsLXNjb3BlIiwidmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5LXNjb3BlIiwic3ZjLW1nbXQtcHJzbmwtaW5mbyIsIm5lc2hhbi1kYXRhLWFjY2VzcyIsImljbXMtcG9veWEtY3VzdG9tZXIiLCJjaXZpbC1yZWdpc3RyYXRpb24taW5xdWlyeSIsImN1c3RvbWVyIiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsInN2Yy1tZ210LXBlcnNvbi1pbnF1aXJ5IiwiZmlkYS1yZWFsLXNjb3BlIiwic3ZjLW1nbXQtaW5kaXZpZHVhbC1jdXN0b21lci1hY2NvdW50cy1pbmZvIiwibmVzaGFuLWFsbG93LWFjY2VzcyIsInN2Yy1jb250YWN0LXZhbGlkYXRpb24taW5xdWlyeS1zY29wZSIsInNjdi1tZ210LWZpZGEiLCJzdmMtbWdtdC1maWRhIiwiYmFhbS1iYXNlLWZvcmVpZ24tZW5yb2xsbWVudCIsImN1c3RvbWVyLXJlZ2lzdGVyIiwiaWNtcy1wb3N0LWlucXVpcnkiXX0=.WMvRqGsE5eUsjtcEaeoqaFxt0RvRUMAkZeq7CfpnqPg'
       return self.token
    ''' 
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
        shahabInquiry3.inquiry4Items(natCode ,bdate , shenasnameNo,inquiryType,access_token=access_token)    
        



'''In this code, the `authenticate_with_sso` function handles the Authorization Code Flow with the SSO server. It prompts the user to visit the authorization URL, enter the authorization code, and then exchanges it for an access token.
If the authentication with the SSO server fails, the code falls back to the `authenticate_with_secondary` function, where you can implement your own secondary authentication logic. In this example, it simply checks if the provided username and password match the fallback credentials.
You can add your own code and logic after obtaining the authentication token from either the SSO server or the secondary method.
''' 