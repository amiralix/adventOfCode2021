# import numpy as np
# timers = [4,1,1,4,1,1,1,1,1,1,1,1,3,4,1,1,1,3,1,3,1,1,1,1,1,1,1,1,1,3,1,3,1,1,1,5,1,2,1,1,5,3,4,2,1,1,4,1,1,5,1,1,5,5,1,1,5,2,1,4,1,2,1,4,5,4,1,1,1,1,3,1,1,1,4,3,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,2,1,1,1,1,1,1,1,2,4,4,1,1,3,1,3,2,4,3,1,1,1,1,1,2,1,1,1,1,2,5,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,4,1,5,1,3,1,1,1,1,1,5,1,1,1,3,1,2,1,2,1,3,4,5,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1,3,1,1,3,1,1,4,1,1,1,1,1,2,1,1,1,1,3,2,1,1,1,4,2,1,1,1,4,1,1,2,3,1,4,1,5,1,1,1,2,1,5,3,3,3,1,5,3,1,1,1,1,1,1,1,1,4,5,3,1,1,5,1,1,1,4,1,1,5,1,2,3,4,2,1,5,2,1,2,5,1,1,1,1,4,1,2,1,1,1,2,5,1,1,5,1,1,1,3,2,4,1,3,1,1,2,1,5,1,3,4,4,2,2,1,1,1,1,5,1,5,2]
# timers = np.array(timers)
# print("Initial state  " , timers)
# for days in range(1,257):
#     zero_indices = list(np.where( timers == 0 ))[0]
#     non_zero_indices = list(np.nonzero(timers))[0]
#     timers[non_zero_indices] = timers[non_zero_indices] -1 
#     timers[zero_indices] = 6
#     timers = np.insert(timers,len(timers), [8] * len(zero_indices))
#     print("After ",days," day: ",timers)            
# print(len(timers))



with open("D:/day6.txt") as file:
    input = file.readlines()

input = [x.strip() for x in input]
input = input[0].split(",")
my_dict = []
DAYS = 19

for days in range(0,DAYS):
    for i in range(0,len(input)):
        input[i] = int(input[i]) 
        input[i] -= 1
        if input[i] == -1:
            input[i] = 6
            my_dict.append(9)
    if len(my_dict) != 0:
        for j in range(0,len(my_dict)):
            my_dict[j] -= 1
            if( my_dict[j] == -1):
                my_dict.append(9)
                input.append(6)
                del my_dict[j]
print("After ",days," day: ",input,my_dict)            
