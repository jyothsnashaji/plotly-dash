import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from plotly import tools
df0=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\2010SantaBarbaraCA.csv')
trace0=go.Heatmap(x=df0['DAY'],y=df0['LST_TIME'],z=df0['T_HR_AVG'].values.tolist())

df1=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\2010SitkaAK.csv')
trace1=go.Heatmap(x=df1['DAY'],y=df1['LST_TIME'],z=df1['T_HR_AVG'].values.tolist())

df2=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\2010YumaAZ.csv')
trace2=go.Heatmap(x=df2['DAY'],y=df2['LST_TIME'],z=df2['T_HR_AVG'].values.tolist())

fig=tools.make_subplots(rows=1,cols=3,subplot_titles=['A','B','C'],shared_yaxes=True)
fig.append_trace(trace0,1,1)
fig.append_trace(trace1,1,2)
fig.append_trace(trace2,1,3)
pyo.plot(fig)