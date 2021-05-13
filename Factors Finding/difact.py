def factors(number):
    lst=[]
    lst.append(1)
    count=2
    for i in range(2,(int(number/2)+1)):
        if(number%i==0):
            lst.append(i)
            count+=1
    lst.append(number)
    print(count)
    [print(i,end=" ") for i in lst]
N=int(input())
factors(N)

