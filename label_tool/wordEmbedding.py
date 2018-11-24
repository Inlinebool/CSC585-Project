import json
import numpy as np

wordVecs = {}

with open('./data/vectors.txt', 'r') as fp:
    firstLine = fp.readline()
    firstLine = str.split(firstLine, ' ')
    wordNumber = int(firstLine[0])
    # print(wordNumber)
    vecSize = int(firstLine[1])
    # print(vecSize)
    done = 0
    for i in range(wordNumber):
        done += 1
        if done % 10000 == 0:
            print("Done reading {:d} words.".format(done))
        line = fp.readline()
        line = str.split(line, ' ')
        # print(line)
        word = line[0]
        # print(word)
        vec = [float(x) for x in line[1:len(line) - 1]]
        assert(len(vec) == vecSize)
        # vec = np.array(vec)
        wordVecs[word] = vec

with open('./data/wordVecs.json', 'w') as fp:
    json.dump(wordVecs, fp)
