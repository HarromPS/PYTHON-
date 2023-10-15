
for i in range(2, 101):
    flag = 0
    for j in range(2, i):
        if(i % j == 0):

            #  flag is set to 1 when the multiples of j is encountered & i%j==0 also when j
            #  encounters itself i.e same no then
            flag = 1
            break
    if(flag == 0):
        print(i, end=" ")
