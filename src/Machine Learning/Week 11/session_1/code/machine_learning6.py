import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Machine Learning\Week 11\materials\PlayTennis.csv"
data = pd.read_csv(data_path)

print(data.head(2))

print("#" * 30)

outlook_encoder = OrdinalEncoder()
data["Outlook"] = outlook_encoder.fit_transform(data[["Outlook"]])
print(data)

print("#" * 30)

temp_encoder = OrdinalEncoder()
data["Temperature"] = temp_encoder.fit_transform(data[["Temperature"]])
print(data)

print("#" * 30)

hu_encoder = OrdinalEncoder()
data["Humidity"] = hu_encoder.fit_transform(data[["Humidity"]])
print(data)

print("#" * 30)

wind_encoder = OrdinalEncoder()
data["Wind"] = wind_encoder.fit_transform(data[["Wind"]])
print(data)

print("#" * 30)

play_encoder = OrdinalEncoder()
data["Play Tennis"] = play_encoder.fit_transform(data[["Play Tennis"]])
print(data)

print("#" * 30)

x = data.drop(["Play Tennis"], axis=1)
y = data["Play Tennis"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

clf = DecisionTreeClassifier(criterion="gini", random_state=42)
clf.fit(x_train, y_train)

y_pred = clf.predict(x_test)

print("#" * 30)

clf_entropy = DecisionTreeClassifier(criterion="entropy", random_state=42)
clf_entropy.fit(x_train, y_train)

y_pred_entropy = clf_entropy.predict(x_test)

print("#" * 30)

print("Accuracy (Gini):", accuracy_score(y_test, y_pred))
print("Classification Report (Gini):\n", classification_report(y_test, y_pred))
print("Confusion Matrix (Gini):\n", confusion_matrix(y_test, y_pred))

print("=" * 30)

print("Accuracy (Entropy):", accuracy_score(y_test, y_pred_entropy))
print(
    "Classification Report (Entropy):\n", classification_report(y_test, y_pred_entropy)
)
print("Confusion Matrix (Entropy):\n", confusion_matrix(y_test, y_pred_entropy))

print("#" * 30)

plt.figure(figsize=(12, 8))
tree.plot_tree(
    clf,
    filled=True,
    feature_names=x.columns,
    class_names=play_encoder.categories_[0],
    rounded=True,
)
plt.title("Decision Tree (Gini)")
plt.show()

plt.figure(figsize=(12, 8))
tree.plot_tree(
    clf_entropy,
    filled=True,
    feature_names=x.columns,
    class_names=play_encoder.categories_[0],
    rounded=True,
)
plt.title("Decision Tree (Entropy)")
plt.show()

print("#" * 50)

import kagglehub

# Download latest version
path = kagglehub.dataset_download("mlg-ulb/creditcardfraud")

print("Path to dataset files:", path)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# %matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.model_selection import GridSearchCV

data = pd.read_csv(
    r"C:\Users\Muhammad Walid\.cache\kagglehub\datasets\mlg-ulb\creditcardfraud\versions\3\creditcard.csv"
)
print(data.head())

data = data.drop(["Time"], axis=1)
print(data.head())

rcParams["figure.figsize"] = 14, 8
plt.bar(data["Class"].unique(), data["Class"].value_counts(), color=["red", "green"])

rcParams["figure.figsize"] = 14, 8
plt.bar(data["Class"].unique(), data["Class"].value_counts(), color=["red", "green"])

plt.xticks([0, 1])
plt.xlabel("Class")
plt.ylabel("Frequency")
plt.title("Frequency of Classes")

x = data.drop(["Class"], axis=1)
y = data["Class"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

hyper_param = {"criterion": ["entropy"], "max_depth": [4]}
decision_tree_grid_param = GridSearchCV(
    estimator=DecisionTreeClassifier(random_state=42), param_grid=hyper_param, cv=5
)
decision_tree_cv = decision_tree_grid_param.fit(x_train, y_train)
print("Best Hyperparameters:", decision_tree_cv.best_params_)
print("Best Estimator:", decision_tree_cv.best_estimator_)
print("Best Score:", decision_tree_cv.best_score_)

print("#" * 30)

hyper_param = {"n_estimators": [3, 5, 10]}
bagging_grid_param = GridSearchCV(
    estimator=BaggingClassifier(), param_grid=hyper_param, scoring="roc_auc", cv=5
)
bagging_cv = bagging_grid_param.fit(x_train, y_train)
print("Best Hyperparameters:", bagging_cv.best_params_)
print("Best Estimator:", bagging_cv.best_estimator_)
print("Best Score:", bagging_cv.best_score_)

print("#" * 30)

hyper_param = {"n_estimators": [3, 5, 10]}
bagging_grid_param = GridSearchCV(
    estimator=RandomForestClassifier(), param_grid=hyper_param, scoring="roc_auc", cv=5
)
bagging_cv = bagging_grid_param.fit(x_train, y_train)
print("Best Hyperparameters:", bagging_cv.best_params_)
print("Best Estimator:", bagging_cv.best_estimator_)
print("Best Score:", bagging_cv.best_score_)

print("#" * 30)

hyper_param = {
    "criterion": ["entropy"],
    "max_depth": [4, 10, 20],
    "n_estimators": [50, 100],
    "max_features": ["sqrt"],
}
bagging_grid_param = GridSearchCV(
    estimator=RandomForestClassifier(), param_grid=hyper_param, scoring="roc_auc", cv=5
)
bagging_cv = bagging_grid_param.fit(x_train, y_train)
print("Best Hyperparameters:", bagging_cv.best_params_)
print("Best Estimator:", bagging_cv.best_estimator_)
print("Best Score:", bagging_cv.best_score_)

print("#" * 30)

plt.figure(figsize=(12, 8))
tree.plot_tree(
    clf_entropy,
    filled=True,
    feature_names=x.columns,
    class_names=play_encoder.categories_[0],
    rounded=True,
)
plt.title("Decision Tree (Entropy)")
plt.show()
