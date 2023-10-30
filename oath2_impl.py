import requests
import base64
import json
import jwt
import datetime
import time
import yaml
from shahabInquiry import *

# SSO server configuration

class TokenManager:   


    """ 
    def __init__(self):
        with open('multiThreadShahab.yaml') as yamlfile:
            yamlContent = yaml.safe_load(yamlfile)
        global  SSO_CLIENT_ID_TEST , SSO_CLIENT_SECRET_TEST , SSO_TOKEN_URL_TEST,SSO_GRANT_TYPE_TEST,SSO_CLIENT_SCOPE_TEST
        SSO_TOKEN_URL_TEST = yamlContent['address']['-yaml']['SSO_CLIENT_SECRET_TEST']
        SSO_CLIENT_SECRET_TEST = yamlContent['address']['-yaml']['SSO_CLIENT_SECRET_TEST']
        SSO_CLIENT_ID_TEST = yamlContent['address']['-yaml']['SSO_CLIENT_ID_TEST']
        SSO_GRANT_TYPE_TEST = yamlContent['address']['-yaml']['SSO_GRANT_TYPE_TEST']
        SSO_CLIENT_SCOPE_TEST = yamlContent['address']['-yaml']['SSO_CLIENT_SCOPE_TEST']

        self.token = self.get_token()
        self.token_timestamp = time.time()

    def get_token(self):      
        # Step 1: Redirect the user to the SSO server for authorization
        authorization = f'{SSO_CLIENT_ID_TEST}:{SSO_CLIENT_SECRET_TEST}'
        auth_base64 = (base64.b64encode(authorization.encode())).decode('utf-8')
        headers = {'Content-Type': 'application/x-www-form-urlencoded','Authorization':f'Basic {auth_base64}'}
        data={"grant_type":f'{SSO_GRANT_TYPE_TEST}',"scope":f'{SSO_CLIENT_SCOPE_TEST}'}
        response = requests.post(url= SSO_TOKEN_URL_TEST ,headers= headers , data=data )
        if response.status_code == 200:
            Tokken = (json.loads((response._content).decode('utf-8')))['access_token']   
            return Tokken
        else : pass       
    """
    
    def getToken(self):
       
       self.token =  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoia2V5IiwiZXhwIjoxNjk2ODkxMDE5MDY1LCJuYmYiOjE2OTY4MDQ2MTkwNjUsInJvbGUiOiIiLCJzZXJpYWwiOiIzYjI3ODcyOC1jZjVjLTM0MmItOWNjYy04NzlhY2JmYzMwOTIiLCJzc24iOiIxMjMiLCJjbGllbnRfaWQiOiIxMjMiLCJzY29wZXMiOlsiaWNtcy1uYWhhYi1pbnF1aXJ5IiwiYWNjb3VudC1zdXBlciIsInN2Yy1tZ210LWFnZy1hY2MtcGFydC1wZXJjLWluZm8iLCJzdmMtbWdtdC1zdG10LXN1cC1pbmZvIiwiY3VzdG9tZXItc3VwZXIiLCJpY21zLW5vY3ItdHJhY2tpbmctaW5xdWlyeSIsInJlY2VpdmUtc21zIl19.2Br4yrMy2KHrcorBvAq7mV2TMhqoh1fDIGMYZqpiRfU'
       return self.token
   
    def token_has_expired(self):
        try:
            decoded_token = jwt.decode(self.token, verify=False)
            exp_timestamp = decoded_token['expires_in']
            exp_datetime = datetime.datetime.fromtimestamp(exp_timestamp)
            current_datetime = datetime.datetime.now()
            return current_datetime > exp_datetime
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return True

    '''
    def refresh_token(self):
        global token, token_timestamp
        token = self.get_token()
        token_timestamp = time.time()
    '''
    def call_service(self , natCode ,bdate , shenasnameNo, inquiryType,access_token):
        #if self.token_has_expired():
         #   self.refresh_token()
        #else:pass
        #print('token is' , token ,'for thread id ' , threading.get_native_id())
        shahabInquiry.inquiry4Items(natCode ,bdate , shenasnameNo,inquiryType,access_token=access_token)
        




'''In this code, the `authenticate_with_sso` function handles the Authorization Code Flow with the SSO server. It prompts the user to visit the authorization URL, enter the authorization code, and then exchanges it for an access token.

If the authentication with the SSO server fails, the code falls back to the `authenticate_with_secondary` function, where you can implement your own secondary authentication logic. In this example, it simply checks if the provided username and password match the fallback credentials.

You can add your own code and logic after obtaining the authentication token from either the SSO server or the secondary method.
'''