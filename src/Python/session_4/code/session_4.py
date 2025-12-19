def reverse_vocab(s):
    """
    param_1 = recieve txt from user
    type param_1: string

    return: string
    type return: string
    """

    st_1 = s.split()
    reverse_str = st_1[::-1]
    new_str = " ".join(reverse_str)

    return new_str


txt = "Hello Muhammad"
print(reverse_vocab(txt))

print("#" * 50)  # Separator

import random


def generate_passcode(length):

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ""
    for i in range(length):

        password += random.choice(chars)

    return password


password_length = 8
print(generate_passcode(password_length))

print("#" * 50)  # Separator

words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
unique_words = set(words)
# print(unique_words)

counts = {word: 0 for word in unique_words}
for i in unique_words:

    for j in words:

        if i == j:

            counts[i] += 1

print(counts)


def count_words(words):

    unique_words = set(words)
    # print(unique_words)

    counts = {word: 0 for word in unique_words}
    for i in unique_words:

        for j in words:

            if i == j:

                counts[i] += 1

    return counts


words = ["Welcome", "Ali", "Hi", "Ali", "No", "Hi", "No", "Ali", "No", "Ali"]
print(count_words(words))

print("#" * 50)  # Separator

import random

responses = {
    "hello": ["hello!", "Hi there!", "Greetings!"],
    "how are you": ["I'm doing well, thank you", "I'm fine, how are you?"],
    "goodbye": ["Goodbye", "See you later", "farewell!"],
    "default": ["I'm Sorry, I did not understand.", "Could you please rephrase that?"],
}


def get_response(user_input):

    for key in responses:

        if key in user_input:

            return random.choice(responses[key])

    return random.choice(responses["default"])


def chatbot():

    print("chatbot: Hi! How can I help you today? ")

    while True:

        user_input = input("user: ").lower()
        chat_response = get_response(user_input)

        print("chatbot: ", chat_response)

        if user_input == "goodbye":

            break


# chatbot()  # Run The ChatBot

print("#" * 50)  # Separator

""" 
this class 



"""


class StudentInfo:

    student_name = "depi"
    std_age = 20
    std_gpa = 3.99
    gender = "male"

    def std_info(self):  # self => البطاقة بتاعتك (نَفْسَكْ) (التصريح بتاعك عشان تعِّدي)

        # print(student_name)
        print("Hello Muhammad!")


s1 = StudentInfo()

print(s1.student_name)
s1.student_name = "AMIT"
print(s1.student_name)

s1.std_info()

print(s1)

print("#" * 50)  # Separator


class test:

    def info(self):

        print(self)


x = test()

print(x)
x.info()

print("#" * 50)  # Separator


class Student:

    def __init__(self):

        print("Hello Muhammad :)")


s1 = Student()

print("#" * 50)  # Separator


class PasswordGenerator:

    def __init__(self, length):

        self.len = length
        self.chars = (
            "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        )

    def generate_passcode(self):

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
        password = ""
        for i in range(self.len):

            password += random.choice(chars)

        return password

if __name__ == "__main__":

    generator = PasswordGenerator(8)
    random_password = generator.generate_passcode()
    print(random_password)