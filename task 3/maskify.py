n = input("Enter Your Phone Number ")
def maskify(n):
    last_4_digit = n[-4:]
    final_str = 6*"#" + last_4_digit
    print(final_str)
if len(n) == 10:
    maskify(n)
else:
    print("Invalid Number")