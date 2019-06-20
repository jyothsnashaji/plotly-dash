import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mpg.csv')

data=[go.Scatter(x=df['horsepower'],y=df['mpg'],text=df['name'],mode='markers',marker=dict(size=2*df['cylinders']))]

layout=go.Layout(title='Bubble')
fig=go.Figure(data,layout)
pyo.plot(fig)