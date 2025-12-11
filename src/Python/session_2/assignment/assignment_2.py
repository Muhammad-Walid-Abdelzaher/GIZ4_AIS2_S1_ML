# DEPI AI & ML Round 4
# Python - Assignment 2
# ---------------------
# Made With <3 By Muhammad Walid
# Dec 11, 2025
# ------------------------------

# Task 1
# ------
email = "Amit_ml@gmail.edu"
# email = "Amit_ml@bellsouth.rr.com"

# Check Validation Of The Email
# Only one '@' and one or more '.' after the '@'
if email.count("@") == 1 and email[email.index("@") + 1 :].count(".") >= 1:

    # Extract Username
    print(email[: email.index("@")])

    # Extract Domain
    print(email[email.index("@") + 1 : email.rindex(".")])

    # Check High Level Domain
    if email[email.rindex(".") :] == ".com":

        print("Commercial Domain")

    elif email[email.rindex(".") :] == ".edu":

        print("Educational Domain")

    else:

        print("Other Domain")

else:

    print("Invalid Email.")

print("#" * 50)  # Separator

# Task 2
# ------
encoded_message = "###!!@mocleW EPGTQ!!!6789"

# Decoding
