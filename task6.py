def longest(list):
    
    list1 =[]
    dict1 ={}

    for str in list:
        list1.append(len(list))
        dict1[str]=len(str)
    

    for key, value in dict1.items():
        if(value==max(list1)):
            print(key )

longest(["once", "upon", "a", "time"])
    
