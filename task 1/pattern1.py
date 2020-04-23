n = int(input("Enter Your Number :"))
for i in range(1,n+1):
    A = 65
    Z = 90
    for j in range(n-((n+i+1)//2)+1):
        if i%2 != 0:
            print(f"{chr(A)} ",end =' ')
            A+=1
        else:
            print(f" {chr(Z)}",end = ' ')
            Z -= 1
    print('')
for i in range(1,n):
    A = 65
    z = 122
    for j in range(i//2+1):
        if i%2 == 0:
            print(f"{chr(A)} ",end =' ')
            A+=1
        else:
            print(f" {chr(z)}",end = ' ')
            z -= 1
    print("")