def ngram(seq,n):
  ngram = []
  for i in range(len(seq) - n + 1):
    ngram.append(seq[i:i + n])
  return ngram
text = 'I am an NLPer'
print('word bi-gram:',ngram(text,2))
print('char bi-gram:',ngram(text.split(),2))
