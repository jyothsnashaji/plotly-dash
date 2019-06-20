import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mpg.csv')

data=[go.Histogram(x=df['mpg'])]
layout= go.Layout(title='Histogram')
fig=go.Figure(data,layout)
pyo.plot(fig)