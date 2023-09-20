def combine(list1, list2):
    mergedList = []

    list1Length = len(list1)
    list2Length = len(list2)
    minLength = min(list1Length,list2Length )
    
    for i in range(minLength):
        mergedList.append(list1[i])
        mergedList.append(list2[i])
    
    if len(list1) > minLength:
        mergedList.extend(list1[minLength:])
    elif len(list2) > minLength:
        mergedList.extend(list2[minLength:])
    
    return mergedList

print(combine([11,22,33,45], [1,2,3]))