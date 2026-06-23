par=input(" enter a paragraph:")
words=par.split()
word_count=0
vowel_count=0
vowels='aeiouAEIOU'
for word in words:
  word_count=word_count+1
  for char in word:
    if char in vowels:
      vowel_count=vowel_count+1
print(word_count)
print(vowel_count)
longest_word = max(words, key=len)
print(longest_word)
