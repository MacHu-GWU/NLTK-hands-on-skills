##encoding=utf-8

"""
The nltk built-in naivebayes black box model api works this way:

Train
-----
[({"feature1": value1, "feature2": value2, ...}, label),
 ({"feature1": value1, "feature2": value2, ...}, label),
 ...,]
 
"""

from __future__ import print_function
from nltk.corpus import names
import nltk
import random


def gender_features(name):
#     return {"first_letter": name[0]}
#     return {"last_letter": name[-1]}
    return {"first_letter": name[0], "last_letter": name[-1]}

males = [(name, "male") for name in names.words("male.txt")]
females = [(name, "female") for name in names.words("female.txt")]
random.shuffle(males)
random.shuffle(females)

males_features = [(gender_features(tp[0]), tp[1]) for tp in males]
females_features = [(gender_features(tp[0]), tp[1]) for tp in females]

train_percentage = 0.9

train = males_features[int(len(males_features) * 0.9):] + females_features[int(len(females_features) * 0.9):]
test = males_features[int(len(males_features) * 0.9):] + females_features[int(len(females_features) * 0.9):]
test_raw = males[int(len(males) * 0.9):] + females[int(len(females) * 0.9):]

classifier = nltk.NaiveBayesClassifier.train(train)

counter = 0
for predict, actual, lastletter, name in zip([classifier.classify(i[0]) for i in test],
                           [j[1] for j in test_raw],
                           [k[0] for k in test],
                           [l[0] for l in test_raw]):
    print(predict, actual, lastletter, name)
    if predict == actual:
        counter += 1
print("correct rate = %.4f" % (counter*1.0/len(test),))

# nltk.download()