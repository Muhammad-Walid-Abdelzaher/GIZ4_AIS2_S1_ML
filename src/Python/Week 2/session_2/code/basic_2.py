list_one = [1, 2, 3, 5, "amit", "learning", True, [1, 2, 3, "True", ["ml", "dl", "ds"]]]
print(type(list_one))

list_one = [1, 2, 3, 5, "amit", "learning", True, [1, 2, 3, "True", ["ml", "dl", "ds"]]]
print(list_one[4])

print(list_one[7][1])

list_one[7][1] = "Depi"

print(list_one[7][1])

print("#" * 50)

list_two = ["amit", "learning", "Python"]
list_two.append("ml")

print(list_two)

list_two.insert(1, "DEPI")

print(list_two)

print("#" * 50)

list_1 = [1, 2, 3]
list_2 = [3, 4, 5]
print(list_1 + list_2)

print(list_1)  # No Change

print("#" * 50)

list_1.extend(list_2)
print(list_1)

print("#" * 50)

list1 = ["amit", "learning", "Python"]
list1.remove("learning")
print(list1)

print("#" * 50)

list2 = ["amit", "learning", "Python"]
list2.pop(0)
print(list2)

print("#" * 50)

del list1  # Remove The Entire List

# print(list1)  # NameError

list1 = [1, 2, 3]
print(list1 * 2)

print("#" * 50)

# input_list = [1, 2, 3]
# user_input = int(input("What's the item you want to delete? ").strip())

# input_list.remove(user_input)

# print(input_list)

print("#" * 50)

dict_1 = {
    "key1": 12.5,
    "key2": "value2",
}

print(dict_1["key1"])
print(dict_1["key2"])
print(type(dict_1["key1"]))
print(type(dict_1["key2"]))

print("#" * 50)

# Quiz
num_1 = int(input("What's the first number?: ").strip())
num_2 = int(input("What's the second number?: ").strip())

addition = num_1 + num_2
subtraction = num_1 - num_2
multiplication = num_1 * num_2
division = num_1 / num_2

print(f"{num_1} + {num_2} = {addition}")
print(f"{num_1} - {num_2} = {subtraction}")
print(f"{num_1} * {num_2} = {multiplication}")
print(f"{num_1} / {num_2} = {division}")

print("#" * 50)

try:

    marks = int(input("What's the total marks?: ").strip())

    if marks > 100:

        raise Exception

except:

    print("Make sure that you enter an integer")

else:

    pass
