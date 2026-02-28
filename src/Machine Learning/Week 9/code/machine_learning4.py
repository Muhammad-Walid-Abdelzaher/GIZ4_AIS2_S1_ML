import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error, root_mean_squared_error
import warnings

warnings.filterwarnings("ignore")
from sklearn.preprocessing import PolynomialFeatures

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\Drive\Data\Salary_Data.csv"
data = pd.read_csv(data_path)

data.head()

x = data.iloc[:, :-1]
y = data.iloc[:, 1]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, train_size=0.8, random_state=10
)

poly = PolynomialFeatures(degree=15)
x_poly_train = poly.fit_transform(x_train)
x_poly_test = poly.transform(x_test)

# print(x_poly_train)

# fit => Grab the Information
# transform => Applyبيـ

poly_model = LinearRegression()
poly_model.fit(x_poly_train, y_train)

y_poly_predict_train = poly_model.predict(x_poly_train)
y_poly_predict_test = poly_model.predict(x_poly_test)

x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
x_range_poly = poly.transform(x_range)
y_range_predict = poly_model.predict(x_range_poly)

# Visualization
plt.scatter(x_train, y_train, color="red", label="Training Data")
plt.scatter(x_test, y_test, color="green", label="Testing Data")
plt.plot(x_range, y_range_predict, color="blue", label="Polynomial Regression")
plt.title("Salary vs. Experience")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.legend()
# plt.show()

mse = mean_squared_error(y_test, y_poly_predict_test)
print(mse)

rmse = root_mean_squared_error(y_test, y_poly_predict_test)
print(rmse)

r2 = r2_score(y_test, y_poly_predict_test)
print(r2)

print("#" * 30)

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\Drive\Data\Social_Network_Ads.csv"
data = pd.read_csv(data_path)

print(data.head())

x = data.iloc[:, [2, 3]].values
# print(x)

y = data.iloc[:, 4].values
print(y)

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=10
)

# MinMaxScaler => Range: [0 - 1]
# StandardScaler => Range: [-1 - 1]

from sklearn.preprocessing import StandardScaler

sc_x = StandardScaler()
x_train = sc_x.fit_transform(x_train)
x_test = sc_x.transform(x_test)

from sklearn.linear_model import LogisticRegression

classifier = LogisticRegression()
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)

print("-" * 50)

# ...

from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score

cm = confusion_matrix(y_test, y_pred)
print(cm)

print("#" * 30)

tp, tn, fp, fn = cm.ravel()

accuracy_score_ =accuracy_score(y_test, y_pred)

recall_score_=recall_score(y_test, y_pred)
precision_score_=precision_score(y_test, y_pred)
f1_score_=f1_score(y_test, y_pred)
print('accuracy_score_',accuracy_score_)
print('recall_score_',recall_score_)
print('precision_score_',precision_score_)
print('f1_score_',f1_score_)

# Visualising the Training set results
from matplotlib.colors import ListedColormap
X_Set, Y_Set = x_train, y_train
X1, X2 = np.meshgrid(np.arange(start = X_Set[:,0].min() -1, stop = X_Set[:, 0].max() +1, step = 0.01),
                     np.arange(start = X_Set[:,1].min() -1, stop = X_Set[:, 1].max() +1, step = 0.01))
 
 
plt.contourf(X1,X2, classifier.predict(np.array([X1.ravel(), X2.ravel()]).T).reshape(X1.shape),
             alpha = 0.75, cmap = ListedColormap(('red', 'green')))
 
plt.xlim(X1.min(), X2.max())
plt.ylim(X2.min(), X2.max())
for i, j in enumerate(np.unique(Y_Set)):
    plt.scatter(X_Set[Y_Set == j, 0], X_Set[Y_Set == j,1],
                c = ListedColormap(('yellow', 'blue'))(i), label = j)
plt.title('Logistic Regression ( Training set)')
plt.xlabel('Age')
plt.ylabel('Estimated Salary')
plt.legend()
plt.show()