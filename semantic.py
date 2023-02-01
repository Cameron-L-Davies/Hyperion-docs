import spacy  # importing spacy
nlp = spacy.load('en_core_web_md') # specifying the model we want to use. Remember to install this model by typing python -m spacy download en_core_web_md into your command line


# Similarities - monkey was noted to be more similar to banana than the cat was - likely due to their association
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#code from task notes:

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))




# ----------------
sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana"
]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

# Example ran in 'sm' model - has no word vectors loaded, it only uses context-sensitive tensors