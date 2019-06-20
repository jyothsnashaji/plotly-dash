import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\2018WinterOlympics.csv')

trace0=go.Bar(x=df['NOC'],y=df['Gold'],name='Gold',marker={'color':'#FFD700'})

trace1=go.Bar(x=df['NOC'],y=df['Silver'],name='Silver',marker={'color':'#9EA0A1'})

trace2=go.Bar(x=df['NOC'],y=df['Bronze'],name='Bronze',marker={'color':'#CD7F32'})


data=[trace0,trace1,trace2]
layout=go.Layout(title="Total Medals")# for stacking barmode='stack')
fig=go.Figure(data,layout)
pyo.plot(fig)
