monthly = [1,2,3,4,5,6,7,8,9,10,11,12]
quarterly = []

for i in range(0, len(monthly)-1,3):
    firstnum = monthly[i]
    secondnum = monthly[i+1]
    thirdnum = monthly[i+2]
    print(firstnum, "+", secondnum, "+", thirdnum)
    sumnum = firstnum + secondnum + thirdnum
    quarterly.append(sumnum)

print(quarterly)
