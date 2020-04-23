#input 5
n = int(input("Enter Your Number :"))
for i in range(n):
    for j in range(n-i):
        print(i+j+1,end = '')
    for j in range(n-i-1):
        print(5-j-1,end= '')
    print("")

