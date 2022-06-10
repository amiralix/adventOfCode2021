class stack:
    def __init__(self) -> None:
        self.list = []
    def push(self,item):
        self.list.append(item)
    def isEmpty(self):
        if self.list == []:
            return True
        else: return False
    def pop(self):
     if self.isEmpty():
         return "The stack is empty."
     else:
         return self.list.pop()
    def print_stack(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
             for i in range(0,len(self.list)):
                 print(self.list[i])
    def purge_stack(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.list
            


def find_penalty(list):
    penalty = 0
    for counter in range(0,len(list)):
        if list[counter] == ")":
            penalty  = penalty  + 3
        elif list[counter] == "]":
            penalty  = penalty  + 57
        elif list[counter] == "}":
            penalty  = penalty  + 1197
        elif list[counter] == ">":
            penalty  = penalty  + 25137
    return penalty

def complete_list(input_invalids,input_list):
    scores = [0] * len(input_list)
    for counter in range(0,len(input_invalids)):
        if input_invalids[counter] == 0:
            mylist = input_list[counter]
            for my_list_counter in range(len(mylist)-1,-1,-1):
                if(mylist[my_list_counter] == "("):
                    scores[counter] = scores[counter] * 5 + 1
                elif (mylist[my_list_counter] == "["):
                    scores[counter] = scores[counter] * 5 + 2
                elif (mylist[my_list_counter] == "{"):
                    scores[counter] = scores[counter] * 5 + 3
                elif (mylist[my_list_counter] == "<"):
                    scores[counter] = scores[counter] * 5 + 4
    return scores


with open("D:/day10.txt") as file:
    input = file.readlines()
input = [x.strip() for x in input]

opens =  ["<" , "[" , "(" , "{"]
closes = [">" , "]" , ")" , "}"]
invalids = [0] * len(input)
invalid_chars = [0] * len(input)

for input_row in range(0 , len(input)):
    myStack = stack()
    for input_column in range (0,len(input[input_row])):
        if input[input_row][input_column] in opens:
            myStack.push(input[input_row][input_column])
        else:
            if closes.index(input[input_row][input_column]) != opens.index(myStack.pop()):
                invalids[input_row] = input[input_row][input_column]
    invalid_chars[input_row] = myStack.purge_stack()

# print(find_penalty(invalids))
# print(invalids)
# print(invalid_chars)
scores = complete_list(invalids , invalid_chars)
scores.sort()