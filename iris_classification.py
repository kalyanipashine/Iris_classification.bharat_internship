# -*- coding: utf-8 -*-
"""Iris_classification.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TfZBzdx-S_k8eizK68RFEYHVYYXOuAhK
"""

import sklearn
import numpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

#load the csv data
df= pd.read_csv('Iris.csv')
df.head()

#deleting the id column
df= df.drop(columns= ['ID'])
df.head()

#display basic stats of data
df.describe()

df.info()

#display no of samples on each class
df['Species'].value_counts()

#preprocessing the dataset
df.isnull().sum()

#data analysis
df['Sepal.Length'].hist()

df['Sepal.Width'].hist()

df['Petal.Length'].hist()

df['Petal.Width'].hist()

#cerate list of colors and class labels
colors=['red','orange','blue']
species= ['virginica','vesicolor','setosa']

for i in range(3):
  #filter data on each class
  x= df[df['Species']== species[i]]
  #plot the scatter plot
  plt.scatter(x['Sepal.Length'], x['Sepal.Width'], c= colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.legend()

for i in range(3):
  #filter data on each class
  x= df[df['Species']== species[i]]
  #plot the scatter plot
  plt.scatter(x['Petal.Length'], x['Petal.Width'], c= colors[i], label=species[i])
plt.xlabel("Petal Length")
plt.ylabel("Petal Width")
plt.legend()

for i in range(3):
  #filter data on each class
  x= df[df['Species']== species[i]]
  #plot the scatter plot
  plt.scatter(x['Sepal.Length'], x['Petal.Length'], c= colors[i], label=species[i])
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.legend()

for i in range(3):
  #filter data on each class
  x= df[df['Species']== species[i]]
  #plot the scatter plot
  plt.scatter(x['Sepal.Width'], x['Petal.Width'], c= colors[i], label=species[i])
plt.xlabel("Seapl Width")
plt.ylabel("Petal Width")
plt.legend()

#correlation matrix
df.corr()

corr= df.corr()
#plot the heat map
fig, ax= plt.subplots(figsize=(5,4))
sns.heatmap(corr, annot=True, ax=ax, cmap='coolwarm')

#model training & testing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
import pickle

#input data
X= df.drop(columns=['Species'])
#output data
Y= df['Species']
#split the data for train and test
X_train, X_test, Y_train, Y_test= train_test_split(X,Y, test_size=0.30)

#Logistic Regression
model= LogisticRegression()
model.fit(X_train, Y_train)
print("Logistic Regression Accuracy: ", model.score(X_test, Y_test) *100)

#model training
model.fit(X_train.values, Y_train.values)

#print metric to get performance
print("Accuracy: ", model.score(X_test, Y_test)*100)

#k-nearest neighbors
model= KNeighborsClassifier()
model.fit(X_train.values, Y_train.values)
print("K-nearest neighbors Accuracy: ", model.score(X_test, Y_test)*100)

model.fit(X_train.values, Y_train.values)

#print metric to get performance
print("Accuracy: ", model.score(X_test, Y_test)*100)

#decision tree
model= DecisionTreeClassifier()
model.fit(X_train.values, Y_train.values)
print("Decision Tree Accuracy: ", model.score(X_test, Y_test)*100)

model.fit(X_train.values, Y_train.values)

#print metric to get performance
print("Acuuracy: ",model.score(X_test, Y_test)*100)

#save the model
import pickle
filename='saved_model.sav'
try:
  with open(filename,'wb') as file:
    pickle.dump(model, file)
    print("Model saved successfully.")
except Exception as e:
  print(f"Error saving the model: {e}")

load_model= pickle.load(open(filename, 'rb'))

load_model.predict([[6.0, 2.2, 4.0, 1.0]])

