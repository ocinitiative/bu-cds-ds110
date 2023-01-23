# Text Processing with TextBlob

# import something we need

from textblob import TextBlob
import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

# Create a TextBlob object (thi is a demo)

blob = TextBlob("Textblob is amazingly simple to use. What great fun!")

# Print the words and tags

for words, tag in blob.tags:
    print(words, tag)

# Print noun phrases

print(blob.noun_phrases)

# Print words in singular and plural form

for word in blob.words:
    print(word.singularize())
    print(word.pluralize())

# TextBlob objects have a .sentiment attribute with polarity and subjectivity scores

print(blob.sentiment)

# So now, let's do something more interesting
# Write a function just_verbs() that takes a string as an argument, and returns a list of the verbs in the sentence.
# Note that the tags returned in the .tags attribute of a TextBlob start with 'VB' for verbs.

def just_verbs(text):
    blob = TextBlob(text)
    return [word for word, tag in blob.tags if tag.startswith('VB')]

# Test your function with the following sentences:

print(just_verbs("Mary slapped the green witch."))
print(just_verbs("Peter told me that he would never do that again."))
print(just_verbs("I love to write Python programs."))

# Write a function just_nouns() that takes a string as an argument, and returns a list of the nouns in the sentence.

def just_nouns(text):
    blob = TextBlob(text)
    return [word for word, tag in blob.tags if tag.startswith('NN')]

# Test your function with the following sentences:

print(just_nouns("Mary slapped the green witch."))
print(just_nouns("Peter told me that he would never do that again."))
print(just_nouns("I love to write Python programs."))
