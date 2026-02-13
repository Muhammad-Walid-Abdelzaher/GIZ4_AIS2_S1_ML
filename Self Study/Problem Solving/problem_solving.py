# 1-3 Problems
# ------------
# Feb 13, 2026
# Made With <3 By Muhammad Walid
# ------------------------------

# Problem 1: Reversed Words (Codewars)
# -------------------------


def reverseWords(given_string: str) -> str:
    words_list = given_string.split()
    reversed_words_list = words_list[::-1]
    reversed_words = " ".join(reversed_words_list)
    return reversed_words


print(reverseWords("The greatest victory is that which requires no battle"))

print("#" * 30)  # Separator

# Problem 2: Are You Playing Banjo? (Codewars)
# ---------------------------------


def are_you_playing_banjo(name: str) -> str:
    try:
        if not isinstance(name, str):
            raise ValueError(
                f"Name MUST be a string, got '{type(name).__name__}' instead."
            )

    except ValueError as VE:
        return f"Value Error: {VE}"

    else:
        if name.startswith(("R", "r")):
            return name + " plays banjo"

        else:
            return name + " does not play banjo"


print(are_you_playing_banjo("Muhammad"))
print(are_you_playing_banjo(1001101_1010111))
print(are_you_playing_banjo("Rami"))
print(are_you_playing_banjo("raouf"))

print("#" * 30)  # Separator

# Problem 3: Two Sum (LeetCode)
# ------------------


class Solution1:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for first_index, first_num in enumerate(nums):
            value_left_to_meet_target = target - first_num

            for second_index, second_num in enumerate(nums):
                if (value_left_to_meet_target == second_num):  # OR => # if (first_num + second_num) == target:
                    return [first_index, second_index]
                    # return [first_num, second_num]

                else:
                    continue


# The problem with this solution is the "Time Complexity" (n**2) as it loops over the same element twice

test_1 = Solution1()
print(test_1.twoSum([2, 7, 11, 15], 9))

test_2 = Solution1()
print(test_2.twoSum([3, 2, 4], 6))

test_3 = Solution1()
print(test_3.twoSum([3, 3], 6))

print("=" * 30)  # Separator


# Another Way (More Efficient with less Time Complexity "n(n-1)/2")
class Solution2:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for index_1 in range(len(nums)):

            for index_2 in range(index_1 + 1, len(nums)):
                # print(nums[index_1])
                # print(nums[index_2])
                if (nums[index_1] + nums[index_2]) == target:
                    return [index_1, index_2]
                    # return [nums[index_1], nums[index_2]]


test_4 = Solution2()
print(test_4.twoSum([2, 7, 11, 15], 9))

test_5 = Solution2()
print(test_5.twoSum([3, 2, 4], 6))

test_6 = Solution2()
print(test_6.twoSum([3, 3], 6))
