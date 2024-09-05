from sklearn.datasets import load_iris 
import pandas as pd 
iris = load_iris() 
data = pd.DataFrame(data=iris.data, columns=iris.feature_names) 
datal species' = iris.target

data.shape
data.info()

# Statistical summary 
data.describe()

# Breakdown by class 
data['species'].value_counts()

# Univariate Plots
import seaborn as sns 
import matplotlib.pyplot as plt

#Boxplot 
data.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)
plt.show()

# Histogram 
data.hist() 
plt.show()

# Multivariate Plots

#Pairplot 
sns.pairplot(data, hue='species') 
plt.show()

from sklearn.model_ selection import train_test_split 
from sklearn.model_ selection import cross_yal_score, StratifiedKFold 
from sklearn.linear_model import LogisticRegression 
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis 
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.tree import DecisionTreeClassifier 
from sklearn.naive_bayes import GaussianNB 
from sklearn.svm import SVC

 # Split dataset into training and validation sets 
X = data.drop(columns=['species']) 
y = data['species'] 
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state)
 # Set-Up the Test Harness Using 10-Fold Cross-Validation 
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)
 # List of models to evaluate 
models = [] 
models.append(('LR', LogisticRegression(max_iter=500)))  #Increased max_iter
models.append(('LDA', LinearDiscriminantAnalysis())) 
models.append(('KNN', KNeighborsClassifier())) 
models.append(('CART', DecisionTreeClassifier())) 
models.append(('NB GaussianNB())) 
models.append(('SVM', SVC()))

# Evaluate each model 
results = []
names = [] 
for name, model in models: 
    cv_results = cross_val_score(model, X_train, y_train, cv=kfold, scoring='a 
    results.append(cv_results) 
    names.append(name) 
    print(f"(name): fcv_results.mean():.3f) (fcv_results.std():.3f))")

# Predictions

# Train the best model 
model = LinearDiscriminantAnalysis() 
model.fit(X_train, y_train)

# Make predictions on the validation set
predictions model.predict(X_val)

 # Evaluate predictions 
from sklearn.metrics import accuracy_score, classification_report
print(accuracy_score(y_val, predictions)) 
print(classification_report(y_val, predictions))
 