# DEPI AI & ML Round 4
# Machine Learning - Final Project
# --------------------------------
# Made With <3 By Muhammad Walid
# Start: March 10, 2026
#        March 12, 2026
# End:   March 13, 2026
# ------------------------------


# Import libraries necessary for this project
import numpy as np
import pandas as pd
import visuals as vs  # Supplementary code
from sklearn.model_selection import ShuffleSplit

# Pretty display for notebooks
# %matplotlib inline

data_path = r"C:\Users\Muhammad Walid\Python\DEPI\GIZ4_AIS2_S1_ML\GIZ4_AIS2_S1_ML\src\Machine Learning\final_project\p1\housing.csv"

# Load the Boston housing dataset
data = pd.read_csv(data_path)
print(data.head(5))

print("#" * 30)  # Separator

# Gathering all information about dataset
# ---------------------------------------


# data.info()
def display_all_data_info(data: pd.DataFrame):
    data_type = data.dtypes
    data_shape = data.shape
    data_statistics = data.describe()

    MEDV_col = data.iloc[:, -1]
    MEDV_statistics = MEDV_col.describe()
    MEDV_nulls_count = MEDV_col.isnull().sum()

    # Check Outliers in MEDV Column using IQR Technique
    MEDV_Q1 = MEDV_col.quantile(0.25)
    MEDV_Q3 = MEDV_col.quantile(0.75)
    MEDV_IQR = MEDV_Q3 - MEDV_Q1

    MEDV_lower_fence = MEDV_Q1 - 1.5 * MEDV_IQR
    MEDV_upper_fence = MEDV_Q3 + 1.5 * MEDV_IQR

    MEDV_lower_outliers = data[MEDV_col < MEDV_lower_fence].values
    MEDV_upper_outliers = data[MEDV_col > MEDV_upper_fence].values

    MEDV_lower_outliers_count = data[MEDV_col < MEDV_lower_fence].count(axis=1).sum()
    MEDV_upper_outliers_count = data[MEDV_col > MEDV_upper_fence].count(axis=1).sum()

    print(pd.DataFrame({"Data Type:": data_type}).T)
    print("#" * 30)
    print(
        f"Data Shape:\n{'=' * 11}",
        f"Number of Rows: {data_shape[0]}",
        f"Number of Columns: {data_shape[1]}",
        sep="\n",
    )
    print("#" * 30)
    print(f"Basic Statistics:\n{'=' * 17}\n{data_statistics}")

    print("#" * 30)
    print(f"MEDV (Prediction) Column Statistics:\n{'=' * 36}\n{MEDV_statistics}")
    print("#" * 30)
    print(f"MEDV (Prediction) Column Nulls Count:\n{'=' * 37}\n{MEDV_nulls_count}")
    print("#" * 30)
    print(f"MEDV (Prediction) Column Lower Fence: {MEDV_lower_fence}")
    print(
        f"MEDV (Prediction) Column Lower Outliers:\n{'=' * 37}\n{MEDV_lower_outliers}"
    )
    print(f"Number of Lower Outliers: {MEDV_lower_outliers_count}")
    print("#" * 30)
    print(f"MEDV (Prediction) Column Upper Fence: {MEDV_upper_fence}")
    print(
        f"MEDV (Prediction) Column Upper Outliers:\n{'=' * 37}\n{MEDV_upper_outliers}"
    )
    print(f"Number of Upper Outliers: {MEDV_upper_outliers_count}")


display_all_data_info(data)

print("#" * 30)

prices = data["MEDV"]
features = data.drop("MEDV", axis=1)
# print the shape of the data
print(
    "Boston housing dataset has {0} data points with {1} variables each.".format(
        *data.shape
    )
)

print("#" * 100)

# Data Exploration
# ----------------

# Minimum price of the data
minimum_price = prices.min()

# Maximum price of the data
maximum_price = prices.max()

# Mean price of the data
mean_price = prices.mean()

# Median price of the data
median_price = prices.median()

# Standard deviation of prices of the data
std_price = prices.std()

# Show the calculated statistics
print(f"Statistics for Boston housing dataset:\n{'=' * 38}")
print("Minimum price: ${:,.2f}".format(minimum_price))
print("Maximum price: ${:,.2f}".format(maximum_price))
print("Mean price: ${:,.2f}".format(mean_price))
print("Median price ${:,.2f}".format(median_price))
print("Standard deviation of prices: ${:,.2f}".format(std_price))

# print("#" * 30)

