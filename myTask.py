def myTask():
    with open("D:/ttest.txt") as file:
        input = file.readlines()
    input = [input[x].strip() for x in range(len(input))]
    for i in range(0,len(input)):
        if (input[i][0] != ','):
            nationalCode = input[i][1:11]
            year = int(input[i][14:18])
            month = int(input[i][19:21])
            day = int(input[i][22:24])
        print(f'{nationalCode,}{year}{month}{day}')


 