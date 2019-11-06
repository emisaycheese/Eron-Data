#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print len(enron_data)
b= enron_data["SKILLING JEFFREY K"]
print b
print len(b)
#find 
count=0
for key in enron_data.keys():
    if enron_data[key]["salary"]!='NaN':
        count=count+1
        print(key)
#print count


count=0
for key in enron_data.keys():
    if enron_data[key]["email_address"]!='NaN':
        count=count+1
        print(key)
print count



#find number of poi in the text file
text_file = open("/Users/ruiqianyang/Desktop/Intro to Machine Learning/ud120-projects-master/final_project/poi_names.txt", "r")
list1 = text_file.readlines()[2:]
list2=[]
for item in list1:
    number=0
    list2.append(str(item))
    number = number + 1
print len(list2)

c=enron_data["PRENTICE JAMES"]
print c
d=enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print d















