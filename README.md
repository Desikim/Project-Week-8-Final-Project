<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Sarcasm Detector
*Kim Desi*

*Ironhack | May 2021*

## Content
- [Project Description📙](#project-description)
- [Questions❔](#questions)
- [Dataset📄](#dataset)
- [Cleaning💎](#cleaning-&-pre-processing)
- [Analysis📊](#analysis)
- [Model Training & Evaluation💫](#model-training-&-evaluation)
- [Conclusion🌟](#conclusion)
- [Future Work🔮](#future-work)
- [Workflow🔧](#workflow)
- [Organization📖](#organization)
- [Links](#links)

## Project Description📙

The goal of this project was to figure out and understand how to detect sarcasm in a sentence using a machine learning model. While researching about natural language processing and sentiment analysis, I came accross the problematic of being able to detect sarcasm in sentences. In sentiment analysis, certain words are used to decide wheter a sentence has a specific sentiment or not. 
For example, to detect a positive sentiment you could train a model with positive words like: good, great, awesome, happy, love, ... and use the frequency of positive words in a sentence to decide whether it is a positive sentence or not. This approach works for detecting negativity in sentences as well, but what about Sarcasm? As soon as you think about it, it makes sense - how can you train a model to detect sarcasm when there is no word that by itself is sarcastic? Sarcasm is hard to detect for people, so how hard is it for a model? 

## Questions❔

- In which way can sarcasm in a sentence even be detected?
- Which features and parameters are used to decide by the model whether a sentence is sarcastic or not?
- How does a model need to be built in order to detect sarcasm accurately?

## Dataset📄

The data set I used was created by Rishabh Misra, by scraping news headlines from "The Onion", a sarcastic fake-news newspaper, and the "Huff Post". The reason behind scraping news articles headlines is the formal style they are written in, as well as the absence of spelling mistakes and emojis. "New headlines for sarcasm detection" can be downloaded on [Kaggle](https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection). There are two versions available for download, I used version 2. The data consists of a json-file, which can be divided in three columns:
1. Sarcasm label (is_sarcastic)
2. Headlines (headline)
3. Link of the article (article_link)  
The data set I used was created by Rishabh Misra, by scraping news headlines from "The Onion", a sarcastic fake-news newspaper, and the "Huff Post".  
The reason behind scraping news articles headlines is the formal style they are written in, as well as the absence of spelling mistakes and emojis.
"New headlines for sarcasm detection" can be downloaded on [Kaggle](https://www.kaggle.com/rmisra/news-headlines-dataset-for-sarcasm-detection).  
The data consists of a json-file, which can be divided in three columns:
1. Sarcasm label (is_sarcastic)
2. Headlines (headline)
3. Link of the article (article_link)  
There are two versions available for download, I used version 2. The data set contains 28619 entries, of which 14985 entries are non-sarcastic headlines  
and 13634 entries are sarcastic headlines. 

## Cleaning & Pre-processing💎

The data set contained no missing values. It did however contain 116 duplicate rows, which have been dropped in order to deliver a
better data set to train the model on. Since the column containing the links to the news article did not carry any relevant information needed to detect sarcasm, it was deleted. After that I changed abbreveated words - e.g. I'm, you're, she's and it's - to their full written form: I am, you are, she is, it is,... 

## Analysis📊

To analyze the data set I attempted to create word clouds displaying the most frequently occuring words in the headlines labelled sarcastic and non-sarcastic. This attempt could not be realized yet as there is an installation problem in anaconda which is causing errors when creating word clouds. Once I fix the installation problems, I want to create the word clouds.

## Model Training & Evaluation💫

I created two different models using Keras Sequential model, word embedding and several other layers containing differing number of neurons.
The evaluation of the model was done by looking at the history of the models value loss and accuracy on the training data and on the testing data. This evaluation was then visualized using Matplotlib.  
It's clearly visible that the model is over fitted on the training data, which is shown by the high value loss of the model in the testing data. Changing vocabulary size and the maximum sentence lenght led to slight improvements.  
Afterwards the model was tested on completely unseen data (e.g. this sentence: "Good news: Jeff Bezos went to space. Bad news: He's back"). By changing the structure and tone of the unseen sentences, it became visible that my sarcasm detection model is very vague in certain instances. 

## Conclusion🌟

My conclusion is that a highly complex model, created by combining several layers of models in a neural network, is needed to create a decent and accurate sarcasm detector. Sarcasm is hard to detect for some people (e.g. the TV-show character Sheldon Cooper), so it makes sense that this task opposes even more difficulties for machines.  
For the level of understanding and knowledge of deep learning that I currently hold, I was able to answer my questions and gain amazing insights on how sarcastic sentences can be detected by a deep learning model. The concept of tokenizing, padding sentences and then embedding their words is amazingly interesting. It's a very logical way to interpret text in information-loaded numbers.

## Future Work🔮

My goal is to further understand Keras Sequential models, as well as other deep learning methods and neural network models that are being used to build sarcasm detection models. I'm planning on going over the models once I gained deeper understanding, to try and see if further improvements can be achieved.  
Another task I want to come back to are the missing word clouds! This seems to be an installation problem coming from Anaconda. 

## Workflow🔧

Outline:  
- Choose topic & data set
- Set up folder, repo, presentation
- Clean data set
- Find out what I need to do as I go 
- Install TensorFlow
- Figure out steps precisely and document 
- Create model & test accuracy
- Improve and change parameters
- Test model with unseen data 
- Update ReadMe & presentation 
- Build web app for user interaction (time-dependent)

## Organization📖

For the organization of this project I used OneNote:
- Project Plan
- To Do lists
- Workflow
- Links to interesting, helpful articles, videos and repos

## Links

[Repository](https://github.com/Desikim/Project5)  