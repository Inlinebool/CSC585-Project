from sklearn.manifold import TSNE
import json
import argparse

parser = argparse.ArgumentParser(description = 'Project data points to 2D')
parser.add_argument('inputFileName')
parser.add_argument('outputFileName')
parser.add_argument('--feature', default='bag_of_words')

args = parser.parse_args()

with open(args.inputFileName, 'r') as fp:
    data = json.load(fp)

# print(data)

