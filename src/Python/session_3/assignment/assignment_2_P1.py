# DEPI AI & ML Round 4
# Python - Assignment 2_1
# -----------------------
# Made With <3 By Muhammad Walid
# Dec 11, 2025
# ------------------------------

# Task 1
# ------
email = "Amit_ml@gmail.edu"
# email = "Amit_ml@bellsouth.rr.com"

# Check Validation Of The Email
# Only One '@' and One OR More '.' after the '@'
if email.count("@") == 1 and email[email.index("@") + 1 :].count(".") >= 1:

    # Extract Username
    print(email[: email.index("@")])

    # Extract Domain
    print(email[email.index("@") + 1 : email.rindex(".")])

    # Check High Level Domain
    if email.endswith(".com"):

        print("Commercial Domain")

    elif email.endswith(".edu"):

        print("Educational Domain")

    else:

        print("Other Domain")

else:

    print("Invalid Email.")

print("#" * 50)  # Separator

# Task 2
# ------
encoded_message = "###!!@emocleW PGTQ!!!6789"

# Decoding
# Extracting The Core Part Of The Message
filtered_chars = []
for char in encoded_message:

    if char.isalpha() or char.isspace():

        filtered_chars.append(char)

core_message = "".join(filtered_chars)
# print(core_message)  # emocleW PGTQ

# Reversing First Word To Get The Word "Welcome"
words_list = core_message.split()
first_word = words_list[0][::-1]
# print(first_word)  # Welcome

second_word = words_list[1]

# Final Decoded Message
final_message = first_word + " " + second_word
print(final_message)  # Welcome PGTQ

print("#" * 50)  # Separator

# Task 3
# ------
encoded_message = "&&&**$gnirtS PLIO!!@1234"

# Decoding
filtered_chars = [
    char for char in encoded_message if char.isalpha() or char.isspace()
]  # List Comprehension

core_message = "".join(filtered_chars)
# print(core_message)  # gnirtS PLIO

# Reversing First Word To Get The Word "String"
words_list = core_message.split()
first_word = words_list[0][::-1]
# print(first_word)  # String

# Reversing First Word To Get The Word "String"
# Replace Some Characters In The Second Word To Get The Word "PLEU"
second_word_chars = []
for char in words_list[1]:

    if char == "I":

        char = "E"

    elif char == "O":

        char = "U"

    second_word_chars.append(char)

second_word = "".join(second_word_chars)
# print(second_word)  # PLEU

# Final Decoded Message
final_message = first_word + " " + second_word
print(final_message)  # String PLEU

print("#" * 50)  # Separator

# Task 4
# ------
encoded_message = "##$$$@!yalpstcejorp EPUVT****9887"

# Decoding
filtered_chars = [char for char in encoded_message if char.isalpha() or char.isspace()]

core_message = "".join(filtered_chars)
# print(core_message)  # yalpstcejorp EPUVT

# Reversing First Word To Get The Word "projectsplay"
words_list = core_message.split()
first_word = words_list[0][::-1]
# print(first_word)  # projectsplay

# Replace Some Characters In The Second Word To Get The Word "APOVT"
second_word_chars = []
for char in words_list[1]:

    if char == "E":

        char = "A"

    elif char == "U":

        char = "O"

    second_word_chars.append(char)

second_word = "".join(second_word_chars)

# Final Decoded Message
final_message = first_word + " " + second_word
print(final_message)  # projectsplay APOVT
