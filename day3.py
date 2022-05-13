def binary2decimal(input):
    return sum(val*(2**idx) for idx, val in enumerate(reversed(input)))

with open("D:/input3.txt") as file:
    diag_report = file.readlines()
diag_report = [diag_report[x].strip() for x in range(len(diag_report))]

# diag_report = ['00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010']




gamma_rate = [0] * len(diag_report[0])
epsilon_rate = [0] * len(diag_report[0])

for bit in range(0,len(diag_report[0])):
    zero_freq = 0
    one_freq = 0
    for j in range(0,len(diag_report)):
        if(int(diag_report[j][bit]) ==  0):
            zero_freq +=1
        else: one_freq +=1
    if(one_freq>zero_freq):
        gamma_rate[bit] = 1
        epsilon_rate[bit] = 0
    else: 
        gamma_rate[bit] = 0
        epsilon_rate[bit] = 1

print(gamma_rate , binary2decimal(gamma_rate))
print(epsilon_rate , binary2decimal(epsilon_rate))
print(binary2decimal(gamma_rate) *  binary2decimal(epsilon_rate))