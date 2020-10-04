# Lab


## Instructions

### Data Import

1. In google colab, click the bottom-most icon (files), hit the upload icon, and upload both survey_data and survey_names CSV files.
2. Import pandas and numpy, then import the CSVs into dataframes using `pd.read_csv('filename.csv')`

### Data Cleaning

1. Combine the data! We have a `survey_data` and `survey_names` dataset, put them together.

2. Fill any missing preferred name with the first name

3. Clean the data! Make sure to normalize things like capitalization, and try googling methods to convert anything that has "first" into `1` in the school year column, for example.

### Visualization

1. Show me a couple of histograms that describe skill levels. You may need to change some of the skill levels 

2. What are common hobbies? Interests? Use the code below to generate a wordcloud. Replace `df.column` with whatever column you're interested in.

```python 
text = " ".join(df.column.values.to_list())

from wordcloud import WordCloud, STOPWORDS
wordcloud = WordCloud(width = 800, height = 600, random_state=1, stopwords = STOPWORDS,
background_color='salmon', colormap='Pastel1', collocations=False).generate(text)
```

- Check out [this link](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter) for more colors.

### Insights

1. How many students are in the class? How many of them are *not* a UVA undergraduate?

2. What was the median time of survey form submission?

3. How many people were at each comfort level with Python? With statistics?
