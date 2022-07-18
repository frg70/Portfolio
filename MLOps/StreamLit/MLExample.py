import streamlit as st
from sklearn import datasets
import numpy as np 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title('Simple Machine Learning Model Deployment')

st.write('''
## **Explore different classifiers**
Which one is the best? 
''')

dataset_name = st.sidebar.selectbox('Select a Dataset', ('Iris', 'Breast Cancer', 'Wine dataset'))
st.write(dataset_name)
classifier_name = st.sidebar.selectbox('Select Classifier', ('KNN', 'SVM', 'Random Forest'))
st.write(classifier_name)

def get_dataset(dataset_name):
    if dataset_name == 'Iris':
        data = datasets.load_iris()
    elif dataset_name == 'Breast Cancer':
        data = datasets.load_breast_cancer()
    elif dataset_name == 'Wine dataset':
        data = datasets.load_wine()
    X = data.data
    y = data.target
    return X, y
X, y = get_dataset(dataset_name)
st.write('Shape of the dataset', X.shape)
st.write('Number of classes', len(np.unique(y)))
 
def add_parameter_ui(clf_name):
    params = dict()
    if clf_name == 'KNN':
        K = st.sidebar.slider('K', 1, 15)
        params['K'] = K 
    elif clf_name == 'SVM':
        C = st.sidebar.slider('C', 0.01, 10.0)
        params['C'] = C
    else:
        max_depth = st.sidebar.slider('max_depth', 2, 300)
        n_estimators = st.sidebar.slider('Number of estimators', 1, 100)
        params['max_depth'] = max_depth
        params['n_estimators'] = n_estimators
    return params
params = add_parameter_ui(classifier_name)

def get_classifier(clf_name, params):
    if clf_name == 'KNN':
        clf = KNeighborsClassifier(n_neighbors=params['K'])
    elif clf_name == 'SVM':
        clf = SVC(C= params['C']) 
    else:
        clf = RandomForestClassifier(n_estimators=params['n_estimators'], max_depth= params['max_depth'], random_state=1)
    return clf 
clf = get_classifier(classifier_name,params)

#Classificaction 
test_size = st.sidebar.slider('Test size', 0.05, 0.4)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= test_size, random_state= 1)

clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
acc = metrics.accuracy_score(y_test, y_pred)
st.write(f'''Classifier = {classifier_name}''')
st.write(f'''**Acuraccy = {acc}**''')

# PLOT THE DATA
pca = PCA(2)
X_projected = pca.fit_transform(X)


x1 = X_projected[:,0]
x2 = X_projected[:,1]
fig = plt.figure()
plt.scatter(x1, x2, c= y, alpha = 0.85, cmap = 'viridis')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.colorbar()

st.pyplot()



