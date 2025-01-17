# -*- coding: utf-8 -*-
"""Text_Generation_with_Marvok_Chains(Project3).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TFnUhqDGpOmbW9kewhyhEXmcwkJoHmxs

Markov Chains are simple stochastic model in which a system can exist in a number of states.
"""

from google.colab import drive
drive.mount('/content/drive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/drive/My Drive/Colab Notebooks

"""Installing Markovify"""

!pip install markovify

"""Start by importing markovify library and a text file whose style we would like to imitiate"""

import markovify
import pandas as pd
df = pd.read_csv('/content/airport_reviews.csv.zip')

"""Next, join the individual reviews into 1 large text string and build a Markov chain model using the airport review text"""

from itertools import chain
N=100
review_subset = df["content"][0:N]
text = "".join(chain.from_iterable(review_subset))
markov_Chain_model = markovify.Text(text)

"""Generate 5 sentences using the Markov chain model"""

for i in range (5):
  print(markov_Chain_model.make_sentence())

"""Generate 3 sentence with a large of no more than 140 characters"""

for i in range (3):
  print(markov_Chain_model.make_short_sentence(140))

"""1. We import markovify library, a library for Markov Chain computations and reading in text which we will inform at our Markov Model

2. We create a Markov Chain Model using the text

3. We generate a few sentences

4. we create a few tweets in the style of the airport reviews using our Markov Chain
"""