# Question 1 - Feature Observation:
# - 'RM' is the average number of rooms among homes in the neighborhood.
# - 'LSTAT' is the percentage of homeowners in the neighborhood considered "lower class" (working poor).
# - 'PTRATIO' is the ratio of students to teachers in primary and secondary schools in the neighborhood.
# Using your intuition, for each of the three features above, do you think that an increase in the value of that feature would lead to an **increase** in the value of `'MEDV'` or a **decrease** in the value of `'MEDV'`? Justify your answer for each.**

# My Short Answer (based on my critical thinking):
"""
By increasing in the value of:

'RM': DEFINITELY WILL INCREASE the prices of the houses (for example: if we have a house with 6 rooms will definitly worth more than one with 2 rooms)
'LSTAT': DEFINITELY WILL DECREASE the prices of the houses
'PTRATIO': WILL DECREASE the prices of the houses
"""

# And here is my detailed answer:
"""
By increasing in the value of:

'RM': As I mentioned, I believe that it would definitely increase the value of the price,
      and it is not necessary that it will be a 'direct relationship'
      (like if a house has 2 rooms will worth $200,000 that doesn't mean that if a house has 4 rooms will worth $400,000) => NOT NECESSARY
      so may be if a house has 4 rooms (it will worth $600,000 for example not $400,000) => it was never a 'direct relationship' in anywhere in this world

'LSTAT': Unfortunately, in our world we judge the book by its cover
         even if we didn't want to (it is just something with our Subconscious mind)
         so if we know that the homeowners of a neighborhood are from the poor
         => we will subconsciously believe that whomever lives in that neighborhood is also a poor guy
         => and we would prefer to live in another neighborhood if we had the option to
         that neighborhood will become unattractive and the prices of the houses there will definitely decrease,
         even if the houses themselves are great

'PTRATIO': Like I said, it will decrease the prices of the houses,
           as normal number of students for one teacher often indicates a good school
           while too many students for one teacher is often an indicator for worse schools
           so 'crowded schools' will definitely decrease the prices of the neighborhood's houses
"""

print("#" * 100)

# Developing a Model
# ------------------

# Import 'r2_score'
from sklearn.metrics import r2_score


def performance_metric(y_test, y_predict):
    """
    Calculates and returns the performance score between
    test and predicted values based on the metric chosen.
    """

    # Calculate the performance score between 'y_test' and 'y_predict'
    score = r2_score(y_test, y_predict)

    # Return the score
    return score


# Calculate the performance of this model
score = performance_metric([3, -0.5, 2, 7, 4.2], [2.5, 0.0, 2.1, 7.8, 5.3])
print(
    "Model has a coefficient of determination, R^2, of {:.3f}.".format(score)
)  # r2_score = 0.923

# Question 2 - Goodness of Fit:
# Would you consider this model to have successfully captured the variation of the target variable?

# My Answer:
"""
Yes, the model can capture the variation of the target variable with very accuracy.
as the r2_score for this model is 0.923 which is very high, since the max range of the r2_score is 1
so this means that 92.3% of the variance in Y (dependent variable 'target') is predictable from X (independent variable)
in other words, the dependent variable Y can be predicted from independent variable X with a small error (small inaccuracy)
"""

print("#" * 30)

# Import 'train_test_split'
from sklearn.model_selection import train_test_split

# Shuffle and split the data into training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(
    features, prices, test_size=0.2, random_state=1
)

# Success
print("Training and testing split was successful.")

# Question 3 - Training and Testing:
# What is the benefit to splitting a dataset into some ratio of training and testing subsets for a learning algorithm?

# My Answer:
"""
Let me explain it with an example:

lets think that we give all our data to the model to train on it, now it is 'overfitted'
what does that mean?
=> it means now your model knows exactly the data you give it to him but doesn't understands it
=> which means if you just made a small change in your data, your model will be absolutely useless
=> also if you tried to give your model another data, again your model will be absolutely useless

on the other hand, if we splitted our data, like train on => 80% of the data, and test on the others (20% of the data)
=> your model will be 'smart', it now understands the data
=> although it doesn't give perfect prediction like the 'overfit model' but it has some 'flexability'
=> which I mean, if you made changes in your data or gave your model another data
=> your model will be absolutely usefull, it can adapt with changes,
=> and also it can work with different data; while maintaining accuracy
"""

print("#" * 100)

# Analyzing Model Performance
# ---------------------------

import warnings
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import learning_curve, ShuffleSplit, train_test_split
from sklearn.tree import DecisionTreeRegressor

# Suppress matplotlib user warnings
warnings.filterwarnings("ignore", category=UserWarning, module="matplotlib")

# Display inline matplotlib plots with IPython
from IPython import get_ipython

# get_ipython().run_line_magic('matplotlib', 'inline')
ip = get_ipython()
if ip is not None:
    ip.run_line_magic("matplotlib", "inline")


