import pandas as pd
from plotly.offline import plot
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

data = pd.read_csv('data/winemag-data_first150k.csv', sep=";")

# 150930 rows -> all unique !
# 11 cols : ['Unnamed: 0', 'country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery']
# first col useless :
data.drop('Unnamed: 0', axis=1)





##########################################
### Proportion of country -> pie chart ###
##########################################


# Values with others section
values = data['country'].value_counts() # all
values_main = values[values>0.016*len(data)] # first rows
values_other = values[values<=0.016*len(data)].sum() # others
t1 = pd.Series(values_other)
t1.index = ['Others']
values = values_main.append(t1) # On ajoute others

labels = values.index.tolist()
fig = go.Figure()
fig.add_pie(labels=labels, # les valeurs sur lesquelles on compte
            values=values, # ce qui sert à faire les pourcentages
            textposition='outside',
            )
fig.update_traces(hoverinfo='label+percent', # ce qu'on voit avec la souris
                  textinfo='label+percent', # Ce qu'on lit dans le pie
                  textfont_size=12, # taille du texte du pie
                  )
fig.update_layout(title="Proportion des vins du dataset par pays",
                  showlegend=False)
plot(fig)





#############################################
### price average by province and variety ###
#############################################

price = data.groupby(by=['country', 'province']).mean()['price']







