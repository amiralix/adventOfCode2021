from NocrOprInqClass import NocrOprInqClass
import pandas as pd
from persiantools.jdatetime import JalaliDate


with open("d:/resultBirthdate.csv",'w') as file:
    data = pd.read_csv("D:/conflict.csv")
    for rows in range(0,len(data)):
            nationalCode = str(data.melliCode[rows])
            nationalCode = int(float(nationalCode))
            nationalCode = str(nationalCode)
            nationalCode = nationalCode.rjust(10,"0")
            print(nationalCode)
            birthdate = str(data.bDate[rows])
            year = str(birthdate[0:4])
            month = str(birthdate[5:7])
            day = str(birthdate[8:10])
            myDate = JalaliDate( year=int(year) , month=int(month) , day=int(day)).to_gregorian().isoformat()
            file.write(f"update CRM.TB_INVOLVED_PARTY set BIRTH_DATE = '{myDate}' where NATIONAL_CODE_NATIONAL_ID = '{nationalCode}'\n")

