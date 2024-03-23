#If "Python" is a keyword in Python

import keyword

def is_keyword(word):
    return keyword.iskeyword(word)

word1 = "True"
word2 = "Python"
print(f"'{word1}' is a keyword: {is_keyword(word1)}")
print(f"'{word2}' is a keyword: {is_keyword(word2)}")



