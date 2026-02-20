# 4-7 Problems
# ------------
# Feb 20, 2026
# Made With <3 By Muhammad Walid
# ------------------------------

# Problem 4: Add Two Numbers (LeetCode)
# --------------------------


class Solution1:
    def addTwoNumbers(self, l1: list, l2: list) -> list:
        """Add the two numbers and return the sum as a linked list

        Args:
            l1 (list): First Number as a Linked List
            l2 (list): Second Number as a Linked List

        Returns:
            list: Sum of the two numbers as a Linked List

        Examples:
            Input: l1 = [2,4,3], l2 = [5,6,4]
            Output: [7,0,8]
            Explanation: 342 + 465 = 807
        """

        # list_of_first_string = []
        # list_of_second_string = []
        # for num in l1[::-1]:
        #     list_of_first_string.append(str(num))

        # for num in l2[::-1]:
        #     list_of_second_string.append(str(num))

        # first_string = "".join(list_of_first_string)
        # second_string = "".join(list_of_second_string)

        # first_num = int(first_string)
        # second_num = int(second_string)

        # # print(first_num)
        # # print(second_num)

        # sum_num = first_num + second_num
        # # print(sum_num)

        # sum_linked_list = []
        # for num in list(str(sum_num)[::-1]):
        #     sum_linked_list.append(int(num))

        # return sum_linked_list

        # Another Way (More Efficient)
        reversed_l1 = l1[::-1]
        reversed_l2 = l2[::-1]

        list_of_first_string = "".join(map(str, reversed_l1))
        list_of_second_string = "".join(map(str, reversed_l2))

        first_num = int(list_of_first_string)
        second_num = int(list_of_second_string)

        # print(first_num)
        # print(second_num)

        sum_num = str(first_num + second_num)
        # print(sum_num)

        sum_linked_list = list(sum_num)[::-1]
        return sum_linked_list


sol_1 = Solution1()
print(sol_1.addTwoNumbers([2, 4, 3], [5, 6, 4]))  # [7,0,8]
print(sol_1.addTwoNumbers([0], [0]))  # [0]
print(sol_1.addTwoNumbers([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]))  # [8,9,9,9,0,0,0,1]

print("#" * 30)  # Separator

# Problem 5: Roman to Integer (LeetCode)
# ---------------------------


class Solution2:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = 0

        for i in range(len(s)):
            if i > 0 and roman[s[i]] > roman[s[i - 1]]:
                value += roman[s[i]] - 2 * roman[s[i - 1]]

            else:
                value += roman[s[i]]

        return value


sol_2 = Solution2()
print(sol_2.romanToInt("III"))  # 3
print(sol_2.romanToInt("LVIII"))  # 58
print(sol_2.romanToInt("MCMXCIV"))  # 1994

print("#" * 30)  # Separator

# Problem 6: Search Insert Position (LeetCode)
# ---------------------------------


class Solution3:
    def searchInsert(self, nums: list[int], target: int) -> int:
        if target in nums:
            return nums.index(target)

        else:
            for num in nums:
                if num > target:
                    return nums.index(num)

            else:
                return len(nums)


sol_3 = Solution3()
print(sol_3.searchInsert([1, 3, 5, 6], 5))  # 2
print(sol_3.searchInsert([1, 3, 5, 6], 2))  # 1
print(sol_3.searchInsert([1, 3, 5, 6], 7))  # 4

print("#" * 30)  # Separator

# Problem 7: Basic Calculator II (LeetCode)
# ------------------------------

class Solution4:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = '+'

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char in '+-*/' or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                
                elif sign == '-':
                    stack.append(-num)
                
                elif sign == '*':
                    stack.append(stack.pop() * num)
                
                elif sign == '/':
                    stack.append(stack.pop() / num)  # truncate toward zero

                sign = char
                num = 0

        return sum(stack)

sol_4 = Solution4()
print(sol_4.calculate("3+2*2"))
print(sol_4.calculate(" 3/2 "))
print(sol_4.calculate(" 3+5 / 2 "))
