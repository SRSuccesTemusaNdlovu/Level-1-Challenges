
def isSixtyFive(num1, num2):

    total = num2 + num1

    totalList = list(map(int, str(total)))

    for x in totalList:
        if x == 65 or (num1 == 65 or num2 == 65):
            boolVal = True

        else:
            boolVal = False
        
    return boolVal
    
        

    
print(isSixtyFive(10,10))