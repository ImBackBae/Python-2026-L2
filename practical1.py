import math
def circle():
    r = int(input("Enter circle radius: "))
    print(f"Circle area = {r**2*3.14}")

def c_to_f():
    c = int(input("Enter the temperature in Celsius? "))
    print(f"{c} (C) = {c*9/5 + 32} (F)")

def check_prime():
    num = int(input("Enter a number? "))
    is_prime = True
    for i in range(2, num):
        if num%i == 0:
            is_prime = False
            break
    if is_prime == True:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

def check_perfect():
    factorial = []
    n = int(input("Enter a number? "))
    for i in range(1, n):
        if n%i == 0:
            factorial.append(i)
    if sum(factorial) == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")

def check_color():
    colors = ["Red", "Blue", "Yellow", "Brown", "Purple"]
    color = input("What is your favorite color? ")
    not_found = True
    for i in range(len(colors)):
        if colors[i] == color:
            print(f"Your colod is at index {i} in my list")
            not_found = False
    if not_found: print("Sorry, I could not find your color")

def print_sequence():
    print(f"Range 1: {list(range(7))}")
    print(f"Range 2: {list(range(1,11,3))}")
    print(f"Range 3: {list(range(5,0,-1))}")
    print(f"Range 4: {list(range(6,-3,-2))}")


def remove_dollar_sign(s):
    i = 0
    while i < len(s):
        if s[i] == "$":
            s = s[:i] + s[i+1:]
        else: 
            i += 1
    return s

def extract_even(l):
    result = []
    for i in l:
        if i%2 == 0:
            result.append(i)
    return result

def fac(num):
    factorial = []
    for i in range(1, num+1):
        if num%i == 0:
            factorial.append(i)
    return factorial

def divisors(num):
    div = []
    for i in range(-num, num+1):
        if i == 0:
            pass
        elif num%i == 0:
            div.append(i)
        
    return div

def compute_two_points(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

def pattern(m, n):
    for i in range(m):
        for j in range(n):
            if (i == 0 or j == 0):
                print("* ", end="")
            elif j == n-1 or i == m-1:
                print("* ", end="")
            else:
                print(" "*2, end="")
        print()
