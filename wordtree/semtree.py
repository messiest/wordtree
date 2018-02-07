from nltk.corpus import wordnet as wn
import networkx

import wn_utilities as util




def main():
    word = "cat"
    hypernyms = util.get_hypernyms(word)
    print(hypernyms)

if __name__ == "__main__":
    main()