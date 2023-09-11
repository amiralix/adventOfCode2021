import re
def checkPostCodeValidation(postalCode) :
        returnValue = False
        if len(postalCode) != 10 :
            returnValue = False
        elif re.match('^[0-9]+$' , postalCode) == False:
            returnValue
        elif postalCode[4] == '5':
            returnValue
        elif '0' in postalCode[0:4] or '2' in postalCode[0:4] :
            returnValue
        elif postalCode[5] == '0':
            returnValue
        elif '0' in postalCode[6:9]:
            returnValue
        else:
            returnValue = True
        return returnValue 
            
postCode = input("enter Postal Code\n")
print(checkPostCodeValidation(postCode))



