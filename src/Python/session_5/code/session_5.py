from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def move(self):

        pass


class Bird(Animal):

    # pass

    def move(self):

        print("Bird")


class Cat(Animal):

    def move(self):

        print("Cat")


b = Bird()
b.move()

print("#" * 50)


class A:

    def do_this(self):

        print("I'm in A")


class B(A):

    pass


class C:

    def do_this(self):

        print("I'm in C")


class D(B, C):

    pass


x = D()
x.do_this()


print("#" * 50)

import os

base = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\session_5\code"
print(type(base))

file = os.listdir(base)
print(file)

# os.remove(base + r"\test.py")

directory = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\session_5\code\test_dir"

if not os.path.exists(directory):

    os.makedirs(directory)
    print(f"{directory} is created successfully.")

else:

    print("Directory already exists:", directory)

print("#" * 50)

import os

path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\session_5\code\tmp_directory"

if not os.path.exists(path):

    os.makedirs(path)

for i in range(20):

    inner_path = os.path.join(path, "dir_" + str(i))

    if not os.path.exists(inner_path):

        os.makedirs(inner_path)

print("#" * 50)

# import os

# def create_folders(path):

#     if not os.path.exists(path):

#         os.makedirs(path)

#     for i in range(20):

#         inner_path = os.path.join(path, "dir_" + str(i))

#         if not os.path.exists(inner_path):

#             os.makedirs(inner_path)

from create_folder import create_folders

# create_folders(path=)

print("#" * 50)

# with open(r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\session_5\code\session_5.py", "a+") as file:  # "w+" "r+"
#     # content = file.read()

#     file.write(" New line added\n")  # Write new content

#     file.seek(0)  # Move the file pointer to the beginning

#     updated_content = file.read()  # Read the updated content

#     print(updated_content)

print("#" * 50)

import random

from prettytable import PrettyTable

u = "test"
p = "1111"

while True:

    x = input("Enter your username: ")
    if x == u:

        y = input("Enter your password: ")
        if y == p:

            s = random.randrange(1000, 1000000)
            print("Verification code is: ", s)

            while True:

                l = int(input("Enter your verification code: "))
                if l == s:

                    print("Access Granted!")
                    break

                else:

                    print("Invalid verification code. please try again.")

            break

        else:

            print("Incorrect password. please try again.")

    else:

        print("Incorrect username. please try again.")
        continue
