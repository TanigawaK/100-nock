def bigram(seq):
  bigram = []
  for i in range(len(seq) - 1):
    bigram.append(seq[i:i+2])
  return bigram

X = set(bigram('paraparaparadise'))
Y = set(bigram('paragraph'))

print(X)
print(Y)
print('和集合:',X | Y)

print('積集合:',X & Y)

print('差集合:',X - Y)
print("'se'がXに含まれているか:",X >= {'se'})
print("'se'がYに含まれているか:",Y >= {'se'})
