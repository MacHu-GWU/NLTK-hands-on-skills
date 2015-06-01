##encoding=utf-8

"""
What is sentence segmentation:
    Divide a large text into sentences, this is sentence segmentation.
    
Reference:
    NLTK in python book, 3.8 Segmentation, Sentence Segmentation, http://www.nltk.org/book/ch03.html  
"""

from __future__ import print_function
from pprint import pprint
from nltk.tokenize import sent_tokenize
import nltk

def sentence_segmentation_example(text, language="english"):
    pprint(sent_tokenize(text))

# 此段有3句话
# 第1句中, 人名中的点没有被判定为句号
# 第3句中, 句子不以大写字母开头
text1 = \
"""
Punkt knows that the periods in Mr. Smith and Johann S. 
Bach do not mark sentence boundaries.
And sometimes sentences can start with non-capitalized words. 
i is a good variable name.
"""
text2 = \
"""
This tokenizer divides a text into a list of sentences by using an 
unsupervised algorithm to build a model for abbreviation words, 
collocations, and words that start sentences. It must be trained on 
a large collection of plaintext in the target language before it can be used.
"""
sentence_segmentation_example(text1)
sentence_segmentation_example(text2)