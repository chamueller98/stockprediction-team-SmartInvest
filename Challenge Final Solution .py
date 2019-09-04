import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor


# Loading Boston DataSet
boston_dataset = load_boston()

# Creating dataframe using pandas
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston['MEDV'] = boston_dataset.target

# Checking if data-cleaning is required
#print(boston.isnull().sum())

# Correlation matrix
# compute the pair wise correlation for all columns  
correlation_matrix = boston.corr().round(2)
sns.heatmap(data=correlation_matrix, annot=True)

# Strongest correlations with LSTAT, RM & PTRATIO (adding any more variables did not result in a lower MSE)

plt.figure(figsize=(20, 5))

features = ['LSTAT', 'RM', 'PTRATIO']
target = boston['MEDV']

for i, col in enumerate(features):
    plt.subplot(1, len(features) , i+1)
    x = boston[col]
    y = target
    plt.scatter(x, y, marker='o')
    plt.title(col)
    plt.xlabel(col)
    plt.ylabel('MEDV')


# **Prepare the data for training**


X = pd.DataFrame(np.c_[boston['LSTAT'], boston['RM'], boston['PTRATIO']], columns = ['LSTAT','RM', 'PTRATIO'])
Y = boston['MEDV']


# **Split the data into training and testing sets**

# splits the training and test data set in 80% : 20%
# assign random_state to any value.This ensures consistency.
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=3)

# **Train the model using sklearn LinearRegression**
lin_model = LinearRegression()
lin_model.fit(X_train, Y_train)

# model evaluation for testing set
y_test_predict = lin_model.predict(X_test)

# root mean square error of the model
mse = (mean_squared_error(Y_test, y_test_predict))
print("The model performance for testing set with Linear Regression is {}".format((mse)))

# plotting the y_test vs y_pred
# ideally should have been a straight line
plt.scatter(Y_test, y_test_predict)
plt.show()

modelRF = RandomForestRegressor(random_state=23, n_estimators=610, criterion="mse")
modelRF.fit(X_train, Y_train)
predictionsRF = modelRF.predict(X_test)
print("The model performance for testing set with Random Forest Regressor is:", mean_squared_error(Y_test, predictionsRF))