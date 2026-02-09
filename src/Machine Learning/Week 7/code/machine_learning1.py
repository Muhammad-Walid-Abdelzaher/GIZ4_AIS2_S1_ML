import numpy as np
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

plt.figure(figsize = (12,5))
plt.subplot(1,2,1)
plt.plot(range(num_iteration), sse_values , label="SSE")
plt.xlabel("Number of Iteration")
plt.ylabel("SSE")
plt.title("SSE Over Iteration")
plt.legend()
plt.subplot(1,2,2)
plt.scatter(x,y , color = "blue" , label= "Data points")
plt.plot(x, w*x +b , color = "red" , label = "regression line")
plt.show()

# y-Predict ... العادية yدي غير ال
y = w * x + b
print(y)

class LinearRegression_muhammad_walid:

    def __init__(self):
        pass