#input 5
n = int(input("Enter Your Number :"))
for i in range(n):
    for j in range(n-i):
        total = i+j+1
        print(total,end = '')
    for j in range(n-i-1):
        print(total-j-1,end= '')
    print("")

