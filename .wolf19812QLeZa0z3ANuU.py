from persiantools.jdatetime import JalaliDate
from shahabInquiry import shahabInquiry
import pandas as pd
from termcolor import colored
from oath2_impl3 import *

fileAdrs = 'D:/15000Result.txt'


def writeData2File(data):
    with open(fileAdrs, "a", closefd=True, newline='\n') as file:
        file.write(data)
        file.flush()


defaultAddress = 'C:/NAHAB_TB_COMPARE_NOCR_result2.csv'
# fileAddress = input("enter file path default is C:/NAHAB_TB_COMPARE_NOCR_result2.csv\n")
# if fileAddress == '':
fileAddress = defaultAddress
writeData2File(str(datetime.datetime.now())+'\n')
with open(fileAddress, 'r') as file:
    lineLIst = file.readlines()
lineListLenght = len(lineLIst)
print(f"reading File with {lineListLenght} rows ...")
token_manager = TokenManager3()
myShahabInquiry = shahabInquiry()
for lines in range(0, lineListLenght, 4):
    shahabinq1 = myShahabInquiry.inquiry4ItemsByUrl('http://192.168.239.231:9081/api/nahab/v1/iranian/individual/shahab/inquiry',
                                                    (str(
                                                        lineLIst[lines][0:10].rjust(10, '0'))),
                                                    (str(
                                                        lineLIst[lines][11:21])),
                                                    (int(
                                                        lineLIst[lines][38:len(lineLIst[lines])])),
                                                    'false',
                                                    (TokenManager3().getToken())
                                                    )
    shahabinq2 = myShahabInquiry.inquiry4ItemsByUrl('http://192.168.239.231:9080/api/nahab/v1/iranian/individual/shahab/inquiry',
                                                    str(lineLIst[lines+1]
                                                        [0:10].rjust(10, '0')),
                                                    str(lineLIst[lines+1]
                                                        [11:21]),
                                                    int(lineLIst[lines+1]
                                                        [38:len(lineLIst[lines+1])]),
                                                    'false',
                                                    token_manager.getToken()
                                                    )

    shahabinq3 = myShahabInquiry.inquiry4ItemsByUrl('http://192.168.239.230:9081/api/nahab/v1/iranian/individual/shahab/inquiry',
                                                    str(lineLIst[lines+2]
                                                        [0:10].rjust(10, '0')),
                                                    str(lineLIst[lines+2]
                                                        [11:21]),
                                                    int(lineLIst[lines+2]
                                                        [38:len(lineLIst[lines+2])]),
                                                    'false',
                                                    token_manager.getToken()
                                                    )

    shahabinq4 = myShahabInquiry.inquiry4ItemsByUrl('http://192.168.239.230:9080/api/nahab/v1/iranian/individual/shahab/inquiry',
                                                    str(lineLIst[lines+3]
                                                        [0:10].rjust(10, '0')),
                                                    str(lineLIst[lines+3]
                                                        [11:21]),
                                                    int(lineLIst[lines+3]
                                                        [38:len(lineLIst[lines+3])]),
                                                    'false',
                                                    token_manager.getToken()
                                                    )
    # type: ignore
    writeData2File(
        f'{json.dumps(shahabinq1)} \n {json.dumps(shahabinq2)} \n {json.dumps(shahabinq3)} \n {json.dumps(shahabinq4)} \n')
