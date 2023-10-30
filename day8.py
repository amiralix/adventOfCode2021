import re
import numpy as np

def create_number_from_list(list):
    res = int(list[0]) * 1000 + int(list[1]) * 100 + int(list[2]) * 10 + int(list[3])
    return res

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

with open("D:/day8_2.txt") as file:
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
        if len(input[row][column]) == 2 : # this is ONE
            one += 1
            result[row][column] = 1
        elif len(input[row][column]) == 4 : # this is FOUR
            four += 1
            result[row][column] = 4
        elif len(input[row][column]) == 3: # this is SEVEN
            seven += 1
            result[row][column] = 7
        elif len(input[row][column]) == 7: # this is EIGHT
            result[row][column] = 8
        elif len(input[row][column]) == 5 : # this is TWO or THREE or FIVE
            # handle TWO

            # match [cdfbe]{5}
            if (re.search('[bcefd]',input[row][column])): #or re.search('[c][d][g][b][a]',input[row][column])\
                # or re.search('',input[row][column])) :
                two += 1
                result[row][column] = 2
            # handle THREE
            elif (re.search('[f][b][c][a][d]',input[row][column]) or re.search('[f][c][a][d][b]',input[row][column]) 
                or re.search('[c][d][b][a][f]',input[row][column]) or re.search('[c][e][f][d][b]',input[row][column]) 
                    or re.search('[c][e][d][b][a]',input[row][column]) or re.search('[b][f][g][e][a]',input[row][column])
                        or re.search('[c][f][g][a][b]',input[row][column])) :
                three += 1
                result[row][column] = 3
            # handle FIVE
            elif ( re.search('[cbedf]',input[row][column]) or re.search('[cbgef]',input[row][column])
                or re.search('[bagce]',input[row][column]) ):
                five += 1
                result[row][column] = 5
        elif len(input[row][column]) == 6: # this is ZERO or SIX or NINE
            # handle ZERO ---new
            if ( ( re.search("[cagedb]{6}",input[row][column]) != None and len((re.search("[cagedb]{6}",input[row][column])).group()) == 6 ) ):
                zero +=1
                result[row][column] = 0
            # handle SIX ---new
            if (  ( re.search("[cdfgeb]{6}",input[row][column]) != None and\
                 re.search("[cdfgea]{6}",input[row][column]) != None and\
                      re.search("[cbfgea]{6}",input[row][column]) != None ) 
                and  ( len((re.search("[cdfgeb]{6}",input[row][column])).group()) == 6  or\
                     len((re.search("[cdfgea]{6}",input[row][column])).group() == 6 ) ) \
                     or len((re.search("[cbfgea]{6}",input[row][column])).group()) == 6 ) :
                    six +=1
                    result[row][column] = 6
            # handle NINE  ---new 
            if (  re.search("[cefabd]{6}",input[row][column]) != None and\
                 ( len((re.search("[cefabd]{6}",input[row][column])).group()) == 6  or len((re.search("[cefgbd]{6}",input[row][column])).group() == 6 ) ) ) :
                nine +=1
                result[row][column] = 9
print(result)

sum = 0
for rows in range(0,len(result)):
    sum = sum + create_number_from_list(result[rows])
print(sum)
        
