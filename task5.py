def triangle(n):
    if n > 0:
        for i in range(n):
            for j in range(i+1):
                print("#", end="")
            print()
    if n < 0:
        for i in range(n):
            for j in range(i, n):
                print("#", end="")
    print()        
            
triangle(-5)