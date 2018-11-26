# Introduction

MIML_RE model adopted from <https://nlp.stanford.edu/software/mimlre.shtml>.

The ```README``` file contains introductions on the project provided by the original authors.

The Relation Labeling Tool is the the ```label_tool``` directory.

## Authors

Mihai Surdeanu, Julie Tibshirani, Ramesh Nallapati, Sonal Gupta, John Bauer, 
David McClosky, Angel X. Chang, Valentin I. Spitkovsky, and 
Christopher D. Manning


## References

Mihai Surdeanu, Julie Tibshirani, Ramesh Nallapati, Christopher D. Manning. 
Multi-instance Multi-label Learning for Relation Extraction. 
Proceedings of the 2012 Conference on Empirical Methods in Natural Language 
Processing and Natural Language Learning (EMNLP-CoNLL), 2012.

## License

Copyright (c) 2009-2012 The Board of Trustees of The Leland Stanford Junior 
University. All Rights Reserved.

This program is free software; you can redistribute it and/or modify it under 
the terms of the GNU General Public License as published by the Free Software 
Foundation; either version 2 of the License, or (at your option) any later 
version.

This program is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS 
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with 
this program (see the file LICENSE.txt); if not, write to the Free Software 
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

For the license for all the jar files include in the lib/ directory, please
see the file LIBRARY_LICENSES.txt.


# How to Run

## The MIMR_RE model

The program requires java 1.6 or higher. I tested the model on KBP data provided by the authors. The results are in ```results``` directory.

To train and test the model, first unzip ```resources.zip``` and ```corpora.zip```, then run

```java -ea -cp classes/;lib/* edu.stanford.nlp.kbp.slotfilling.KBPTrainer -props config/kbp/kbp_mimlre.properties``` on Windows operating system, or

```java -ea -cp classes/:lib/* edu.stanford.nlp.kbp.slotfilling.KBPTrainer -props config/kbp/kbp_mimlre.properties``` on Unix operating system.

## The Relation Labeling Tool

### Generate Sample Data

The sample data is generated from the annotated data provided by Gabor Angeli at. el. 2014.

Python 3.6 or higher is required for the scripts.

run ```python parseCsv.py``` to generate 10 sample datasets. Each dataset contains 300 random data instances from the annotated dataset with either ```per:spouse```, ```per:city_of_birth```, ```org:city_of_headquarters```, or ```no_relation```.

### Construct Sentence Embedding

The sentence embedding is constructed using the simple weighted bag-of-words methods proposed in Sanjeev Arora at. el. 2016.

A precomputed word embedding is included in ```data``` directory. ```nltk``` is required for the scripts.

To generate sentence embedding for all the sentences, first unzip ```vectors.txt.zip```, then run ```python wordEmbedding.py```, ```python wordFreq.py```, and ```python sentenceEmbedding.py```. The result will be stored in ```data/sentenceVecs.json```.

### 2D Projection

```scikit-learn``` and ```nltk``` are needed for the script to run.

Run ```python projection {inputdata.json} {outputdata.json}``` to project the data into 2D using t-SNE. After projection a 2D scatter-plot will pop up and the results will be stored in ```{outputdata.json}```.

### Visual Labeling Interface

The web-based visual labeling interface can be invoked by running ```index.html``` in any modern internet browser supporting HTML5 such as Chrome, Safari, or Microsoft Edge.

By default the first sample and its projection is used. For now this cannot be changed interactively. It can only be changed by directly change the ```index.html``` file.