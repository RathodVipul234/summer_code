#input 7
n = int(input("Enter Your Number : "))

for i in range(n):
    for j in range(i+1):
        print(n-i+j,end = " ")
    print(" ")