import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(56)

x=np.linspace(0,1,100)
y=np.random.randn(100)

trace0=go.Scatter(x=x,y=y+5,
                mode='markers',name='markers')

trace1=go.Scatter(x=x,y=y,mode='lines',name='liness')

trace2=go.Scatter(x=x,y=y-5,mode='lines+markers', name='both')
data=[trace0,trace1,trace2]

layout=go.Layout(title='Line Chart')

fig=go.Figure(data,layout)
pyo.plot(fig)