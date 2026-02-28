# DEPI AI & ML Round 4
# Machine Learning Task
# ---------------------
# Made With <3 By Muhammad Walid
# Feb 28, 2026
# ------------------------------

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

        print(
            f"Optimized Parameters: slope (theta_1) = {self.w:.6f}, Bias (theta_0) = {self.b:.6f}"
        )

    def predict(self, X: list):
        X = np.array(X)
        y_predict = self.w * X + self.b
        return y_predict

    def fit_lasso(self, Lambda=0.1):
        """
        Performs gradient descent with L1 (Lasso) regularization.
        Lambda: regularization strength. Higher = more penalty on large weights.
        """

        self.w = 0
        self.b = 0
        self.sse_values = np.array([])

        for iteration in range(self.num_of_iterations):
            # Here comes the difference between 'ridge' and 'GD'
            dl_dw = (2 / self.n) * np.sum(
                (((self.w * self.x) + self.b) - self.y) * self.x
            ) + Lambda * np.sign(self.w)
            dl_db = (2 / self.n) * np.sum(((self.w * self.x) + self.b) - self.y)

            self.w -= self.alpha * dl_dw
            self.b -= self.alpha * dl_db

            y_hat = (self.w * self.x) + self.b
            sse = np.sum((y_hat - self.y) ** 2)
            self.sse_values = np.append(arr=self.sse_values, values=sse)

            if iteration % 20 == 0:
                print(f"Lasso Iteration No.: {iteration}", "-" * 17, sep="\n")
                print(
                    f"New 'w': {self.w:.6f}, New 'b': {self.b:.6f}, SSE: {self.sse_values}"
                )
                print("=" * 30)

        print(
            f"Lasso Optimized Parameters: slope (theta_1) = {self.w:.6f}, Bias (theta_0) = {self.b:.6f}"
        )

    def fit_ridge(self, Lambda=0.1):
        """
        Performs gradient descent with L2 (Ridge) regularization.
        Lambda: regularization strength. Higher = more penalty on large weights.
        """

        self.w = 0
        self.b = 0
        self.sse_values = np.array([])

        for iteration in range(self.num_of_iterations):
            # Here comes the difference between 'ridge' and 'GD'
            dl_dw = (2 / self.n) * np.sum(
                (((self.w * self.x) + self.b) - self.y) * self.x
            ) + 2 * Lambda * self.w
            dl_db = (2 / self.n) * np.sum(((self.w * self.x) + self.b) - self.y)

            self.w -= self.alpha * dl_dw
            self.b -= self.alpha * dl_db

            y_hat = (self.w * self.x) + self.b
            sse = np.sum((y_hat - self.y) ** 2)
            self.sse_values = np.append(arr=self.sse_values, values=sse)

            if iteration % 20 == 0:
                print(f"Ridge Iteration No.: {iteration}", "-" * 17, sep="\n")
                print(
                    f"New 'w': {self.w:.6f}, New 'b': {self.b:.6f}, SSE: {self.sse_values}"
                )
                print("=" * 30)

        print(
            f"Ridge Optimized Parameters: slope (theta_1) = {self.w:.6f}, Bias (theta_0) = {self.b:.6f}"
        )


if __name__ == "__main__":

    x = np.array([1, 2, 3, 4])
    y = np.array([2, 2.8, 3.6, 4.5])
    # y = np.array([2, 2.2, 3.6, 4.7])

    linear = LinearRegression_muhammad_walid(
        alpha=0.01, weight=0, bias=0, num_of_iteration=100, x_data=x, y_data=y
    )

    print(linear.mean_squared_error())

    print("#" * 30)

    linear.fit()  # w = 1.025995, b = 0.573752

    # Will use it later for visualization
    linear_results = (
        "Linear Regression",
        linear.w,
        linear.b,
        linear.sse_values,
        "blue",
    )

    print("#" * 30)

    print(linear.predict(9))

    print("#" * 30)

    linear.fit_lasso()  # w = 1.011733, b = 0.598079
    lasso_results = ("Lasso Regression", linear.w, linear.b, linear.sse_values, "red")

    print("#" * 30)

    linear.fit_ridge()  # w = 0.997637, b = 0.621843
    ridge_results = ("Ridge Regression", linear.w, linear.b, linear.sse_values, "green")

    print("#" * 30)

    # Visualization for Linear, Lasso, and Ridge Regression
    # -----------------------------------------------------
    # Create the configuration list
    configs = [linear_results, lasso_results, ridge_results]

    # Create smooth x values for plotting
    x_line = np.linspace(min(x), max(x), 100)

    configs = [linear_results, lasso_results, ridge_results]
    x_line = np.linspace(min(x), max(x), 100)

    fig, axes = plt.subplots(2, 3, figsize=(15, 8))
    fig.suptitle("Linear vs Lasso vs Ridge", fontsize=14, fontweight="bold")

    for col, (title, w, b, sse_vals, color) in enumerate(configs):

        # Top row: regression line
        axes[0, col].scatter(x, y, color="black", zorder=5, label="Data points")
        axes[0, col].plot(
            x_line,
            w * x_line + b,
            color=color,
            linewidth=2,
            label=f"w={w:.4f}, b={b:.4f}",
        )
        axes[0, col].set_title(title)
        axes[0, col].set_xlabel("x")
        axes[0, col].set_ylabel("y")
        axes[0, col].legend(fontsize=8)
        axes[0, col].grid(True, linestyle="--", alpha=0.5)

        # Bottom row: SSE curve
        axes[1, col].plot(range(len(sse_vals)), sse_vals, color=color, linewidth=2)
        axes[1, col].set_title(f"SSE — {title}")
        axes[1, col].set_xlabel("Iteration")
        axes[1, col].set_ylabel("SSE")
        axes[1, col].grid(True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()
