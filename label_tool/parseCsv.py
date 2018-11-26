import csv
import json
import random

data = []
dataObjs = []
simpleDataObjs = []
negativeObjs = []
simpleEvents = ["per:spouse", "per:city_of_birth",
                "org:city_of_headquarters"]
with open('./data/annotated_sentences.csv', newline='', encoding="utf8") as csvFile:
    dataReader = csv.reader(csvFile, delimiter=',', quotechar='\"')
    for row in dataReader:
        data.append(row)

title = data[0]

for i in range(1, len(data)):
    item = {}
    for j in range(0, len(title)):
        item[title[j]] = data[i][j]
    if (item["relation"] == "no_relation"):
        negativeObjs.append(item)
    if (item["relation"] in simpleEvents):
        simpleDataObjs.append(item)
    dataObjs.append(item)

print(dataObjs[0])
print(len(dataObjs))
print(len(simpleDataObjs))
print(len(negativeObjs))

sampleNumber = 300
negativeRatio = len(negativeObjs) / len(dataObjs)
negativeSampleNumber = int(sampleNumber * negativeRatio)

sampleFileNumber = 10

for t in range(sampleFileNumber):
    positiveSampled = {}
    negativeSampled = {}
    sampleObjs = []

    for i in range(sampleNumber - negativeSampleNumber):
        x = random.randint(0, len(simpleDataObjs) - 1)
        while x in positiveSampled:
            x = random.randint(0, len(simpleDataObjs) - 1)
        positiveSampled[x] = True
        sampleObjs.append(simpleDataObjs[x])

    for i in range(negativeSampleNumber):
        x = random.randint(0, len(negativeObjs) - 1)
        while x in negativeSampled:
            x = random.randint(0, len(negativeObjs) - 1)
        negativeSampled[x] = True
        sampleObjs.append(negativeObjs[x])

    random.shuffle(sampleObjs)
    sampleFileName = './data/sample_' + str(t) + '.json'

    with open(sampleFileName, 'w') as fp:
        json.dump(sampleObjs, fp)


# with open("./data/data.json", 'w') as fp:
#     json.dump(dataObjs, fp)
