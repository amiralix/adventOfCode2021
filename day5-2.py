import numpy as np
MAX_ITEM = 1000


def find_overlaps(input):
    sum = 0
    for row in range(0,MAX_ITEM):
        for column in range(0,MAX_ITEM):
            if input[row][column] >= 2 :
                sum +=1
    return sum

def check_vertical(x1,y1,x2,y2):
    if ( abs(x2-x1) == abs(y2-y1)): # secondary diagonal
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
    elif (check_vertical(x1,y1,x2,y2) == 0 ): # Main diagonal lines
        for w in range(0,x2-x1+1):
            table[x1+w][y1+w] = table[x1+w][y1+w] +1
    elif (check_vertical(x1,y1,x2,y2) == 1 ): # secondary  lines
        if( x1 > x2 and y1 > y2 ):
            for z in range(0,max(abs(x2-x1),abs(y2-y1)) +1):
                table[x1-z][y1-z] = table[x1-z][y1-z] +1
        elif( x1 > x2 and y2 > y1 ):
            for t in range(0,max(abs(x2-x1),abs(y2-y1)) +1):
                table[x1-t][y1+t] = table[x1-t][y1+t] +1
        elif( x1 < x2 and y1 > y2 ):
            for r in range(0,max(abs(x2-x1),abs(y2-y1)) +1):
                table[x1+r][y1-r] = table[x1+r][y1-r] +1
        elif( x1 < x2 and y2 > y1 ):
            for b in range(0,max(abs(x2-x1),abs(y2-y1)) +1):
                table[x1+b][y1+b] = table[x1+b][y1+b] +1


print(np.transpose(table))
print(find_overlaps(table))

