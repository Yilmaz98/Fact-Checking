from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
example_sent = input("Enter the input claim:")
 
stop_words = set(stopwords.words('english'))
 
word_tokens = word_tokenize(example_sent)
 
filtered_sentence = [w for w in word_tokens if not w in stop_words]
 
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
print(word_tokens)
print(filtered_sentence)
ans=""
for word in filtered_sentence:
	ans=ans+word	
	ans+=" "
print(ans)
