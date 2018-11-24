import nltk
import json
from nltk.corpus import wordnet


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

tokenizer = nltk.tokenize.TreebankWordTokenizer()
lemmatizer = nltk.WordNetLemmatizer()

wordCnt = 0
wordFreq = {}

done = 0

for item in data:
    done += 1
    if done % 1000 == 0:
        print("Done processing {:d} sentences.".format(done))
    sentence = item['sentence']
    sentence = sentence.replace('&#44;', ',')
    sentence = sentence.replace('&quot;', ' ')
    sentence = sentence.replace('&ndash;', ' ')
    sentence = sentence.replace('&mdash;', ' ')
    tokens = tokenizer.tokenize(sentence)
    wordTags = nltk.pos_tag(tokens)
    # print(wordTags)
    for i in range(len(tokens)):
        token = tokens[i]
        lemmatizedToken = lemmatizer.lemmatize(
            token, get_wordnet_pos(wordTags[i][1]))
        if str.isnumeric(lemmatizedToken):
            lemmatizedToken = 'xnumx'
        lemmatizedToken = lemmatizedToken.lower()
        if lemmatizedToken not in wordFreq:
            wordFreq[lemmatizedToken] = 1
        else:
            wordFreq[lemmatizedToken] += 1
        wordCnt += 1

for word in wordFreq:
    wordFreq[word] /= wordCnt

with open('./data/wordFreq.json', 'w') as fp:
    json.dump(wordFreq, fp)
