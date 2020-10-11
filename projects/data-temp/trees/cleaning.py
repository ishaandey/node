url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-01-28/sf_trees.csv'
import pandas as pd 
import numpy as np
df = pd.read_csv(url)

df['species_name'] = df.species.str.split('::').apply(lambda x: x[0].strip())
df['species_name'] = df.species_name.replace({'':np.nan})
df['common_name'] = df.species.str.split('::').apply(lambda x: x[-1].strip())
df['common_name'] = df.common_name.replace({'':np.nan})
df['site_location'] = df.site_info.str.split(':').apply(lambda x: x[0].strip())
df['site_location'] = df.site_location.replace({'':np.nan})
df['site_type'] = df.site_info.str.split(':').apply(lambda x: x[-1].strip())
df['site_type'] = df.site_type.replace({'':np.nan})
df2 = df.drop(columns=['site_order','species','site_info']).copy()
df2 = df2.dropna(subset=['species_name','common_name','site_location','site_type','dbh','date'])
df2 = df2[['tree_id', 'legal_status', 'caretaker', 'dbh',
       'plot_size',  'species_name', 'common_name', 'date',
       'site_location', 'site_type','latitude', 'longitude','address']]
df2.to_csv('week-1/trees.csv',index=False)