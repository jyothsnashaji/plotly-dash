import pandas as  pd
import plotly.offline as pyo
import plotly.graph_objs as go

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\2010YumaAZ.csv')


days=['TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY','MONDAY']


data=[]

for day in days:
    df2=df[df['DAY']==day]
    trace=go.Scatter(x=df2['LST_TIME'],y=df2['T_HR_AVG'],mode='lines',name=day)
    data.append(trace)

pyo.plot(data)
