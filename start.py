year = u'வியாழன்'

print(year)
#just adding space
print('''


''')


word_list = []

#working
from uniseg.graphemecluster import grapheme_clusters
from uniseg.wordbreak import words
for word in list(words(year)):
#    for letter in list(grapheme_clusters(word)):
#       print (letter)

    word_list.append(word)

for words in word_list:
    print(words)
