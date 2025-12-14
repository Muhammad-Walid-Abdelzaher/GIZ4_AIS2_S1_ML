def user_info(x, y):
    """
    param_1: take first number from user
    
    type:param_1: int
    
    param_2: take second number from user
    
    type_param_2: int
    
    return: sum two numbers
    
    type_return: int
    """
    return f"num_1 is {x}, num_2 is {y} = {x + y}"

print(user_info(2, 3))

print("#" * 50)  # Separator

def calc(num_1, num_2):

    print(f"{num_1} + {num_2} = {num_1 + num_2}")

    print(f"{num_1} - {num_2} = {num_1 - num_2}")

    print(f"{num_1} * {num_2} = {num_1 * num_2}")

    print(f"{num_1} / {num_2} = {num_1 / num_2}")

calc(10, 5)

print("#" * 50)  # Separator

# Positional Argument Function
def get_info(name, age):

    return f"My name is {name} and my age is {age}"

print(get_info(20, "Muhammad"))

print("#" * 50)  # Separator

# Keyword Argument Function
def get_info(name, age):

    return f"My name is {name} and my age is {age}"

print(get_info(age=20, name="Muhammad"))

print("#" * 50)  # Separator

# Default Argument Function
def get_info(name, age=21):

    return f"My name is {name} and my age is {age}"

print(get_info("Muhammad"))

print("#" * 50)  # Separator

# Varadic (args) Argument Function
def get_info(*name):

    print(f"My name is {name}")
    print(type(name))

get_info("Hello", "Muhammad", "Python", "amit", 2, 2.5, True)
get_info(["Hello", "Muhammad", "Python", "amit", 2, 2.5, True])

print("#" * 50)  # Separator

# Kwargs Argument Function
def get_info(**name):

    print(f"My name is {name}")
    print(type(name))

get_info(key1 = 10.5, key2 = 2, key3 = "Machine Learning", key4 = "Python")

print("#" * 50)  # Separator

# Lambda Function (Small Anonymous Function)
func_1 = lambda x : x + 10

print(type(lambda x : x + 10))
print(type(func_1))
print(func_1(10))  # 20

print("#" * 50)  # Separator

def factorial(num):

    if num == 0:

        return 1
    
    if num == 1:

        return 1
    
    return num * factorial(num - 1)

print(factorial(5))

print("#" * 50)  # Separator

def isPrime(num):

    for i in range(2, num):

        if num % i == 0:

            return False
    
    return True

print(isPrime(9))
print(isPrime(3))
print(isPrime(2))
print(isPrime(20))

print("#" * 50)  # Separator

def dividors(num1, num2):
    """
    :param num1: first number
    :type param num1: int
    
    :param num2: second number
    :type param num2: int

    :return: common dividor between the two numbers
    :type return: int
    """
    mn = min(num1, num2)
    common_dividors = []
    for i in range(1, mn + 1):

        if num1 % i == 0 and num2 % i == 0:

            common_dividors.append(i)

    return common_dividors

print(dividors(3, 6))

print("#" * 50)  # Separator

# Task 3 ( NOT SOLVED )
eveen = []
def even_func(num):

    for i in range(num):

        if i % 2 == 0:

            print(eveen.append(num))

    return eveen

# print(even_func())

print("#" * 50)  # Separator

# Task 4 ( NOT SOLVED )

str1 = input("Enter The First String: ")
str2 = input("Enter The Second String: ")

longest_str = ""
for i in range(len(str1)):

    # print(i)
    for j in range(i, len(str1)):

        # print(j)
        sub_str = str1[i : j + 1]
        print(sub_str)
        if sub_str in str2:

            if len(sub_str) > len(longest_str):

                longest_str = sub_str

print(longest_str)