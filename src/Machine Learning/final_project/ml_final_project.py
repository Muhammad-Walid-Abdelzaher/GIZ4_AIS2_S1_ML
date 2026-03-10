# DEPI AI & ML Round 4
# Machine Learning - Final Project
# --------------------------------
# Made With <3 By Muhammad Walid
# March 10, 2026
# ------------------------------


# Task 1
# Step 1
# ------
def bank_account_management(balance: float) -> None:
    """
    Interactive Bank Account Management System.

    Allows the user to:
    - Deposit money to their account
    - Withdraw money from their account
    - Check their current balance
    - Exit the program

    :param balance: The Current Balance in the User's Account
    :type balance: int
    :return: No return value
    :rtype: None
    """

    while True:

        user_choice = int(
            input(
                f"What do you want to do?\n1- Deposit\n2- Withdrawal\n3- Check Current Balance\n4- Cancel\n"
            )
        )

        if user_choice == 1:  # If user wanted to Deposit

            deposit = int(input("How much do you want to deposit? "))

            if deposit > 0:

                balance += deposit
                print(
                    f"{'#' * 30}\nDeposited {deposit}. New balance: {balance}\n{'#' * 30}"
                )

            else:

                print(f"{'#' * 40}\nCan not deposit money less than 0.\n{'#' * 40}")

        elif user_choice == 2:  # If user wanted to Withdraw

            withdraw = int(input("How much do you want to withdraw? "))

            if withdraw > 0:

                balance -= withdraw
                print(
                    f"{'#' * 30}\nWithdrew {withdraw}. New balance: {balance}\n{'#' * 30}"
                )

            else:

                print(f"{'#' * 40}\nCan not withdraw money less than 0.\n{'#' * 40}")

        elif user_choice == 3:  # If user wanted to Check his/her Current Balance

            print(f"{'#' * 30}\nCurrent balance: {balance}\n{'#' * 30}")

        elif user_choice == 4:  # If user wanted to Cancel Current Transaction

            print("Exiting...")
            break

        else:

            print("Invalid Choice.")


bank_account_management(100)

print("=" * 50)


# Task 1
# Step 2
# ------
class BankAccount:
    """
    A class representing a bank account with basic banking operations

    Attributes:
        balance (float): The current balance of the bank account

    Methods:
        deposit(money): Adds money to the account balance
        withdraw(money): Subtracts money from the account balance
        check_balance(): Returns the current balance
    """

    def __init__(self, bal: float):

        self.balance = bal

    def deposit(self, money: float):

        try:

            if money <= 0:

                raise Exception(
                    f"{'#' * 45}\nCan not deposit money less than or equal 0.\n{'#' * 45}"
                )

        except Exception as negative_deposit:

            return negative_deposit

        else:

            self.balance += money
            return f"Deposited {money}. New balance: {self.balance}"

    def withdraw(self, money: float):

        try:

            if money <= 0:

                raise Exception(
                    f"{'#' * 45}\nCan not withdraw money less than or equal 0.\n{'#' * 45}"
                )

        except Exception as negative_withdraw:

            return negative_withdraw

        else:

            self.balance -= money
            return f"Withdrew {money}. New balance: {self.balance}"

    def check_balance(self):

        return f"Current balance: {self.balance}"


user_account = BankAccount(100)

print(user_account.deposit(50))
print(user_account.withdraw(30))
print(user_account.check_balance())

print("#" * 50)


# Task 2
# ------
class Calculator:
    """
    A class representing a calculator with basic arithmetic operations

    Attributes:
        num_1 (float): First Number in the calc
        num_2 (float): Second Number in the calc

    Methods:
        add(): Prints the sum of num_1 and num_2
        subtract(): Prints the difference (num_1 - num_2)
        multiply(): Prints the product of num_1 and  num_2
        divide(): Prints the quotient (num_1 / num_2)
        main(): Interactive menu to choose and execute operations
    """

    def __init__(self, first_number: float, second_number: float):

        self.num_1 = float(first_number)
        self.num_2 = float(second_number)

    def add(self):

        print(f"{self.num_1} + {self.num_2} = {self.num_1 + self.num_2}")

    def subtract(self):

        print(f"{self.num_1} - {self.num_2} = {self.num_1 - self.num_2}")

    def multiply(self):

        print(f"{self.num_1} * {self.num_2} = {self.num_1 * self.num_2}")

    def divide(self):

        print(f"{self.num_1} / {self.num_2} = {self.num_1 / self.num_2}")

    def main(self):

        print("Welcome to the Calculator!", "Choose an operation:", sep="\n")
        print("1: Add", "2: Subtract", "3: Multiply", "4: Divide", sep="\n")
        choice = input()

        if choice == "1":

            self.add()

        elif choice == "2":

            self.subtract()

        elif choice == "3":

            self.multiply()

        elif choice == "4":

            self.divide()

        else:

            print("Invalid Choice.")


