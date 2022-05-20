import re
import numpy as np

ZERO = 6
ONE = 2 
TWO = 5
THREE = 5
FOUR = 4
FIVE = 5
SIX = 6
SEVEN = 3 
EIGHT = 7
NINE = 6

with open("D:/day8.txt") as file:
    input = file.readlines()

input = [(((x.split("|"))[1]).strip().split(" ")) for x in input]

zero = 0
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
seven = 0
eight = 0
nine = 0

result = np.zeros((len(input),4))

for row in range(0,len(input)):
    for column in range(0,4):
        if len(input[row][column]) == ONE:
            one += 1
            result[row][column] = 1
        if len(input[row][column]) == FOUR:
            four += 1
            result[row][column] = 4
        if len(input[row][column]) == SEVEN:
            seven += 1
            result[row][column] = 7
        if len(input[row][column]) == EIGHT:
            result[row][column] = 8
        if len(input[row][column]) == TWO:
            # handle TWO
            if (re.search('[g][c][d][f][a]',input[row][column]) or re.search('[c][d][g][b][a]',input[row][column])) :
                two += 1
                result[row][column] = 2
            # handle THREE
            if (re.search('[f][b][c][a][d]',input[row][column]) or re.search('[f][c][a][d][b]',input[row][column]) 
                or re.search('[c][d][b][a][f]',input[row][column]) or re.search('[c][e][f][d][b]',input[row][column]) 
                    or re.search('[c][e][d][b][a]',input[row][column]) or re.search('[b][f][g][e][a]',input[row][column])
                        or re.search('[c][f][g][a][b]',input[row][column])) :
                three += 1
                result[row][column] = 3
            # handle FIVE
            if (re.search('[cdb][dcba][fbg][bec][ebf]',input[row][column])) :
                five += 1
                result[row][column] = 5
        if len(input[row][column]) == SIX:
            # handle ZERO
            if (re.search('[c][a][g][e][d][b]',input[row][column])) :
                zero +=1
                # result[row][column] = 0
            # handle SIX
            if (re.search('[cgb][dac][fdg][gfa][ef][bce]',input[row][column])) :
                six +=1
                result[row][column] = 6
            # handle NINE       
            if (re.search('[cfe][ecdf][fgca][abe][bgdc][db]',input[row][column])) :
                nine +=1
                result[row][column] = 9
print(result)
        
