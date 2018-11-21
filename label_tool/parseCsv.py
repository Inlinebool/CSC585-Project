import csv
import json

data = []
dataObjs = []
simpleDataObjs = []
simpleEvents = ["per:spouse", "per:city_of_birth", "org:city_of_headquarters", "no_relation"]
with open('./data/annotated_sentences.csv', newline='', encoding="utf8") as csvFile:
    dataReader = csv.reader(csvFile, delimiter=',', quotechar='\"')
    for row in dataReader:
        data.append(row)

title = data[0]

for i in range(1, len(data)):
    item = {}
    for j in range(0, len(title)):
        item[title[j]] = data[i][j]
    if (item["relation"] in simpleEvents):
        simpleDataObjs.append(item)
    dataObjs.append(item)

print(dataObjs[0])
print(len(dataObjs))
print(len(simpleDataObjs))

with open("data.json", 'w') as fp:
    json.dump(dataObjs, fp)
with open("simpleData.json", 'w') as fp:
    json.dump(simpleDataObjs, fp)
