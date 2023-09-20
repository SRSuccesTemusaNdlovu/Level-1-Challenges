

def hasThree(num1, num2):

    total = num2 + num1

    totalList = list(map(int, str(total)))

    for x in totalList:
        if x ==3 and (num1 == 3 or num2 == 3):
            boolVal = True

        else:
            boolVal = False
        
    return boolVal
    
        

    
print(hasThree(33,3))
    