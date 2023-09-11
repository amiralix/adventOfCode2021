from persiantools.jdatetime import JalaliDate
from  NocrOprInqClass import NocrOprInqClass
with open("D:/new2.txt") as file:
    input = file.readlines()
input = [input[x].strip() for x in range(len(input))]
for i in range(0,len(input)):
    if (input[i][0] != ','):
        nationalCode = input[i][1:11]
        year = int(input[i][14:18])
        month = int(input[i][19:21])
        day = int(input[i][22:24])
        try:
            myDate = JalaliDate(year=year , month=month , day=day).to_gregorian().isoformat()
            nocrInq = NocrOprInqClass(nationalCode , myDate)
            if (nocrInq.inquiry().status_code == 200):
                print(nationalCode,'SUCCESS')
                with open("D:/convertedTimeSuccess.csv","a") as filesuccess:
                    filesuccess.write(f'{nationalCode,}\n')
            else:
                print(nocrInq.inquiry())
                with open("D:/convertedTimeError.csv","a") as filesuccess:
                    filesuccess.write(f'{nationalCode,}\n')
        except Exception as myEX:
            print(myEX)
            with open("D:/convertedTimeError.csv","a") as fileError:
                fileError.write(f'{nationalCode,}\n')



