import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from sklearn.model_selection import cross_val_score, train_test_split
import warnings
from joblib import dump, load
from sklearn import preprocessing
warnings.filterwarnings("ignore")
from sklearn.svm import SVC

df = pd.read_csv('Data/Training.csv')
X = df.iloc[:, :-1]
y = df['prognosis']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=20)
try:
    rf_clf=load('model.joblib')
except:
    rf_clf = SVC()
    rf_clf.fit(X_train, y_train)
    dump(rf_clf, 'model.joblib')

scores = cross_val_score(rf_clf, X_test, y_test, cv=3)
print (scores.mean())
symptoms_dict = {symptom: index for index, symptom in enumerate(X)}



def getNext(symptoms):
    condition = (df[symptoms] == 1).all(axis=1)
    a=df.iloc[:,:-1].where(condition).dropna()
    j=a.loc[:, (a != 0).any(axis=0)]
    nonzero_counts = (j != 0).sum()
    new_df = pd.DataFrame({'Column': nonzero_counts.index, 'Non-Zero Count': nonzero_counts.values})
    new_df=new_df.sort_values('Non-Zero Count', ascending=False)
    next_ = [i for i in list(new_df['Column']) if i not in symptoms][0].replace('_',' ')
    return next_ 

def predict(symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in symptoms:
        input_vector[[symptoms_dict[item['symptom'].replace(' ','_')]]] = item['value']
    return str(rf_clf.predict([input_vector])[0])