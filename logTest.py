import requests
from colorama import Fore
import csv
import logging

myLogger = logging.getLogger(__name__)
strealLoggingHandler = logging.StreamHandler()
strealLoggingHandler.setLevel(logging.INFO)
loggingFormatter = logging.Formatter('%(name)s  - %(levelname)s - %(message)s ')
strealLoggingHandler.setFormatter(loggingFormatter)
myLogger.addHandler(strealLoggingHandler)
with open('d:/new2.txt') as csv_file:
     nationalCodes = csv.reader(csv_file)
     for nationalCode in nationalCodes:
        api_url = 'http://customer.bmiapis.ir/api/icms/v1/customer-info/real/iranian/'+str(nationalCode[0])
        headers = {'Content-Type': 'application/json' ,
            'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicGlzaGdhbWFuLXBvdXlhIiwiZXhwIjoxNjkwMzc1NjQ1NTk4LCJuYmYiOjE2OTAyODkyNDU1OTgsInJvbGUiOiIiLCJzZXJpYWwiOiIyYmRjOTQyZS02MjYyLTNmZjItODNkNi0zODhjYzQ5YWNjOTQiLCJzc24iOiIxMTExMTExMTgiLCJjbGllbnRfaWQiOiIxMTExMTExMTgiLCJzY29wZXMiOlsiaWNtcy1jdXN0b21lci1pbnF1aXJ5Il19.BdUVOJq8iyvq20v0SkLBuolUNH6JxzJoc4xPRi-eiVg'}
        response = requests.get(api_url ,headers=headers , verify=False)
        if response.status_code == 200:
            pass
            #myLogger.info('success')
            #print(Fore.GREEN , response._content)
        else: 
            myLogger.error('error')
            #print(Fore.RED ,response.status_code)
