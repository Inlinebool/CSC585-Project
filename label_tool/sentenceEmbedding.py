import json
import numpy as np
import nltk
from nltk.corpus import wordnet
from sklearn.decomposition import PCA


def get_wordnet_pos(treebank_tag):

    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


with open('./data/data.json', 'r') as fp:
    data = json.load(fp)

with open('./data/wordVecs.json', 'r') as fp:
    wordVecs = json.load(fp)

with open('./data/wordFreq.json', 'r') as fp:
    wordFreq = json.load(fp)

print('Done loading stuff.')
print(wordVecs['of'])

tokenizer = nltk.tokenize.TreebankWordTokenizer()
lemmatizer = nltk.WordNetLemmatizer()

vecSize = 200
a = 10e-3

done = 0
sentenceEmbeddings = np.zeros((len(data), vecSize))
for t in range(len(data)):
    done += 1
    if done % 1000 == 0:
        print("Done processing {:d} sentences.".format(done))
    # if done == 1000:
    #     break
    item = data[t]
    sentence = item['sentence']
    sentence = sentence.replace('&#44;', ',')
    sentence = sentence.replace('&quot;', ' ')
    sentence = sentence.replace('&ndash;', ' ')
    sentence = sentence.replace('&mdash;', ' ')
    tokens = tokenizer.tokenize(sentence)
    wordTags = nltk.pos_tag(tokens)
    embedding = np.zeros(vecSize)
    wordCnt = 0
    for i in range(len(tokens)):
        token = tokens[i]
        lemmatizedToken = lemmatizer.lemmatize(
            token, get_wordnet_pos(wordTags[i][1]))
        if str.isnumeric(lemmatizedToken):
            lemmatizedToken = 'xnumx'
        lemmatizedToken = lemmatizedToken.lower()
        # print(lemmatizedToken)
        if wordVecs.get(lemmatizedToken) != None:
            wordEmbedding = np.array(wordVecs[lemmatizedToken])
            w = a / (a + wordFreq[lemmatizedToken])
            embedding += w * wordEmbedding
            wordCnt += 1
    sentenceEmbeddings[t] = embedding / wordCnt

pca = PCA(n_components=1).fit(sentenceEmbeddings)
firstComponent = pca.components_

sentenceVecs = {}

for i in range(len(data)):
    sentenceEmbeddings[i] -= firstComponent[0]
    sentenceVecs[data[i]['key']] = sentenceEmbeddings[i].tolist()

with open('./data/sentenceVecs.json', 'w') as fp:
    json.dump(sentenceVecs, fp)
