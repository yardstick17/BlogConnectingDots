Title: Hierarchical Probabilistic Neural Network Language Model
Date: 2017-04-01 00:00
Category: Research Paper Explained


[Paper Link](http://www.iro.umontreal.ca/~lisa/pointeurs/hierarchical-nnlm-aistats05.pdf)
####Authors: <span> Frederic Morin, Yoshua Bengio </span>

###**Aim**
Various neural network architecture have been used for Language modeling. With the emergence of word embeddings, these models
have been successfully applied. However these models are quite slow in comparison to traditional n-gram models.
To speed-up training and prediction, hierarchical the decomposition of the conditional probabilities that yields a speed-up by a factor about 200.

###**Introduction**
In n-gram model as the size of vocabulary increases, the dictionary sizes with all combinations shoots up very sharply.

###Challenges
*   Traversal across all combination even if a small fraction of update is done.
*   Similar object should have the same probability which is not possible if knowledge free representation is used.
*   Long training time and huge computation is needed.
 
 
##### **The objective of this paper is thus to propose a much faster variant of the neural probabilistic language model.**
