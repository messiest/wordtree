from nltk.corpus import wordnet as wn
import wn_utilities as util


# print(type(wn.all_synsets('n')))  # generator of all synsets

all_nouns = wn.all_synsets('n')

for i, synset in enumerate(all_nouns):

    print(i+1, synset) # synset.definition(),

    print('  Hypernyms:')
    for j, word in enumerate(synset.hypernyms()):
        print("\t", j+1, word)

    print('  Hyponyms:')
    for j, word in enumerate(synset.hyponyms()):
        print("\t", j+1, word)

    if i == 100000:

        break

    print("\n")