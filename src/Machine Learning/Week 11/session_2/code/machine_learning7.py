import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn import tree

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

x = data.drop(["Class"], axis=1)
y = data["Class"]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

from sklearn.ensemble import GradientBoostingClassifier

# Gradient Boosting <=> GB
gbm_param = {
    "n_estimators": [10, 50, 100, 200],  # عدد الشجر
    "learning_rate": [0.01, 0.1],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9],
    "min_samples_split": [2, 5, 10],
}

gbm_param_grid_search = GridSearchCV(
    GradientBoostingClassifier(),
    gbm_param,
    scoring="roc_auc",
    cv=5,
    n_jobs=-1,
    verbose=2,
)
gbm_cv = gbm_param_grid_search.fit(x_train, y_train)

# print(gbm_cv)
# print("#" * 30)
# print("Best parameters found: ", gbm_param_grid_search.best_params_)
# print("Best AUC score: ", gbm_param_grid_search.best_score_)

print("The best paramter combination is ")
# print(gbm_cv.best_params_)  #gets best estimator

# Prediction Using the Model
y_pred_gbm = gbm_cv.best_estimator_.predict(x_test)
cm_gbm = confusion_matrix(y_test, y_pred_gbm)
# print(cm_gbm)
# print(classification_report(y_test, y_pred_gbm, target_names=["Safe", "Fraud"]))

# Calculate sensitivity, specificity, and accuracy
total_gbm = sum(sum(cm_gbm))
accuracy_gbm = (cm_gbm[0, 0] + cm_gbm[1, 1]) / total_gbm
# print('Accuracy (GBM): ', accuracy_gbm)

sensitivity_gbm = cm_gbm[0, 0] / (cm_gbm[0, 0] + cm_gbm[0, 1])
# print('Sensitivity (GBM): ', sensitivity_gbm)

specificity_gbm = cm_gbm[1, 1] / (cm_gbm[1, 0] + cm_gbm[1, 1])
# print('Specificity (GBM): ', specificity_gbm)
##
from xgboost import XGBClassifier

gbm_param = {
    "n_estimators": [10, 50, 100, 200],  # عدد الشجر
    "learning_rate": [0.01, 0.1],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9],
    "min_samples_split": [2, 5, 10],
    "colsample_bytree": [0.8, 1.0],
}
##
from lightgbm import LGBMClassifier

gbm_param = {
    "n_estimators": [10, 50, 100, 200],  # عدد الشجر
    "learning_rate": [0.01, 0.1],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9],
}
##
from catboost import CatBoostClassifier

gbm_param = {
    "n_estimators": [10, 50, 100, 200],  # عدد الشجر
    "learning_rate": [0.01, 0.1],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9],
}
##
from sklearn.ensemble import AdaBoostClassifier

gbm_param = {
    "n_estimators": [10, 50, 100, 200],  # عدد الشجر
    "learning_rate": [0.01, 0.1],
    "max_depth": [3, 4, 5, 6],
    "subsample": [0.7, 0.8, 0.9],
}
##

from imblearn.over_sampling import SMOTE, RandomOverSampler
from typing import Counter

ros = RandomOverSampler(random_state=50)
x_ros, y_ros = ros.fit_resample(x_train, y_train)

print("Original Dataset Shape", Counter(y))
print("Resampled Dataset Shape", Counter(y_ros))
