# DEPI AI & ML Round 4
# Python - Assignment 4
# ---------------------
# Made With <3 By Muhammad Walid
# Dec 19, 2025
# ------------------------------


# Task 1
# ------
class Factorial:
    """
    Factorial class handles the operation of calculating the factorial of a number
    """

    def __init__(self):
        """Intialize the Factorial calculator"""
        pass

    def fact(self, n):
        """
        calculates the factorial of a given number using recursion

        Args:
            n (int): A non-negative integer to calculate the factorial of

        Returns:
            int: The factorial of n (n!)
        """

        if n == 0 or n == 1:

            return 1

        else:

            return n * self.fact(n - 1)


fact_num = Factorial()
print(fact_num.fact(5))

print("#" * 50)


# Task 2
# ------
class Prime:
    """
    A class for checking if a number is prime

    A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself

    Attributes:
        num (int): The number to check for primality
    """

    def __init__(self, number):
        """
        Initialize the Prime checker with a number

        Args:
            number (int): The number to check for primality
        """

        self.num = number

    def is_prime(self):
        """
        Check if the stored number is prime.

        Returns:
            bool: True if the number is prime, False otherwise
        """

        for i in range(2, self.num):

            if self.num % i == 0:

                return False

        return True


num = Prime(19)
print(num.is_prime())

print("#" * 50)


# Task 3
# ------
class Divisor:
    """
    A class for finding common divisors of two numbers and generating even numbers

    Attributes:
        num1 (int): The first number
        num2 (int): The second number
    """

    def __init__(self, number_1, number_2):
        """
        Initialize the Dividor with two numbers

        Args:
            number_1 (int): The first number
            number_2 (int): The second number
        """

        self.num1 = number_1
        self.num2 = number_2

    def dividors(self):
        """
        Find all common divisors of the two stored numbers

        A common divisor is a number that divides both numbers without a remainder

        Returns:
            list: A list of integers representing all common divisors, sorted in ascending order
        """

        minimum = min(self.num1, self.num2)
        common_dividors = []

        for i in range(1, minimum + 1):

            if self.num1 % i == 0 and self.num2 % i == 0:

                common_dividors.append(i)

        return common_dividors

    def even_fun(self, num):
        """
        Generate a list of even numbers from 0 up to (but not including) num.

        Args:
            num (int): The upper limit for generating even numbers.

        Returns:
            list: A list of even integers from 0 to num-1.
        """

        even_nums = []
        for i in range(num):

            if i % 2 == 0:

                even_nums.append(i)

        return even_nums


nums = Divisor(20, 10)
print(nums.dividors())
print(nums.even_fun(6))

print("#" * 50)


# Task 4
# ------
class LongestString:
    """
    A class for finding the longest common substring between two input strings

    The longest common substring is the longest sequence of characters that
    appears in both strings in the same order
    """

    def __init__(self):

        pass

    def longest_str(self):
        """
        Find the longest common substring between two user-input strings

        Prompts the user to enter two sentences and finds the longest substring
        that appears in both

        Returns:
            str: The longest common substring found. Returns an empty string if
                  no common substring exists
        """

        self.str1 = input("Enter the first sentence: ").strip()
        self.str2 = input("Enter the second sentence: ").strip()

        longest_str = ""

        for i in range(len(self.str1)):

            for j in range(i, len(self.str1)):

                sub_str = self.str1[i : j + 1]

                if sub_str in self.str2:

                    if len(sub_str) > len(longest_str):

                        longest_str = sub_str

        return longest_str


long_str = LongestString()
print(long_str.longest_str())

print("#" * 50)


# Task 5
# ------
class ReverseString:
    """
    A class for reversing the order of words in a string

    Takes a string and reverses the order of words (space-separated tokens),
    keeping the words themselves unchanged

    Attributes:
        str (str): The string to be reversed
    """

    def __init__(self, given_string):
        """
        Initialize the ReverseString with a string

        Args:
            given_string (str): The string whose words will be reversed
        """

        self.str = given_string

    def reverse_str(self):
        """
        Reverse the order of words in the stored string

        Returns:
            str: A new string with words in reverse order
        """

        lst = self.str.split(" ")
        new_lst = lst[::-1]
        new_str = " ".join(new_lst)

        return new_str


txt = ReverseString("Hello World")
print(txt.reverse_str())

print("#" * 50)

# Task 6
# ------
import random


class PasswordGenerator:
    """
    A class for generating random passwords with customizable length

    Generates passwords using a mix of lowercase letters, uppercase letters,
    digits, and special characters

    Attributes:
        length (int): The desired length of the generated password
    """

    def __init__(self, length):
        """
        Initialize the PasswordGenerator with a desired password length.

        Args:
            length (int): The number of characters in the generated password.
        """

        self.length = length

    def generate_password(self):
        """
        Generate a random password of the specified length

        The password includes lowercase letters (a-z), uppercase letters (A-Z),
        digits (0-9), and special characters (!@#$%^&*)

        Returns:
            str: A randomly generated password
        """

        characters = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
        )
        num_of_chars = len(characters)
        password = ""

        for i in range(self.length):

            rand_indx = random.randrange(
                0, num_of_chars
            )  # Generate random character for the password
            password += characters[rand_indx]  # Add a new character to the password

        return password


password = PasswordGenerator(13)
print(password.generate_password())

print("#" * 50)


# Task 7
# ------
class UniqueWords:
    """
    A class for filtering and counting unique words in a list

    Identifies unique words in a list and prints each word along with its
    frequency count
    """

    def __init__(self):

        pass

    def filter_words(self, words):
        """
        Print each unique word and its count from a list of words

        Args:
            words (list): A list of strings (words) to analyze

        Returns:
            None: Prints results to console in format "word:count"
        """

        unique_words = set(words)

        for word in unique_words:

            print(f"{word}:{words.count(word)}")


lst = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
words = UniqueWords()
words.filter_words(lst)

print("#" * 50)

# Task 9
# ------
import random


class ChatBot:
    """
    A simple rule-based chatbot that responds to user input

    The chatbot matches keywords in user input against predefined responses
    and provides random responses from matching categories. Continues chatting
    until the user says "goodbye"

    Attributes:
        responses (dict): A dictionary mapping keywords to lists of possible
                          responses
    """

    def __init__(self):
        """
        Initialize the ChatBot with predefined responses

        Sets up response templates for common greetings and a default response
        for unrecognized input
        """

        # Predefined responses
        self.responses = {
            "hello": ["Hello!", "Hi there!", "Greetings!"],
            "how are you": ["I'm doing well, thank you!", "I'm fine, how about you?"],
            "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
            "default": [
                "I'm sorry, I didn't understand.",
                "Could you please rephrase that?",
            ],
        }

    def get_response(self, user_input):
        """
        Get an appropriate response based on user input

        Searches for keywords in the user input and returns a random response
        from the matching category. Returns a default response if no keywords
        are found

        Args:
            user_input (str): The user's message

        Returns:
            str: A randomly selected response string
        """

        for key in self.responses:

            if key in user_input:

                return random.choice(self.responses[key])

        return random.choice(self.responses["default"])

    def chatbot(self):
        """
        Start the chatbot conversation loop

        Initiates a conversation with the user and continues responding to
        input until the user types "goodbye". All user input is converted
        to lowercase for matching

        Returns:
            None: Runs an interactive loop that prints to console
        """

        print("Chatbot: Hi! How can I assist you today?")

        while True:

            user_input = input("User: ").lower()
            response = self.get_response(user_input)
            print("Chatbot:", response)

            if user_input == "goodbye":

                break


bot = ChatBot()
bot.chatbot()
