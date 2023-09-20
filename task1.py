

def multiples(num):

    total = 0

    for i in range(1, num):
        if i % 3 == 0 or i % 5 ==0:
            total += i
    print(total)

multiples(10)
multiples(11)


