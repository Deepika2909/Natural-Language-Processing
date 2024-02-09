import nltk

from nltk.tokenize import word_tokenize

def tokenize_text(text):

tokens = word_tokenize(text)

return tokens

sample_inputs = [

"welcome to nlp lab"," happy new year",

]

for input_text in sample_inputs:

print("Input:", input_text)

tokens = tokenize_text(input_text)

print("Tokens:", tokens)

print()
