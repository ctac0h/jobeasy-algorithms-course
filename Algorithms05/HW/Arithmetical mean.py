def below_arithmetical_mean(arr):
    a_mean = sum(arr)/len(arr)
    print(a_mean)
    return [x for x in arr if x < a_mean]


print(below_arithmetical_mean([1,2,3,4,5,6,7,8,9,10]))
