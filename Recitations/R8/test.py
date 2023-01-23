# Use TextBlob to find the individual words in the sentence, "If I had $1,000,000.00, I'd be rich."

from textblob import TextBlob

sentence = "If I had $1,000,000.00, I'd be rich."

blob = TextBlob(sentence)

for word in blob.words:
    print(word)

# Output:
# If
# I
# had
# 1,000,000.00
# I'd
# be
# rich

# Still Textblob

# Download the speech tagger, then find and interpret the tag that is given to the million dollars in the sentence above.

from textblob import TextBlob

sentence = "If I had $1,000,000.00, I'd be rich."

blob = TextBlob(sentence)

for word in blob.words:
    print(word, word.tag_)

# Try using the default TextBlob sentiment analyzer on the strings, "Woo hoo!  I'm rich!" and ""Too bad I'm not actually rich."

from textblob import TextBlob

blob = TextBlob("Woo hoo!  I'm rich!")

print(blob.sentiment)

blob = TextBlob("Too bad I'm not actually rich.")

print(blob.sentiment)

# Try removing the stopwords from the sentence, "If I can't have a million dollars, nobody else should have a million dollars, either."

from textblob import TextBlob

sentence = "If I can't have a million dollars, nobody else should have a million dollars, either."

blob = TextBlob(sentence)

for word in blob.words:
    if word not in blob.stopwords:
        print(word)

# Now write a function that iterates through the TextBlob-discovered sentences in a string, and for each, ignore it if it's missing an NNP (singular proper noun).  If it has at least one NNP, create a tuple out of the NNP word that was found and the sentiment polarity of the sentence.  Return a list of these tuples.  For example, analysis of the string "I hate Coke Products.  But I love Honest Tea."  might return [("Coke",-0.8),("Honest",0.55), ("Tea",0.55)].

from textblob import TextBlob

def analyze_sentences(sentence):
    blob = TextBlob(sentence)
    results = []
    for sentence in blob.sentences:
        for word in sentence.words:
            if word.tag_ == "NNP":
                results.append((word, sentence.sentiment.polarity))
                break
    return results

# Try using the requests module and BeautifulSoup to grab all the large headers (h1 and h2) from this text of Alice's Adventures in Wonderland: https://www.gutenberg.org/files/11/11-h/11-h.htm
# Store the header texts as a list, then print the list.

import requests
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/files/11/11-h/11-h.htm"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

headers = soup.find_all(["h1", "h2"])

header_texts = []

for header in headers:
    header_texts.append(header.text)

print(header_texts)







