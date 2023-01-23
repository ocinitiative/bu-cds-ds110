# Write the code to use the requests module to get the Rotten Tomatoes review site for *Star Wars:  A New Hope*, at URL https://www.rottentomatoes.com/m/star_wars_a_new_hope/reviews?intcmp=rt-scorecard_tomatometer-reviews .
# Then use Beautiful Soup to extract all div tags with a class of 'the_review'.



# Import the requests module
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
import nltk
nltk.download('punkt')

url = 'https://www.rottentomatoes.com/m/star_wars_a_new_hope/reviews?intcmp=rt-scorecard_tomatometer-reviews'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html, "html.parser")
reviews = soup.find_all('div', attrs={'class':'the_review'})

# Write some code to use Beautiful Soup's get_text() method to remove the tags from these text snippets.



for review in reviews:
    print(review.text)
    analysis = TextBlob(review.text)
    print(analysis.sentiment)
    print("")


# Finally, write the code to use the TextBlob class to print a Sentiment for each sentence, separated from the sentence itself by '::'.




