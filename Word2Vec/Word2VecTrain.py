from gensim.models import Word2Vec
from nltk import tokenize
import string

with open("cleanWikiText_.txt","r",encoding="utf8") as f:
    corpus = f.readlines()

corpus_cleaned = []  
for seq in corpus:

    seq = seq.replace("\n", "")
    
    seq = seq.translate(str.maketrans('', '', string.punctuation))

    corpus_cleaned.append(seq)
    
word_model = Word2Vec([i.split() for i in corpus_cleaned], vector_size=100, min_count=7, window=5, epochs=3,workers=12)
word_model.save("word2vec.model")



