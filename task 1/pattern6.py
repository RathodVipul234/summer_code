n = int(input("Enter Your Number :"))
for i in range(n):
    for j in range(i+1):
        print(" ",end = '')
    for j in range(n-i  ):
        print(i+j+1,end = " ")
    print("")
for p in range(n):
    for q in range(n-p):
        print(" ",end = '')
    for q in range(p+1):
        print(n-p+q,end = ' ')
    print("")
