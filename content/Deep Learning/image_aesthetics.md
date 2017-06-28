Title: Image Aesthetic Assessment
Date: 2017-05-01 00:00
Category: Deep Learning, Artificial Intelligence
Summary: Image Aesthetic Assessment using Deep Learning. The defined network takes the complete image instead of fixed or re-sized input. This makes the network to learn for original image composition.  


<br>



> **_"Beauty is really in the eye of the beholder"_**


Image aesthetics assessment is an attempt to define the **beauty** of an Image.
While everyone has different tastes, there are universally accepted norms when it comes to beauty – things which everyone pretty much agrees are beautiful, like sunsets or sunrises over the mountains or the ocean.


![Beautiful Image](https://usatunofficial.files.wordpress.com/2012/03/barns_grand_tetons.jpg)

Some of the visual feature that come handy are 

* edge distributions, 
* color histogram, 
* Some photographic rules like rue of thirds also determines the beauty of an image.


*Defining image quality with visual features like other manually curated features are limited in the scope.*


<br>


The two photographer's story.

  Great Shot!!  | So what?
  ------------- | -------------
  ![Beautiful Image](https://image.ibb.co/eVhL0k/resize_thumb_ambiance_amazing_1024.jpg)  | ![low quality Image](https://image.ibb.co/ittcfk/resize_thumb_ambiance_bad_1024.jpg)
  
The Image is of same place taken with different lightening, angle, adjusted contrast. And it is obvious that image on the left has better aesthetic attire.

<br>


**Significance of Image Aesthetics**

For a platform especially that serves media content, one of the crucial aspect is to show high quality content. With social sites and the given ‘selfie’ trend, we are generating huge amount of data in the form of either images or videos.
 Having a track on the quality will always be helpful.


  Curated Content  |  User Generated Content
  ------------- | -------------
  ![Curated Content](https://image.ibb.co/fwvb6Q/resize_thumb_Screen_Shot_2017_04_15_at_11_18_25_AM_1024.jpg)  | ![User Generated Content](https://image.ibb.co/kThTLk/resize_thumb_Screen_Shot_2017_04_15_at_11_30_00_AM_1024.jpg)


<br>

## **Can we model such Human Perception?**

<br>

## **Deep learning**

The topic needs no introduction. It’s a revolution especially in the image classification domain since the last 5 years. With “Alexnet” winning the Image-Net competition, improving error rate with a huge margin acted as spark in the field. Since then, CNN has many state of the arts on its name.

**Network architecture of Alexnet.** 

![Alexnet architecture](https://image.ibb.co/cG4sfk/thumb_CNN_image_1024.jpg)

The first layer is input, where input in fed to the network. We can see there pooling operations, convolution operations finally followed by a fully connected layer 
and final softmax layer so that we get values as the probability for each class we label.

<br>

## **Fixed size input constraint**

  
  Input Layer   |  
  ------------- | -------------
  ![Input Layer](https://image.ibb.co/mMhFi5/thumb_input_CNN_image_1024.jpg) | Input image **re-sized to 224 * 224** irrespective of original image shape.


We always resize the input feature vector. If the image is larger, image is cropped 
or pad image if image dimensions are smaller, to get a fixed size input to fed the network


  

  The Mountains |  Qutub Minar
  ------------- | -------------
  ![Mountains](https://www.freewebheaders.com/wordpress/wp-content/gallery/beautiful-landscape/iceland-blue-lagoon-and-snow-mountains-landscape-header.jpg) | ![Qutub Minar](http://images.mapsofindia.com/india-tour/newvolume/mapindia/india-tour/wp-content/blogs.dir/6/files/2012/09/qutub-minar-minaret.jpg)



The above two images are **beautiful in their original aspect ratio.** 
What happens if we re-size the image to a fixed size of 224 * 224? 
Certainly the image will **loose all it’s original aesthetic value!** 
From Landscape to Squared size. All damage is done. The original image composition is lost when image is re-sized.

<br>

## **Demystifying the Network Architecture**

![Network Architecture](https://image.ibb.co/cG4sfk/thumb_CNN_image_1024.jpg)

Let’s unveil the hidden layers! So, we can see that after the input , there are few layers of **Operations**. 
The operations are either **Max-pooling** or convolving with a filter i.e. **Convolution**.
So why fixed size of input is required at all then?  
It’s because of the **Fully Connected Layer** just before the outputs. 
Fully Connected Layers are in the network for non-linear combination of feature extracted before in convolution network.

Let's understand bit by bit.

<br>


## **Max Pooling**

Max pooling are there for **Down-sampling** the feature space while maintain the spatial information
Max Pooling in action

![Max Pooling](https://image.ibb.co/jKK0GQ/cropped_max_pooling.gif)


<br>


##**Spatial Pyramid Pooling**
In spp, an image is divided into bins. Each bin is pooled in its turn. As the number of bins are fixed, 
we always get the **Fixed Shape Output**.

Spp operation in action

![Spatial Pyramid Pooling](https://image.ibb.co/juAki5/sppp_2_cropped.gif)

![Spatial Pyramid Pooling](https://image.ibb.co/f77y35/bin_4_spp.gif)

<br>


##**Spp Network Architecture**

![Spp Network Architecture](https://image.ibb.co/fxiPAk/network.png)

The first network is the traditional CNN , we can see the **Max-pool layer** just before the fully connected layer.
In the second architecture, the last max pooling layer is **replaced by a Spp layer**. 
With the **Fixed Bin size (1,2,4)** we make sure that the fully connected layer gets the fixed shape input.

![Spp Network Architecture](https://camo.githubusercontent.com/9099d29d9e59248dff137dd10189e0c81d35aa56/687474703a2f2f692e696d6775722e636f6d2f5351574a566f442e706e67)


<br>

##**Training the Spp-Net**

Training the Spp-Net on **live-dataset**, very small dataset, about 1K images total, model achieved the accuracy of 75% on training data, 83% on the test data.

  Accuracy  |  Training Loss
  ------------- | -------------
  ![Spp-Net Accuracy](https://image.ibb.co/m9AAi5/training_accuracy.png)  | ![Spp-Net Training Loss](https://image.ibb.co/fkS1qk/training_loss.png)



<br>

##**Takeaways**

**With Spp in Network**  

* Model learns the scale invariant feature like SIFT(traditional image processing algorithm).
* One of the challenge in text classification with Deep learning is the fixed size feature vector representation of sentence.


<br>

##**Interesting Results**

<br>

  Blurred Cropped Image, Model predicted **high score of 0.46** |     
  ------------- | -------------
  ![Blurred Image](https://image.ibb.co/nqyrqk/Screen_Shot_2017_04_25_at_2_48_51_PM.png)  |
    

<br>

  Complete Image, Model predicted **high score of 0.94** |  
  ------------- | -------------
  ![Complete Image](https://image.ibb.co/fR5zbQ/blurred_0071.jpg)  | 
      

<br>

##**References**

* [Kaiming He, Xiangyu Zhang, Shaoqing Ren, Jian Sun, Spatial Pyramid Pooling in Deep Convolutional Networks for Visual Recognition](https://arxiv.org/abs/1406.4729)
* [Alex Krizhevsky, Ilya Sutskever, Geoffrey E. Hinton, ImageNet Classification with Deep Convolutional Neural Networks 2012](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks.pdf)
* [Long Mai, Hailin Jin, Feing Liu, Composition-Preserving Deep Photo Aesthetics Assessment](https://ieeexplore.ieee.org/document/7780429/)


With that I would like to wrap up. Any Questions ?
