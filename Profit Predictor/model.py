#model creation
#import library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from pickle import dump

#load the data
data = pd.read_csv("company_data_march24.csv")
print(data)
print(data.head())
print(data.tail())

#features and target
features = data[["R&D Spend", "Administration", "Marketing Spend"]]
target = data["Profit"]

#train and test
x_train, x_test, y_train, y_test = train_test_split(features.values, target)

#model
model = LinearRegression()
model.fit(x_train, y_train)

# Save the model to a file
with open("company.pkl", "wb") as f:
    dump(model, f)

print("Model created")




