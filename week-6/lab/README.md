# Lab 6: Predict Majors of Node Students

A certain Node PL is trying to predict whether or not someone is in a data science related major (i.e. CS or Stats), based upon the student's famiarity with various languages (i.e. Python, R, etc).

Your task: **apply ML concepts** to create a model that predicts whether or not someone is a data major or not.

High-Level Steps:

1. Start up a fresh collab notebook, load in `survey_cleaned.csv` 
2. Drop irrelevant columns
3. Convert the target into `1` and `0`
4. Convert the rest into dummies (or assign ordinal values using `.map()`)
5. Split the data into input / output, train / test
6. Pick a classifier, and fit the model
7. Evaluate / report the performance using accuracy

Check the key when you're done: [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-6/lab/survey-ml_key.ipynb)