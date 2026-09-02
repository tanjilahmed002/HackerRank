string="Hello, World!"
print(string)


n = int(input())

if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")


a=int(input(""))
b=int(input(""))
print(a+b)
print(a-b)
print(a*b)


# Task
# The provided code stub reads two integers,  and , from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

# No rounding or formatting is necessary.

a=int(input(""))
b=int(input(""))
print(a//b)
print(float(a/b))