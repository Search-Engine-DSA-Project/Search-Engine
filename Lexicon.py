import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize

with open("newsdata/airwars.json") as f: # Opens files
    data = json.load(f)


alldata = "" 
for i in data:  #Stores content in a variable
    alldata += i["title"] 
    alldata += i["content"]

tokenize_words = word_tokenize(alldata) #Separates words in a list
stop_words = set(stopwords.words('english')) # All stopwords of English stored
keyword_dictionary = {} # Dictionary for keywords with word IDs
word_ID = 0
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
porter = PorterStemmer()

for word in tokenize_words: # Finds keywords to append in list 
    if word not in stop_words:
        if word not in punctuation: 
            word = porter.stem(word)
            keyword_dictionary[word] = word_ID
            word_ID += 1

print(keyword_dictionary)




