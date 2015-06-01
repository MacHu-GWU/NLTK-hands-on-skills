##encoding=utf-8

"""
This module is to teach you how to use nltk to do word stemming (词干抽取)

What is word stemming:
    word stemming is to normalize word in different forms to a standard one.
    for example: information, informed => inform

Documentation: http://www.nltk.org/api/nltk.stem.html#nltk-stem-package

Reference:
    NTLK with python book: Charpter 3.6 Normalizing Text
    Wiki: http://en.wikipedia.org/wiki/Stemming
"""

from __future__ import print_function
from pprint import pprint
import nltk
from nltk.stem.lancaster import LancasterStemmer # nltk.stem.lancaster module
from nltk.stem.porter import PorterStemmer # nltk.stem.porter module
from nltk.stem import RegexpStemmer # 正则分词算法 nltk.stem.regexp module
from nltk.stem import SnowballStemmer # 多语言支持分词算法 nltk.stem.snowball module

def word_stem_example(word="Amevive"):
    """
    [EN]Read: http://www.nltk.org/book/ch03.html, 3.6 Normalizing Text
    [CN]根据NLTK in python书中的推荐Porter算法较为鲁棒, 推荐使用
    """
    stemmer = LancasterStemmer()
    print("Lancaster [%s => %s]" % (word, stemmer.stem(word)))
    
    stemmer = PorterStemmer() # <=== recommended algorithm
    print("Porter [%s => %s]" % (word, stemmer.stem(word)))
    
    stemmer = RegexpStemmer('ing$|s$|e$', min=4)
    print("Regexp [%s => %s]" % (word, stemmer.stem(word)))
    
    stemmer = SnowballStemmer('english') # Choose a language
    print("Snowball [%s => %s]" % (word, stemmer.stem(word)))

word_stem_example("Amevive")
word_stem_example("lying")
word_stem_example("greater")
word_stem_example("information")
