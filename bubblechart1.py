import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mpg.csv')

data=[go.Scatter(x=df['mpg'],y=df['cylinders'],text=df['name'],mode='markers',marker=dict(size=df['displacement']/100))]

layout=go.Layout(title='Bubble')
fig=go.Figure(data,layout)
pyo.plot(fig)