def ModelLearning(X, y):
    """Calculates the performance of several models with varying sizes of training data.
    The learning and testing scores for each model are then plotted."""

    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

    # Generate the training set sizes increasing by 50
    train_sizes = np.rint(np.linspace(1, X.shape[0] * 0.8 - 1, 9)).astype(int)

    # Create the figure window
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))

    # Create four different models based on max_depth
    for k, depth in enumerate([1, 3, 6, 10]):
        # Create a Decision tree regressor at max_depth = depth
        regressor = DecisionTreeRegressor(max_depth=depth)

        # Calculate the training and testing scores
        sizes, train_scores, test_scores = learning_curve(
            regressor, X, y, cv=cv, train_sizes=train_sizes, scoring="r2"
        )

        # Find the mean and standard deviation for smoothing
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)

        # Subplot the learning curve
        ax = axes[k // 2, k % 2]
        ax.plot(sizes, train_mean, "o-", color="r", label="Training Score")
        ax.plot(sizes, test_mean, "o-", color="g", label="Testing Score")
        ax.fill_between(
            sizes, train_mean - train_std, train_mean + train_std, alpha=0.15, color="r"
        )
        ax.fill_between(
            sizes, test_mean - test_std, test_mean + test_std, alpha=0.15, color="g"
        )

        # Labels
        ax.set_title(f"max_depth = {depth}")
        ax.set_xlabel("Number of Training Points")
        ax.set_ylabel("Score")
        ax.set_xlim([0, X.shape[0] * 0.8])
        ax.set_ylim([-0.05, 1.05])
        ax.legend(loc="lower right")

    # Visual aesthetics
    fig.suptitle("Decision Tree Regressor Learning Performances", fontsize=16, y=1.03)
    fig.tight_layout()
    # plt.show()


# Produce learning curves for varying training set sizes and maximum depths
ModelLearning(features, prices)

# Question 4 - Learning the Data:
# * Choose one of the graphs above and state the maximum depth for the model.
# * What happens to the score of the training curve as more training points are added? What about the testing curve?
# * Would having more training points benefit the model?

# My Answer:
"""
The The Second Graph or the graph with 'max_depth = 3'
=> by adding more 'training points' => 'score' becomes around 0.8 (80%) which is good btw
=> and it is not also about the score, it is about that the model can understands the data in this graph more than any other graphs
=> the 'training curve' and the 'testing curve' are close to each other which empathize what I just said about that the model can understands the data

By increasing the number of the training points => it will reduce overfitting
=> More data helps the model to generalize better (understand data better)
"""

# vs.ModelComplexity(X_train, y_train)  # Complexity Curves
# print(dir(vs))


def ModelComplexity(X, y):
    """Calculates the performance of the model as model complexity increases.
    The learning and testing errors rates are then plotted."""

    # Create 10 cross-validation sets for training and testing
    cv = ShuffleSplit(n_splits=10, test_size=0.2, random_state=0)

    # Vary the model complexity by adjusting max_depth from 1 to 10
    max_depth = np.arange(1, 11)

    # Calculate the training and testing scores
    train_scores, test_scores = [], []
    for d in max_depth:
        regressor = DecisionTreeRegressor(max_depth=d)
        sizes, train_s, test_s = learning_curve(
            regressor, X, y, cv=cv, train_sizes=[0.8], scoring="r2"
        )
        train_scores.append(np.mean(train_s))
        test_scores.append(np.mean(test_s))

    # Plot the complexity curve
    plt.figure(figsize=(7, 5))
    plt.plot(max_depth, train_scores, "o-", color="r", label="Training Score")
    plt.plot(max_depth, test_scores, "o-", color="g", label="Testing Score")
    plt.title("Decision Tree Regressor Complexity Performance")
    plt.xlabel("Maximum Depth")
    plt.ylabel("Score")
    plt.xticks(max_depth)
    plt.xlim([1, 10])
    plt.ylim([-0.05, 1.05])
    plt.legend(loc="lower right")
    plt.tight_layout()
    plt.show()


ModelComplexity(X_train, y_train)  # Complexity Curves

# Question 5 - Bias-Variance Tradeoff:
# * When the model is trained with a maximum depth of 1, does the model suffer from high bias or from high variance?
# * How about when the model is trained with a maximum depth of 10? What visual cues in the graph justify your conclusions?

# My Answer:
"""
when max_depth = 1, the model will suffer from HIGH BIAS, it will become UNDERFIT MODEL
so the best that this model can do is calculate the mean (average) of the data

when max_depth = 10, the model will suffer from HIGH VARIANCE, it will become OVERFIT MODEL
so this model will MEMORIZE THE DATA WITHOUT UNDERSTANDING
"""

# Question 6 - Best-Guess Optimal Model:
# * Which maximum depth do you think results in a model that best generalizes to unseen data?
# * What intuition lead you to this answer?

# My Answer:
"""
Best generalize to unseen data is when model has max_depth = 3 or 4 (if found)
=> by adding more 'training points' => 'score' becomes around 0.8 (80%) which is good btw
=> and it is not also about the score, it is about that the model can understands the data in this graph more than any other graphs
=> the 'training curve' and the 'testing curve' are close to each other which empathize what I just said about that the model can understands the data
"""

print("#" * 100)

# Evaluating Model Performance
# ----------------------------

# Question 7 - Cross-Validation:
# * What is the k-fold cross-validation training technique?
# * What benefit does this technique provide for grid search when optimizing a model?

# My Answer:
"""
cross-validation: means that we try to split the data multiple times to get a reliable score
k-fold cross-validation: means that we do the same in "k-times"

And with grid search: we are trying to find the best hyperparameters (like best max_depth)

so if we combine both of them (grid search + cross-validation):
=> means that we try to split the data multiple times with different max_depth
=> till we find the 'best max_depth'
"""

# Import 'make_scorer', 'DecisionTreeRegressor', and 'GridSearchCV'
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import make_scorer
from sklearn.model_selection import GridSearchCV


def fit_model(X, y):
    """Performs grid search over the 'max_depth' parameter for a
    decision tree regressor trained on the input data [X, y]."""

    # Create cross-validation sets from the training data
    cv_sets = ShuffleSplit(X.shape[0], test_size=0.20, random_state=0)

    # Create a decision tree regressor object
    regressor = DecisionTreeRegressor()

    # Create a dictionary for the parameter 'max_depth' with a range from 1 to 10
    params = {"max_depth": list(range(1, 11))}

    # Transform 'performance_metric' into a scoring function using 'make_scorer'
    scoring_fnc = make_scorer(performance_metric)

    # Create the grid search object
    grid = GridSearchCV(regressor, params, scoring=scoring_fnc, cv=cv_sets)

    # Fit the grid search object to the data to compute the optimal model
    grid = grid.fit(X, y)

    # Return the optimal model after fitting the data
    return grid.best_estimator_


print("Best model parameters:", fit_model(X_train, y_train))

print("#" * 30)

# Question 9 - Optimal Model:
# * What maximum depth does the optimal model have? How does this result compare to your guess in **Question 6**?

# My Answer:
"""
Best generalize to unseen data is when model has max_depth = 4
=> it is very close to my guess in Question 6, as I said that the best max_depth is 3 or 4 (if found)
"""

# Fit the training data to the model using grid search
reg = fit_model(X_train, y_train)

# Produce the value for 'max_depth'
print(
    "Parameter 'max_depth' is {} for the optimal model.".format(
        reg.get_params()["max_depth"]
    )
)

print("#" * 30)

# Question 10 - Predicting Selling Prices:
# * What price would you recommend each client sell his/her home at?
# * Do these prices seem reasonable given the values for the respective features?

# My Answer:
"""
For Client 3, I would recommend the highest price as this client we can say 'the perfect one'
=> Largest House (8 Rooms), Lowest Poor Owners (7 Owners), Best Student-to-Teacher ratio (each teacher has 12 students)
=> so I would recommend $1,000,000.00

For Client 2, I would always recommend the lowest price ever as this client we can say 'the worst one'
=> Smallest House (4 Rooms), Highest Poor Owners (55 Owners), Worst Student-to-Teacher ratio (each teacher has 22 students)
=> so I would recommend $100,000.00

For Client 1, I would recommend the best price (average price) as this client we can say 'the normal one'
=> Average House (5 Rooms), High Poor Owners (34 Owners), Normal Student-to-Teacher ratio (each teacher has 15 students)
=> so I would recommend $450,000.00
"""

print("#" * 30)

# Produce a matrix for client data
client_data = [[5, 34, 15], [4, 55, 22], [8, 7, 12]]  # Client 1  # Client 2  # Client 3

# Show predictions
for i, price in enumerate(reg.predict(client_data)):
    print("Predicted selling price for Client {}'s home: ${:,.2f}".format(i + 1, price))

"""
Predicted selling price for Client 1's home: $411,417.39
Predicted selling price for Client 2's home: $230,828.57
Predicted selling price for Client 3's home: $937,230.00
"""

# My Predictions:
# ---------------
# Predicted selling price for Client 1's home: $450,000.00
# Predicted selling price for Client 2's home: $100,000.00
# Predicted selling price for Client 3's home: $1,000,000.00
