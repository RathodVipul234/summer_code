#input 7
n = int(input("Enter Your Number : "))
for i in range(n):
    for k in range(n-i):
        print(" ",end = "")
    if i < 3:
        for p in range(i+1):
            print("*",end = " ")
    else:
        print("*",end = "")
        for j in range(i-1):
            print("",end = " ")
        print("*",end = "")
        for m in range(i-1):
            print("",end = " ")
        print("*",end = '')
    print(" ")