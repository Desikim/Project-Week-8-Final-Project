#!/usr/bin/env python
# coding: utf-8

# In[22]:

import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences


# In[23]:

model = keras.models.load_model(r"C:\Users\kim.buchner\Desktop\Ironhack\Module1\WEEK8\Project5\Project5\models")

# In[27]:

import csv

with open(r"C:\Users\kim.buchner\Desktop\Ironhack\Module1\WEEK8\Project5\Project5\your-project\training_headlines.csv", newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

training_headlines = [item for sublist in data for item in sublist]

# In[28]:

tokenizer = Tokenizer(num_words=7500, oov_token="<OOV>")
tokenizer.fit_on_texts(training_headlines)


# In[31]:

def predict_sarcasm(user_input):
    user_input = [user_input]

    sequence = tokenizer.texts_to_sequences(user_input)
    padded = pad_sequences(sequence, maxlen=40, padding='post')
    pred = model.predict(padded)

    if pred[0][0]>=0.5:
        result = "This sentence is sarcastic!"

    else:
        result = "This sentence is not sarcastic!"
    st.write(result)
    return


# In[32]:
st.title("Sarcasm Detector")
user_input = st.text_input("Please enter a sentence to analyze")
analyze = st.button("Analyze")
if analyze:
  predict_sarcasm(user_input)



