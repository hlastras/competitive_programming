import re
from collections import Counter

f = open("03-pg17013.txt")
book = f.read()
f.close()

book = book.lower()
book = re.sub(r"[^abcdefghijklmnñopqrstuvwxyzáéíóúü]", ' ', book)
words = list(filter(lambda x: (len(x) > 2), book.split()))

word_and_occ_by_index = list(Counter(words).items())
word_and_occ_by_index.sort(key=lambda x: x[0]) # sort alphabetically
word_and_occ_by_index.sort(key=lambda x: x[1], reverse=True) # sort by occurrences. Python sort is stable

occ_and_index_by_word = {}
for index, data in enumerate(word_and_occ_by_index):
  occ_and_index_by_word[data[0]] = (data[1], index)

n = int(input())
for case in range(1, n+1):
  word = input()
  result = ""
  if word.isnumeric():
    index = int(word)-1
    data = word_and_occ_by_index[index]
    result = "%s %d" % (data[0], data[1])
  else:
    data = occ_and_index_by_word[word]
    result = "%d #%d" % (data[0], data[1]+1)


  print("Case #%d: %s" % (case, result))