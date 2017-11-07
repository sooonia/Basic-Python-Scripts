import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import classification_report,confusion_matrix

df = pd.read_csv("C:/Python Projects/breast-cancer-wisconsin-data/data.csv")
df["diagnosis"] = df["diagnosis"].astype('category')
df["diagnosis"] = df["diagnosis"].cat.codes

df["diagnosis"] = df["diagnosis"].astype('category')
df["diagnosis"] = df["diagnosis"].cat.codes
X= df.drop(['diagnosis', 'id', 'Unnamed: 32'], 1)

plt.scatter(X[['perimeter_worst']],X[['perimeter_mean']], s=1 )
plt.xlabel("perimeter_worst")
plt.ylabel("perimeter_mean")
plt.show()

predVars = ['perimeter_mean', 'radius_worst', 'texture_worst',
'perimeter_worst', 'area_worst',
'smoothness_worst', 'compactness_worst',
'concavity_worst', 'concave points_worst',
'symmetry_worst', 'fractal_dimension_worst']
X= X[predVars]
corr = X.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)
plt.xticks(rotation=30)
plt.yticks(rotation=0)
plt.show()
#print("Predictor Variables:\n",list(X))
#print("\nSummary: ",X.describe())
#X = np.array(X)
y=  df['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.2)
scaler= StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

mlp = MLPClassifier(hidden_layer_sizes=(10,10,10),activation="relu", max_iter= 300)
mlp.fit(X_train,y_train)
preds_test = mlp.predict(X_test)
preds_train = mlp.predict(X_train)

print("\nNeural Net Train set:\n",confusion_matrix(y_train,preds_train))
print("\nNeural Net Test set:\n",confusion_matrix(y_test,preds_test))

model = neighbors.KNeighborsClassifier()
model.fit(X_train, y= y_train)
preds_n_test = model.predict(X_test)
preds_n_train = model.predict(X_train)
print("\nNearest Neighbors Train set:\n",confusion_matrix(y_train,preds_n_train))
print("\nNearest Neighbors Test set:\n",confusion_matrix(y_test,preds_n_test))