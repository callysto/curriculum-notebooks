from html.parser import HTMLParser
from textblob import TextBlob
import nltk

nltk.download('stopwords')
from nltk.corpus import stopwords

class TagRemover(HTMLParser):
    def __init__(self):
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def remove_tags(html):
    s = TagRemover()
    s.feed(html)
    return s.get_data()

def interesting_words(text):
    blob = TextBlob(text)
    blob.words

    all_words = blob.words.lower()
    remove_words = stopwords.words('english') + ["'s", "n't", "'re", "'ll"]
    interesting_words = set(all_words) - set(remove_words)

    selected_words = []
    for word in all_words:
        if word in interesting_words:
            selected_words.append(word)
            
    return selected_words

def reverse_column(forward_column):
    return list(reversed(list(forward_column)))