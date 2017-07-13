Title: Word Embeddings - Skip-gram model
Date: 2017-04-01 00:00
Category: Natural Language Processing

Image and audio processing systems work with rich, high-dimensional datasets encoded as vectors of the individual 
raw pixel-intensities for image data, or e.g. power spectral density coefficients for audio data. For tasks like object 
or speech recognition we know that all the information required to successfully perform the task is encoded in the data 
(because humans can perform these tasks from the raw data). However, natural language processing systems traditionally treat words as discrete atomic symbols, and therefore 'cat' may be represented as Id537 and 'dog' as Id143. These encodings are arbitrary, and provide no useful information to the system regarding the relationships that may exist between the individual symbols. This means that the model can leverage very little of what it has learned about 'cats' when it is processing data about 'dogs' (such that they are both animals, four-legged, pets, etc.). Representing words as unique, discrete ids furthermore leads to data sparsity, and usually means that we may need more data in order to successfully train statistical models. 
Using vector representations can overcome some of these obstacles. 



##**References**  FIX LINKS

* [Hierarchical Probabilistic Neural Network Language Model](https://arxiv.org/abs/1406.4729)
* [Distributed Representations of Words and Phrases and their Composition](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
* [Noise-Contrastive Estimation and its Generalizations](https://ieeexplore.ieee.org/document/7780429/)

With that I would like to wrap up. Any Questions ?
