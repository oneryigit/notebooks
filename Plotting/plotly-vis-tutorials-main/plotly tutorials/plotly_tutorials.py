# =============================================================================
# Plotly Visualization Notes
# =============================================================================

# =============================================================================
# Required Modules
# =============================================================================
import pandas as pd
import numpy as np
import seaborn as sns

import chart_studio.plotly as py
import plotly.express as px
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import cufflinks as cf
cf.go_offline()

import plotly.io as pio
#pio.renderers.default='browser' #or
pio.renderers.default = 'chrome'
# =============================================================================
# Some Basics
# =============================================================================
from plotly import __version__
print(__version__) # 4.14.1

#Get some artifical data
df=pd.DataFrame(np.random.randn(100,4),columns='A B C D'.split())
df2=pd.DataFrame({'Category':['A','B','C'],
                  'Values':[32,43,50]})
# =============================================================================
# Ploting
# =============================================================================
df.iplot() #it will show plot on crome browser

df.iplot(kind='scatter', x='A', y='B',
         mode='markers', size=10)

df2.iplot(kind='bar', x='Category', y='Values')


df.sum().iplot(kind='bar')


df.iplot(kind='box')

# =============================================================================
# 3D plots
# =============================================================================

df3=pd.DataFrame({'x':[1,2,3,4,5],
                  'y':[10,20,30,20,10],
                  'z':[500,400,300,200,100]})


df3.iplot(kind='surface')



df4=pd.DataFrame({'x':[1,2,3,4,5],
                  'y':[10,20,30,20,10],
                  'z':[5,4,3,2,1]})

df4.iplot(kind='surface', colorscale='rdylbu')

# =============================================================================
# Hist
# =============================================================================

df['A'].iplot(kind='hist', bins=50)



df.iplot(kind='hist', bins=50) #whole dataframe

#spread
df[['A','B']].iplot(kind='spread')

#bubble

df.iplot(kind='bubble', x='A', y='C', size='B')

df.scatter_matrix()

# =============================================================================
# GEO-PLOT
# =============================================================================
#Choropleth Maps
import plotly.graph_objs as go #add for geo
data=dict(type='choropleth',
          locations=['AZ','CA','NY'],
          locationmode='USA-states',
          colorscale='Portland', #'jet' #'green'
          text=['Text 1', 'Text 2', 'Text 3'],
          z=[0.1,2.0,1.0],
          colorbar={'title':'Colorbar Title Goes Here'})

layout= dict(geo={'scope':'usa'})

choromap=go.Figure(data=[data],layout=layout)
iplot(choromap)


# =============================================================================
# Geo-USA
# =============================================================================

df=pd.read_csv('2011_US_AGRI_Exports')

data=dict(type='choropleth',
          colorscale='YlOrRd',
          locations= df['code'],
          locationmode='USA-states',
          z=df['total exports'],
          text=df['text'],
          marker=dict(line=dict(color='rgb(255,255,255)',width=2)),
          colorbar={'title':'Millions USD'}
          )

layout=dict(title='2011 Agriculture Exports by State',
            geo=dict(scope='usa',showlakes=True,
                     lakecolor='rgb(85,173,240)'))

choromap2=go.Figure(data=[data],layout=layout)
iplot(choromap2)

#marker state borders width.

# =============================================================================
# Geo-World
# =============================================================================

df=pd.read_csv('2014_World_GDP')

data=dict(type='choropleth',
          locations=df['CODE'],
          z=df['GDP (BILLIONS)'],
          text=df['COUNTRY'],
          colorscale='sunset',
          colorbar={'title':'2014 Global GDP'})

layout=dict(title='2014 Global GDP',
            geo=dict(showframe=False,
                     projection={'type':'mercator'}))


choromap3=go.Figure(data=[data], layout=layout)
iplot(choromap3)








