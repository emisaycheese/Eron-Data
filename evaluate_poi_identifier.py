#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn import cross_validation 
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features,labels,test_size=0.3,random_state=42)

from sklearn.tree import DecisionTreeClassifier
clf=DecisionTreeClassifier()
clf.fit(features,labels)
#overfitting
print clf.score(features,labels) 



clf=DecisionTreeClassifier()
clf.fit(features_train,labels_train)
#pred=clf.predict(features_test)
print clf.score(features_test,labels_test)
print sum(labels_test)
print labels_test
pred=clf.predict(features_test)
print pred
new=[]
for i in range(0,28):
    if labels_test[i] == pred[i]:
        new.append(pred[i])

#print new
from sklearn.metrics import precision_score
print precision_score(labels_test, pred)

from sklearn.metrics import recall_score
print recall_score(labels_test, pred)

predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
truelb = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]

tst=[]
for i in range(0,len(truelb)):
    if predictions[i] <> truelb[i]:
        tst.append(predictions
                   [i])

print len(tst)-3


from sklearn.metrics import precision_score
print precision_score(truelb, predictions)

from sklearn.metrics import recall_score
print recall_score(truelb, predictions)
























