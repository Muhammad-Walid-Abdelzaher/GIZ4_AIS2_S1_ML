import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4])
y = np.array([2, 2.2, 3.6, 4.7])

w = 0
b = 0
alpha = 0.01
num_iteration = 20

# from sklearn.linear_model import LinearRegression

# Sum Square Error (SSE)
sse_values = []
for i in range(num_iteration):
    y_hat = w * x + b

    delta_w = 2 * np.sum((y_hat - y) * x)
    delta_b = 2 * np.sum((y_hat - y) * 1)

    w -= alpha * delta_w  # OR => w = w - alpha * delta_w
    b -= alpha * delta_b  # OR => b = b - alpha * delta_b

    sse = np.sum((y_hat - y) ** 2)
    sse_values.append(sse)

    if (i + 1) % 20 == 0:
        print(f"Iteration {i + 1}, SSE: {sse}")

print(f"Optimized Parameters: Bias = {b}, Slope = {w}")

print("#" * 30)

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range(num_iteration), sse_values, label="SSE")
plt.xlabel("Number of Iteration")
plt.ylabel("SSE")
plt.title("SSE Over Iteration")
plt.legend()
plt.subplot(1, 2, 2)
plt.scatter(x, y, color="blue", label="Data points")
plt.plot(x, w * x + b, color="red", label="regression line")
plt.show()

# y-Predict ... العادية yدي غير ال
y = w * x + b
print(y)


class LinearRegression_muhammad_walid:

    def __init__(self):
        pass

    def fit(self, x):
        pass


# linear = LinearRegression_muhammad_walid(alpha=0.01, w, b, 20)


def NormalDist(*w):
    pass


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error
import warnings

warnings.filterwarnings("ignore")

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Machine Learning\Week 8\materials\Salary_Data.csv"
data = pd.read_csv(data_path)
print(data.head())

print("#" * 30)

plt.figure(figsize=(3, 3))
sns.pairplot(
    data, x_vars=["YearsExperience"], y_vars=["Salary"], size=7, kind="scatter"
)
plt.xlabel("Years")
plt.ylabel("Salary")
plt.title("Salary Prediction")
# plt.show()

x = data.iloc[:, :-1]
y = data.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, random_state=10
)

linear_model = LinearRegression()
linear_model.fit(x_train, y_train)

plt.scatter(x_train, y_train, color="red")
plt.plot(x_train, linear_model.predict(x_train), color="blue")
plt.title("Salary vs. Experience (Training Set)")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
# plt.show()

print(y_test)

print("#" * 30)

y_predict = linear_model.predict(x_test)
print(y_predict)

print("#" * 30)

mse = mean_squared_error(y_test, y_predict)
print(mse)

rmse = root_mean_squared_error(y_test, y_predict)
print(rmse)

print("#" * 30)

r2_scr = r2_score(y_test, y_predict)
print(r2_scr)
