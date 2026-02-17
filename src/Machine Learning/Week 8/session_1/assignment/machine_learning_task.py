# DEPI AI & ML Round 4
# Machine Learning Task
# ---------------------
# Made With <3 By Muhammad Walid
# Feb 18, 2026
# ------------------------------

import os

# Change The Current Working Directory (CWD)
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib.pyplot as plt
from machine_learning import LinearRegression_muhammad_walid
# from sklearn.linear_model import LinearRegression


# Task 1: Load & Understand the Data
# ----------------------------------

X = [50, 60, 70, 80, 90]
y = [150, 180, 210, 240, 270]  # house price in thousands

# Explanation:
# ------------
# X => Independent Variable (Feature)        => House Area   (in m**2)
# y => Dependent Variable (Target or Output) => House Prices (in thousands)

X_array = np.array(X)
y_array = np.array(y)

# Task 2: Create and Train the Model
# ----------------------------------

learning_rate = 0.001
n_iters = 100

linear_model = LinearRegression_muhammad_walid(
    alpha=learning_rate,
    num_of_iteration=n_iters,
    weight=3,
    bias=0,
    x_data=X_array,
    y_data=y_array,
)

linear_model.fit()

# Answer for the question:
# Linear Regression Equation: y_hat (or y_predict) = w ** x + b
# "theta_0" is the "Bias" (b) or "Intercept", "theta_1" is the "Slope" (w)

print("#" * 30)  # Separator

# Task 3: Prediction
# ------------------

print(linear_model.predict(70))

print("#" * 30)  # Separator

# Answer for the question:
# Yes, as the dataset is perfectly linear (70 m**2 is already in the dataset)

# Task 4: Visualization
# ---------------------

# SSE over iterations
plt.figure(figsize=(6, 4))
plt.plot(linear_model.sse_values)
plt.xlabel("Iterations")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("SSE vs Iterations (Gradient Descent)")
plt.grid(True)
plt.show()


# Regression Line with data points
y_pred = linear_model.predict(X)
# print(y_pred)

plt.figure(figsize=(6, 4))
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")
plt.xlabel("House Size (m²)")
plt.ylabel("House Price (Thousands)")
plt.title("Linear Regression Fit")
plt.legend()
plt.grid(True)
plt.show()

# Q: Why does SSE decrease over time?
# A: => Gradient Descent updates parameters in the direction of lower error
#    => Each iteration reduces the distance between predictions and true values

# Q: What does convergence mean?
# A: => Parameters stop changing significantly
#    => SSE stops decreasing
#    => Model has reached (or is very close to) the minimum error

# Task 5: Experimentation
# -----------------------

large_learning_rate = 0.1
n_iters = 100

large_linear_model = LinearRegression_muhammad_walid(
    alpha=learning_rate,
    num_of_iteration=n_iters,
    weight=3,
    bias=0,
    x_data=X_array,
    y_data=y_array,
)

linear_model.fit()

print("#" * 50)  # Separator

large_learning_rate = 0.00001
n_iters = 100

small_linear_model = LinearRegression_muhammad_walid(
    alpha=learning_rate,
    num_of_iteration=n_iters,
    weight=3,
    bias=0,
    x_data=X_array,
    y_data=y_array,
)

linear_model.fit()
