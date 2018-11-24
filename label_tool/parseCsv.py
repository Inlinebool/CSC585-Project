import csv
import json
import random

data = []
dataObjs = []
simpleDataObjs = []
negativeObjs = []
sampleObjs = []
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

positiveSampled = {}
negativeSampled = {}

for i in range(sampleNumber - negativeSampleNumber):
    x = random.randint(0, len(simpleDataObjs))
    while x in positiveSampled:
        x = random.randint(0, len(simpleDataObjs))
    positiveSampled[x] = True
    sampleObjs.append(simpleDataObjs[x])

for i in range(negativeSampleNumber):
    x = random.randint(0, len(negativeObjs))
    while x in negativeSampled:
        x = random.randint(0, len(negativeObjs))
    negativeSampled[x] = True
    sampleObjs.append(negativeObjs[x])

random.shuffle(sampleObjs)

with open("./data/data.json", 'w') as fp:
    json.dump(dataObjs, fp)
with open("./data/sample.json", 'w') as fp:
    json.dump(sampleObjs, fp)
