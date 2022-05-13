def freqquency_finedr(input):
    zero_total = [0] * len(input[0])
    one_total = [0] * len(input[0])
    for column in range(len(input[0])):
        zero_freq = 0
        one_freq = 0
        for row in range(len(input)):
            if(int(input[row][column]) == 0) :
                zero_freq +=1
            else: 
                one_freq +=1
        zero_total[column] = zero_freq
        one_total[column] = one_freq
    return zero_total , one_total

def find_item_nth_bit_frequent(input,nth_bit,frequent_bit):
    items = []
    for row in range(len(input)):
        if(int(input[row][nth_bit]) == frequent_bit):
            items.append(input[row])
    return items


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



with open("D:/input3.txt") as file:
    diag_report = file.readlines()
diag_report = [diag_report[x].strip() for x in range(len(diag_report))]




zero_freq , one_freq = freqquency_finedr(diag_report)
if( one_freq[0] > zero_freq[0] ) :
    items = find_item_nth_bit_frequent(diag_report,0,1)
else:
    items = find_item_nth_bit_frequent(diag_report,0,0)
iteration_count = len(items[0])
for bit_number in range(1,iteration_count):
    zero_freq , one_freq = freqquency_finedr(items)
    if( int(one_freq[bit_number]) >= int(zero_freq[bit_number]) ):
        items = find_item_nth_bit_frequent(items,bit_number,1)
    else:
        items = find_item_nth_bit_frequent(items,bit_number,0)
oxygen_generator_rating = items[0]


zero_freq , one_freq = freqquency_finedr(diag_report)
if( one_freq[0] > zero_freq[0] ) :
    items = find_item_nth_bit_frequent(diag_report,0,0)
else:
    items = find_item_nth_bit_frequent(diag_report,0,1)
iteration_count = len(items[0])
for bit_number in range(1,iteration_count):
    if (len(items) == 1) :
        break
    zero_freq , one_freq = freqquency_finedr(items)
    if( int(one_freq[bit_number]) >= int(zero_freq[bit_number])):
        items = find_item_nth_bit_frequent(items,bit_number,0)
    else:
        items = find_item_nth_bit_frequent(items,bit_number,1)
co2_generator_rating = items[0]
print(oxygen_generator_rating,co2_generator_rating)