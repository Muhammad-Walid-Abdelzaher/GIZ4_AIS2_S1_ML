import numpy as np
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

x = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])

lin_reg = LinearRegression()
lin_reg.fit(x, y)
y_predict_lin = lin_reg.predict(x)

print(y_predict_lin)  # [2. 4. 6. 8.]
print(lin_reg.coef_)  # [2.]
print(lin_reg.intercept_)  # 0.0

print("#" * 30)

ridge = Ridge(alpha=10.0)
ridge.fit(x, y)
y_predict_ridge = ridge.predict(x)

print(y_predict_ridge)  # [2. 4. 6. 8.]
print(ridge.coef_)  # [2.]
print(ridge.intercept_)  # 0.0

print("#" * 30)

lasso = Lasso(alpha=10.0)
lasso.fit(x, y)
y_predict_lasso = lasso.predict(x)

print(y_predict_lasso)
print(lasso.coef_)
print(lasso.intercept_)

print("#" * 30)

print("Linear Regression:")
print("MSE:", mean_squared_error(y, y_predict_lin))
print("R2:", r2_score(y, y_predict_lin))

print("=" * 30)

print("Ridge Regression:")
print("MSE:", mean_squared_error(y, y_predict_ridge))
print("R2:", r2_score(y, y_predict_ridge))

print("=" * 30)

print("Lasso Regression:")
print("MSE:", mean_squared_error(y, y_predict_lasso))
print("R2:", r2_score(y, y_predict_lasso))


plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_predict_lin, color="red", label="Linear Regression")
plt.title("Linear Regression")
plt.show()

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_predict_ridge, color="red", label="Ridge Regression")
plt.title("Ridge Regression")
plt.show()

plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_predict_lasso, color="red", label="Lasso Regression")
plt.title("Lasso Regression")
plt.show()

plt.scatter(x, y, color="blue", label="Actual Data")
plt.plot(x, y_predict_lin, color="red", label="Linear Regression")
plt.plot(x, y_predict_ridge, color="green", linestyle="--", label="Ridge Regression")
plt.plot(x, y_predict_lasso, color="purple", linestyle=":", label="Lasso Regression")
plt.title("Comparison of Linear, Ridge & Lasso Regressions")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
