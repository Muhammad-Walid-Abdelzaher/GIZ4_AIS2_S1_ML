import numpy as np
import matplotlib.pyplot as plt


class LinearRegression_muhammad_walid:

    def __init__(self, alpha, weight, bias, num_of_iteration, x_data, y_data):
        self.alpha = alpha
        self.w = weight  # 'w' or "weight" or "theta_1"
        self.b = bias  # 'b' or "bias" or "theta_0"
        self.n = len(x_data)
        self.num_of_iterations = num_of_iteration

        self.x = x_data
        self.y = y_data
        self.sse_values = np.array([])

    def mean_squared_error(self):
        y_hat = (self.w * self.x) + self.b  # "y_hat" or "y_predict"
        sse = np.sum((y_hat - self.y) ** 2)  # 'SSE' or "Sum Squared Error"
        mse = (1 / self.n) * sse  # 'MSE' or "Mean Squared Error"
        return f"MSE: {mse}"

    def gradient_descent(self):
        dl_dw = (2 / self.n) * np.sum((((self.w * self.x) + self.b) - self.y) * self.x)
        dl_db = (2 / self.n) * np.sum(((self.w * self.x) + self.b) - self.y)

        self.w -= self.alpha * dl_dw
        self.b -= self.alpha * dl_db


        y_hat = (self.w * self.x) + self.b
        sse = np.sum((y_hat - self.y) ** 2)
        self.sse_values = np.append(arr=self.sse_values, values=sse)

    def fit(self):

        for iteration in range(self.num_of_iterations):
            # print(f"Current 'w': {self.w:.6f}, Current 'b': {self.b:.6f}")
            self.gradient_descent()
            # print(f"Iteration No.: {iteration}", "-" * 17, sep="\n")
            # print(
            #     f"New 'w': {self.w:.6f}, New 'b': {self.b:.6f}, SSE: {self.sse_values}"
            # )
            # print("=" * 30)

            if iteration % 20 == 0:
                print(f"Iteration No.: {iteration}", "-" * 17, sep="\n")
                print(
                    f"New 'w': {self.w:.6f}, New 'b': {self.b:.6f}, SSE: {self.sse_values}"
                )
                print("=" * 30)

        print(f"Optimized Parameters: slope = {self.w:.6f}, Bias = {self.b:.6f}")

    def predict(self, X: list):
        X = np.array(X)
        y_predict = self.w * X + self.b
        return f"Prediction = {y_predict:.6f}"


x = np.array([1, 2, 3, 4])
y = np.array([2, 2.8, 3.6, 4.5])
# y = np.array([2, 2.2, 3.6, 4.7])

linear = LinearRegression_muhammad_walid(
    alpha=0.01, weight=0, bias=0, num_of_iteration=100, x_data=x, y_data=y
)

print(linear.mean_squared_error())

print("#" * 30)

linear.fit()

print("#" * 30)

print(linear.predict(9))

plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(range(linear.num_of_iterations), linear.sse_values, label="SSE")
plt.xlabel("Number of Iteration")
plt.ylabel("SSE")
plt.title("SSE Over Iteration")
plt.legend()
plt.subplot(1, 2, 2)
plt.scatter(linear.x, linear.y, color="blue", label="Data points")
plt.plot(linear.x, linear.w * linear.x + linear.b, color="red", label="regression line")
plt.show()
