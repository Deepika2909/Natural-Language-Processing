import nltk 

from nltk.util import ngrams 

 

# Function to generate word n-grams 

def generate_word_ngrams(sentence, n): 

    words = sentence.split() 

    word_ngrams = list(ngrams(words, n)) 

    for gram in word_ngrams: 

        print(' '.join(gram)) 

 

# Example usage for word n-grams 

input_sentence = "The quick brown fox jumps over the lazy dog" 

n_value = 3  # Change to desired value of n-gram 

print(f"Word {n_value}-grams:") 

generate_word_ngrams(input_sentence, n_value) 
