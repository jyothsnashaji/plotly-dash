import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mocksurvey.csv')

data=[]

for col in df.columns:
    if col.startswith('Question'):
        continue
    data.append(go.Bar(x=df['Question'],y=df[col],name=col))

layout=go.Layout(title='Survey',barmode='stack')
fig=go.Figure(data,layout)
pyo.plot(fig)