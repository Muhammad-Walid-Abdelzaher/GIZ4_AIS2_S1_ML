# DEPI AI & ML Round 4
# Data Analysis - Numpy Assignment
# --------------------------------
# Made With <3 By Muhammad Walid
# Jan 31, 2026
# --------------------------------

import numpy as np

# Solving a problem of mine
outer_edges = np.ones(shape=(5, 5), dtype="int32")
inner_edges = np.full((3, 3), fill_value=0)
core = 9
inner_edges[1, 1] = core
outer_edges[1:-1, 1:-1] = inner_edges
# print(inner_edges)
print(outer_edges)

print("#" * 100)


# Part 1
# ------


def array_factory(mode, shape, value=None):
    """
    Creates various NumPy arrays based on the mode.
    - 'zeros': Array filled with 0.
    - 'ones': Array filled with 1.
    - 'full': Array filled with a specified 'value'.
    - 'identity': A square identity matrix of size 'shape'.
    """

    if mode == "zeros":

        return np.zeros(shape)  # Zeros Array

    elif mode == "ones":

        return np.ones(shape)  # Ones Array

    elif mode == "full":

        return np.full(shape=shape, fill_value=value)  # Specific Value Array

    elif mode == "identity":

        return np.identity(shape)  # Square Identity Array (Matrix)

    else:

        raise ValueError(f"Invalid Mode Option: {mode}")


print(array_factory("zeros", (2, 3)))

print("=" * 30)

print(array_factory("ones", (3, 4)))

print("=" * 30)

print(array_factory("full", (4, 5), "coding"))

# print(array_factory('empty', (4, 5)))

print("=" * 30)

print(array_factory("identity", 6))

print("#" * 30)

# Part 2
# ------
import numpy as np


def secure_reshape_and_stack(data1, data2, new_shape):
    """
    1. Validates and converts inputs to NumPy arrays.
    2. Reshapes the first dataset to a specific dimension.
    3. Vertically stacks both datasets into one matrix.
    """
    try:
        # Convert inputs to ndarray to ensure they are processed as Tensors
        # arr = np.array(data1)

        arr1 = np.array(data1)
        arr2 = np.array(data2)

        # Rule: Change the shape of arr1 to new_shape
        # Common usage: turning a vector (1D) into a matrix (2D)  by using reshape function
        reshaped_arr1 = arr1.reshape(new_shape)

        # Rule: Vertical Stacking (vstack)
        # Requirement: Both matrices must have the same number of columns
        combined_dataset = np.vstack((reshaped_arr1, arr2))

        return combined_dataset

    except ValueError as e:
        # Handle cases where reshape size doesn't match or stack columns don't match
        raise ValueError(f"Company-grade Error: {e}")


# Part 3
# ------


def apply_threshold(arr, threshold, replacement_value=-1):
    """
    Finds elements satisfying a condition (>= threshold)
    and replaces them with a new value.
    """
    # 1. Convert input to a numpy array (ndarray)
    arr = np.array(arr)
    # 2. Define the condition: elementwise comparison
    # This creates a Boolean numpy array
    condition = arr >= threshold

    # 3. Apply Modification using np.where()
    # np.where(condition, value_if_true, value_if_false)
    modified_arr = np.where(condition, replacement_value, arr)

    return modified_arr


# Test Case
# ---------

# Regional Branch A (Flat sales data)
branch_a = [1, 2, 3, 4, 5, 6]

# Regional Branch B (Already formatted 2x3 matrix)
branch_b = [[7, 8, 9], [10, 11, 12]]

# Reshape A to 2x3 and stack with B
final_report = secure_reshape_and_stack(branch_a, branch_b, (2, 3))
print(final_report)
# print(final_report.shape)  # Resulting shape: (4, 3)

print("#" * 30)  # Separator

v = np.array([1, 2, 3])
print(apply_threshold(v, 2, -20))
