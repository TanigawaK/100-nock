sentences = 'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
words = sentences.replace(',','').replace('.','').split(' ')
i = 0
result = [len(x) for x in words]

print(words)
print(result)
