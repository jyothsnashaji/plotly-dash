import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd


df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\gapminderDataFiveYear.csv')

app=dash.Dash()

years=[]
for year in df['year'].unique():
    years.append({'label':str(year),'value':year})

app.layout=html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='dropdown',options=years,value=df['year'].min())
])


@app.callback(Output('graph','figure'),
                [Input('dropdown','value')])
def update_figure(selectedyear):
    df2=df[df['year']==selectedyear]
    traces=[]
    for continent in df2['continent'].unique():
        df3=df2[df2['continent']==continent]
        traces.append(go.Scatter(x=df3['gdpPercap'],y=df3['lifeExp'], mode='markers',name=continent))
    return go.Figure(traces)

if __name__ == "__main__":
    app.run_server()