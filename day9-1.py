import numpy as np
marked = np.zeros((len(input),len(input[0])))
basins = np.zeros((len(input),len(input[0])))

def check_basins():
    for row in range(0,len(marked)):
        for column in range(0,len(marked[0])):
            if marked[row][column] == 1:
                #check_left_for_item
                if column == 0 :
                    input[row][column] == input[row][column+1]
                    
                elif  column != 0 :
                    input[row][column] == input[row][column-1]

                #check_right_for_item
                #check_up_for_item
                #check_down_for_item
                #check_vertical_for_item




def find_low_point_in_adjacent(input):
    # risk_level = 0
    
    for row in range(0,len(input)):
        for column in range(0,len(input[0])):
            if row ==0  :
                if input[row][column] < input[row + 1][column] :
                    if column ==0  :
                        if input[row][column] < input[row][column+1] :
                            marked[row][column] = 1
                            basins[row][column] = 1
                            rrow = row
                            ccolumn = column
                            while input[rrow][column] == input[rrow][column+1] +1 and input[rrow][column+1] != 9 and column != 8  :
                                basins[rrow][ccolumn+1] +1
                                ccolumn = column +1
                    elif  column == len(input[0])-1:
                        if input[row][column] < input[row][column-1] :
                            marked[row][column] = 1
                    else:
                        if input[row][column] < input[row][column+1] and \
                            input[row][column] < input[row][column-1] and \
                            input[row][column] < input[row + 1][column] :
                                marked[row][column] = 1
            elif row == len(input)-1 :
                if input[row][column] < input[row-1][column] :
                    if column ==0  :
                        if input[row][column] < input[row][column+1] :
                            marked[row][column] = 1
                    elif  column == len(input[0])-1:
                        if input[row][column] < input[row][column-1] :
                            marked[row][column] = 1
                    else:
                        if input[row][column] < input[row][column+1] and \
                            input[row][column] < input[row][column-1] and \
                            input[row][column] < input[row - 1][column] :
                                marked[row][column] = 1
            else:
                if input[row][column] < input[row + 1][column] and input[row][column] < input[row - 1][column] :
                    if column ==0 :
                        if input[row][column] < input[row ][column +1]:
                            marked[row][column] = 1
                    elif column == len(input[0])-1:
                        if input[row][column] < input[row ][column -1]:
                            marked[row][column] = 1
                    else:
                        if input[row][column] < input[row][column +1] and\
                             input[row][column] < input[row ][column -1] and\
                                  input[row][column] < input[row+1 ][column] and\
                                       input[row][column] < input[row -1][column ]:
                            marked[row][column] = 1
    for row in range(0,len(input)):
        for column in range(0,len(input[0])):
            if(marked[row][column] == 1):
                # risk_level = risk_level + input[row][column] +1
    print(marked)
    # return risk_level



with open("D:/day9.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]
result = np.zeros((len(input),len(input[0])))

for row in range(0,len(input)):
    for column in range(0,len(input[0])):
        result[row][column] = input[row][column]

print(find_low_point_in_adjacent(result))