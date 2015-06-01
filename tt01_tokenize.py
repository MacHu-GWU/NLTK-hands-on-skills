##encoding=utf-8

"""
This module is to teach you the basic use of wordsegmentation/tokenize (句子分词)

What is tokenize?
    tokenize is to split sentence into word tokens and punctuations. 
    For example: I like obama. => ["I", "like", "obama", "."]
"""

from __future__ import print_function
from pprint import pprint
import nltk

def tokenize_example():
    r"""
    [EN]Usually the first step of natural language analysis is split sentence into word token.
    To do this you need run nltk.download() and download:
        tokenizers/punkt/english.pickle using NLTK downloader => Model => punkt
        
    [CN]自然语言分析的第一步就是句子分词(将句子拆分成有独立语义的单词)
    nltk.word_tokenize(text)是内置的方法。若要对英文进行分词则需要下载:
        tokenizers/punkt/english.pickle 下载方法: NLTK downloader => Model => punkt
    下载后的文件会被储存在中:
        C:\Users\username\AppData\Roaming\nltk_data\tokenizers
    """
    
    sentence = """At eight o'clock on Thursday morning ... Arthur didn't feel very good."""
    tokens = nltk.word_tokenize(sentence)
    pprint(tokens)
    
tokenize_example()

# nltk.download()