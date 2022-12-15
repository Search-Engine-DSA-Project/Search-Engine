import json
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize,sent_tokenize

with open("newsdata/airwars.json") as f:
    data = json.load(f)


alldata = "" 
for i in data:  #Stores content in a variable
    alldata += i["title"] 
    alldata += i["content"]

tokenize_words = word_tokenize(alldata) #Separates words in a list
stop_words = set(stopwords.words('english')) # All stopwords of English stored
keywordlist = [] # A list for keywords
punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
porter = PorterStemmer()

for word in tokenize_words: # Finds keywords to append in list 
    if word not in stop_words:
        if word not in punctuation: 
            keywordlist.append(porter.stem(word))

print(keywordlist)
print()




