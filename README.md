# Introduction

MIML_RE model adopted from <https://nlp.stanford.edu/software/mimlre.shtml>.

The ```README``` file contains introductions on the project provided by the original authors.

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

The program requires java 1.6 or higher. I tested the model on KBP data provided by the authors. The results are in ```results``` directory.

To train and test the model, first unzip ```resources.zip``` and ```corpora.zip```, then run

```java -ea -cp classes/;lib/* edu.stanford.nlp.kbp.slotfilling.KBPTrainer -props config/kbp/kbp_mimlre.properties``` on Windows operating system, or

```java -ea -cp classes/:lib/* edu.stanford.nlp.kbp.slotfilling.KBPTrainer -props config/kbp/kbp_mimlre.properties``` on Unix operating system.
