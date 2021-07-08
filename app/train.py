from sklearn import datasets
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle


iris = datasets.load_iris()
X = iris.data
y = iris.target

print(iris.feature_names)
print(iris.target_names)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

pipe = Pipeline(steps=[
    ('scaler', StandardScaler()),
    ('estimator', LogisticRegression(random_state=42))
])

pipe.fit(X_train, y_train)
y_pred = pipe.predict(X_test)
y_pred_proba = pipe.predict_proba(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc)
# print(y_pred_proba)

with open('./iris_v1.pkl', 'wb') as f:
    pickle.dump(pipe, f)