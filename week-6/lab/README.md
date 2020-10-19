# Lab 6: Predict Majors of Node Students

### Goal

A certain Node PL is trying to predict whether or not someone is in a data science related major (i.e. CS or Stats) based upon the student's famiarity with various languages (i.e. Python, R, etc) and school year.

Your task: **apply ML concepts** to create a model that predicts whether or not someone is a data major or not.

### Outline

1. Start up a fresh collab notebook
2. Load in `survey_cleaned.csv` 
3. Drop irrelevant columns
4. Convert the target feature into `1` and `0`
5. Convert the rest into dummies (or assign ordinal values using `.map()`)
6. Split the data into input / output, train / test
7. What type of model is this? Supervised / Unsupervised? Classification / Regression? 
7. Pick a classifier, and fit the model
8. Evaluate / report the performance using accuracy

Check the key when you're done: [![Link](../../tools/buttons/open-colab.svg)](https://colab.research.google.com/github/ishaandey/node/blob/master/week-6/lab/survey-ml_key.ipynb)