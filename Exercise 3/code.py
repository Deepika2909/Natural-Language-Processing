import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('stopwords')

user_input = input("Enter a sentence: ")
stop_words = set(stopwords.words("english"))

words = word_tokenize(user_input.lower())
words_filtered = []

for word in words:
    if word not in stop_words:
        words_filtered.append(word)

print(words_filtered)
