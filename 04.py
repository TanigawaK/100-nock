sentences = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'
words = sentences.replace(',','').split(' ')
r = {}
for i, words in enumerate(words,1):
  if i in[1,5,6,7,8,9,15,16,19]:
    r[i] = words[0]

  else:
    r[i] = words[:2]

print(r)