calc = Calculator(22, 33)
calc.main()

print("#" * 50)


# Task 3
# ------
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, animal_name):

        self.name = animal_name

    @abstractmethod
    def make_sound(self):

        pass

    def describe(self):  # Concrete Method

        print(f"This is {self.name}, a {self.__class__.__name__}.")


class Dog(Animal):
    """
    A class representing a Dog, a specific type of Animal

    Attributes:
        game (str): The game that the dogs like, default is "catching balls"

    Methods:
        make_sound(): Implements the dog's barking sound
        describe(): Provides information about dog's favourite game
    """

    def __init__(self, animal_name: str):

        super().__init__(animal_name)
        self.game = "catching balls"

    def make_sound(self):

        print(f"{self.name} says: Woof!")

    def describe(self):

        super().describe()
        print(f"{self.name} likes {self.game}")


class Cat(Animal):
    """
    A class representing a Cat, a specific type of Animal

    Attributes:
        food (str): The food that the cats love, default is "milk"

    Methods:
        make_sound(): Implements the cat's meowing sound
        describe(): Provides information about cat's favourite food
    """

    def __init__(self, animal_name: str):

        super().__init__(animal_name)
        self.food = "milk"

    def make_sound(self):

        print(f"{self.name} says: Meow!")

    def describe(self):

        super().describe()
        print(f"{self.name} loves {self.food}")


class Cow(Animal):
    """
    A class representing a Cow, a specific type of Animal

    Attributes:
        product (str): The product obtained from cows, default is "cheese"

    Methods:
        make_sound(): Implements the cow's mooing sound
        describe(): Provides information about cow products
    """

    def __init__(self):

        self.product = "cheese"

    def make_sound(self):

        print(f"{self.__class__.__name__} says: Moo!")

    def describe(self):

        print(f"{self.__class__.__name__} gives us {self.product}")


animals = [Dog("Fawzy"), Cat("Fawzia"), Cow()]

for animal in animals:

    animal.describe()
    animal.make_sound()
    print("=" * 30)

print("#" * 50)


# Task 4
# ------
class TextFileReader:

    def __init__(self, file_path: str):

        self.path = file_path
        self.content = ""

    def read_file(self):

        with open(self.path, "r") as file:

            self.content = file.read()

    def count_lines(self):

        if not self.content:

            self.read_file()

        return len(self.content.split("\n"))

    def count_words(self):

        return len(self.content.split())

    def count_characters(self):

        return len(self.content)

    def display_content(self):

        return self.content


reader = TextFileReader(r"C:\Users\Muhammad Walid\Python\SEARCH.txt")
print(f"No. of lines in file: {reader.count_lines()}")
print(f"No. of words in file: {reader.count_words()}")
print(f"No. of chars in file: {reader.count_characters()}")
print("=" * 30)
print(f"File Content: {reader.display_content()}")

print("#" * 50)


# Task 6
# ------
def read_txt_file(file_path):

    try:

        with open(file_path, "r") as file:

            content = file.read()
            return content

    except FileNotFoundError:

        return f"Error: File {file_path} Not Found."

    except IOError:

        return f"Error happened during the interaction between the program and the OS (Operation System)"

    except:

        return f"Error Found."


class UserExtractor:

    def __init__(self, file_path):

        self.fpath = file_path
        self.usernames = {}

    def extract_usernames(self):

        file_content = read_txt_file(self.fpath)
        lines = file_content.split("\n")
        for line_num, line in enumerate(lines, 1):

            if ":" not in line:

                print(f"Warning: Line {line_num} has invalid format: '{line}'")
                continue

            parts = line.split(":")
            username, password = parts[0].strip(), parts[1].strip()
            self.usernames[username] = password

        return self.usernames


user_extract = UserExtractor(
    r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Python\final_project\usernames.txt"
)
print(user_extract.extract_usernames())
