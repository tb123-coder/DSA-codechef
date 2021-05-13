def divisbity(Num) :
    if(Num%5==0)&(Num%11==0):
        print("BOTH")
    elif(Num%5==0)|(Num%11==0):
        print("ONE")
    else:
        print("NONE")


try:
    N=int(input())
    divisbity(N)

except:
    print("N is not a  intezer")
    exit()
