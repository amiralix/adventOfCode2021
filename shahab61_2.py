from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import pandas as pd
from colorama import *
from termcolor import colored

myDictionary = {'natCode': [],'Bdate': [],'idDoc': []}
data = pd.read_csv("d:/NAHAB_TB_COMPARE_NOCR_result_edited3.csv")
    #check if birthdate is gregorian or persian . true means gregorian birth date   
print("read file completed")
english_date_default_flag = True
for rows in range(0,len(data)):
        str_melli_code = str(data.natCode[rows])
        str_melli_code = str_melli_code.rjust(10,'0')
        if english_date_default_flag == False :
            strPersianBirth = str(data.birthDate[rows])
            strGregBirth = JalaliDate(year=int(strPersianBirth[0:4]) , month=int(strPersianBirth[5:7]) , day=int(strPersianBirth[8:10])).to_gregorian().isoformat()
        else:
            strGregBirth = str(data.birthDate[rows])    
        str_shenasnameNo = str(data.idDoc[rows])
        if (str_shenasnameNo == 'nan'):
                str_shenasnameNo = 0
        shahabinq = shahabInquiry.inquiry4Items(natCode=str_melli_code , bdate=strGregBirth , shenasnameNo=str_shenasnameNo,inquiryType='true',access_token='eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJncmFudCI6IkNMSUVOVCIsImlzcyI6Imh0dHA6Ly9hcGkuYm1pLmlyL3NlY3VyaXR5IiwiYXVkIjoicmF5YW4taWNtcy1jbGllbnQiLCJleHAiOjE2OTMyMzYxNDY0MDYsIm5iZiI6MTY5MzE0OTc0NjQwNiwicm9sZSI6IiIsInNlcmlhbCI6ImVkM2MzNDU2LTlmOGQtMzY4OC1hOTU5LWUyNzFiYmNlYTQ4MiIsInNzbiI6IjEzNzIiLCJjbGllbnRfaWQiOiIxMzcyIiwic2NvcGVzIjpbInNjdi1tZ210LWJhc2ljLWZpZGEiLCJmaWRhLWxlZ2FsLXNjb3BlIiwidmFsaWRhdGlvbi1hZHZhbmNlZC1pbnF1aXJ5LXNjb3BlIiwic3ZjLW1nbXQtcHJzbmwtaW5mbyIsIm5lc2hhbi1kYXRhLWFjY2VzcyIsImljbXMtcG9veWEtY3VzdG9tZXIiLCJjaXZpbC1yZWdpc3RyYXRpb24taW5xdWlyeSIsImN1c3RvbWVyIiwic2VydmljZXMtbm9jci10cmFja2luZy1pbnF1aXJ5Iiwic3ZjLWNvbnRhY3QtdmFsaWRhdGlvbi1zY29wZSIsInN2Yy1tZ210LXBlcnNvbi1pbnF1aXJ5IiwiZmlkYS1yZWFsLXNjb3BlIiwic3ZjLW1nbXQtaW5kaXZpZHVhbC1jdXN0b21lci1hY2NvdW50cy1pbmZvIiwibmVzaGFuLWFsbG93LWFjY2VzcyIsInN2Yy1jb250YWN0LXZhbGlkYXRpb24taW5xdWlyeS1zY29wZSIsInNjdi1tZ210LWZpZGEiLCJzdmMtbWdtdC1maWRhIiwiYmFhbS1iYXNlLWZvcmVpZ24tZW5yb2xsbWVudCIsImN1c3RvbWVyLXJlZ2lzdGVyIiwiaWNtcy1wb3N0LWlucXVpcnkiXX0=.WMvRqGsE5eUsjtcEaeoqaFxt0RvRUMAkZeq7CfpnqPg')
        if shahabinq[0] == 200:
            print('success for',str_melli_code)
        else :       
            continue

        

