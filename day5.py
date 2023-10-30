import numpy as np
MAX_ITEM = 1000


def find_overlaps(input):
    sum = 0
    for row in range(0 , MAX_ITEM):
        for column in range(0,MAX_ITEM):
            if input[row][column] >= 2 :
                sum +=1
    return sum

def check_vertical(x1,y1,x2,y2):
    if ( abs(x2-x1 ) == abs(y2-y1)): # secondary diagonal
        return 1
    if ( x1 == y1 and x2 == y2 ): # main diagonal
        return 0
    return -1

with open("D:/day5.txt") as file:
    input = file.readlines()

input = [x.strip() for x in input]
table = np.zeros((MAX_ITEM,MAX_ITEM))

for counter in range(len(input)):
    x1 = int((input[counter].split(","))[0])
    y1 = int((((input[counter].split(","))[1]).split("->"))[0])
    x2 = int((((input[counter].split(","))[1]).split("->"))[1])
    y2 = int((input[counter].split(","))[2])
    if( x1 == x2 ): # horizontal 
        if(y2>y1) :
            for i in range(y1,y2+1):
                table[x1][i] = table[x1][i] +  1
        else:
            for j in range(y2,y1+1):
                table[x1][j] = table[x1][j] +  1
    elif( y1 == y2 ): # vertical
        if(x2>x1) :
            for f in range(x1,x2+1):
                table[f][y1] = table[f][y1] +  1
        else:
            for k in range(x2,x1+1):
                table[k][y1] = table[k][y1] +  1


print(np.transpose(table))
print(find_overlaps(table))

