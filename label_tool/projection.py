from sklearn.manifold import TSNE
import json
import argparse
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description='Project data points to 2D')
parser.add_argument('inputFileName')
parser.add_argument('outputFileName')
parser.add_argument('--feature', default='bag_of_words')

args = parser.parse_args()

with open(args.inputFileName, 'r') as fp:
    data = json.load(fp)

if args.feature == 'bag_of_words':
    with open('./data/sentenceVecs.json', 'r') as fp:
        sentenceVecs = json.load(fp)

vecSize = 200

# print(data)
vecs = np.zeros((len(data), vecSize))
for i in range(len(data)):
    vecs[i] = np.array(sentenceVecs[data[i]['key']])

tsne = TSNE(n_components=2)

projection = tsne.fit_transform(vecs)

catagory = []
catagoryNames = ['per:spouse', 'per:city_of_birth',
                 'org:city_of_headquarters', 'no_relation']
for item in data:
    for i in range(len(catagoryNames)):
        if item['relation'] == catagoryNames[i]:
            catagory.append(i)

with open(args.outputFileName, 'w') as fp:
    json.dump(projection.tolist(), fp)

projectionFig = plt.figure()
projectionAx = projectionFig.add_subplot(111)
projectionAx.set_aspect('equal', 'box')
projectionCollection = projectionAx.scatter(
    projection[:, 0], projection[:, 1], c=catagory, cmap=plt.cm.get_cmap('tab10', 4))

formatter = plt.FuncFormatter(lambda val, loc: catagoryNames[val])
projectionFig.colorbar(projectionCollection, ax=projectionAx, ticks=[
                       0, 1, 2, 3], format=formatter)
# projectionCollection.clim(-0.5, 2.5)

plt.show()
