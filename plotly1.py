#scatter plot

import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

np.random.seed(42)

x=np.random.randint(1,101,100)
y=np.random.randint(1,101,100)

data=[go.Scatter(x=x,y=y,mode='markers',marker=dict(size=12,
                            color='rgb(100,10,10)',
                            symbol='cross-thin-open',
                            line={'width':2}))]
layout=go.Layout(title='Scatter Plot',
                xaxis={'title':'X AXIS'},
                yaxis=dict(title='Y AXIS'),
                hovermode='closest')

fig=go.Figure(data,layout)
pyo.plot(fig,'scatter.html')