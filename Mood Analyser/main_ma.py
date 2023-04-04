import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import glob
#using glob library to get the list of the file name
text_files=[]
for text_file in text_files:
    #opeining the text file
    with open(,"r",encoding='utf-8',) as file:
        book=file.read()
print(type(book))

# Create an instance of the SentimentIntensityAnalyzer class
analyzer = SentimentIntensityAnalyzer()

mood=analyzer.polarity_scores(book)
