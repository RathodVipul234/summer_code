#input 7
n = int(input("Enter Your Number : "))
for i in range(n):
    for k in range(n-i):
        print(" ",end = "")
    if i % 2 == 0:
        for j in range(i+1):
            print("*", end = " ")
    else:
        for j in range(i+1):
            print(j+1,end = ' ')
    print(" ")