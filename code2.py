from nltk.tokenize import word_tokenize
import re

f=open("da.txt")
text=f.read()
text=re.sub('[^A-Za-z0-9]+',' ',text)
text=re.sub("\S*\d\S*",'',text).strip()
w=word_tokenize(text)
from nltk.stem import PorterStemmer
ps=PorterStemmer()
ps_st=[ps.stem(i) for i in w]
print("Stemming:",ps_st)

