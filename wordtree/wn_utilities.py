"""
WordNet Docs - http://www.nltk.org/howto/wordnet.html

Chris Messier
"""
from nltk.corpus import wordnet as wn


def get_root(term):
    print("Root - ", term)
    for i, word in enumerate(wn.synsets(term)):
        print('\t', i, word, word.root_hypernyms())


def get_hypernyms(term):
    print("Hypernyms - ", term)
    for i, word in enumerate(wn.synsets(term)):
        print('\t', i, word, [str(w.name()) for w in word.hypernyms()])


def get_lemmas(term, pos):
    print("Lemmas - ", term)
    for i in wn.lemmas(term, pos):
        print('\t', i)


def main(search):
    get_lemmas(search, 'n')
    get_hypernyms(search)
    get_root(search)


if __name__ == "__main__":
    search_term = input("Search: ")
    main(search_term)
