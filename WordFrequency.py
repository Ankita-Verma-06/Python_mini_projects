par=input("enter a paragraph: ")
words=par.split(" ")
word_count={}
for word in words:
  word=word.strip(".,!?")
  word=word.lower()
  if word in word_count:
    word_count[word]+=1
  else:
    word_count[word]=1
print(word_count)
top_fr_words=sorted(word_count, key=word_count.get, reverse=True)[:5]
print(top_fr_words)
tfw=[]
for word in top_fr_words:
  tfw.append(word)
