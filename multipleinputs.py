import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mpg.csv')
app=dash.Dash()

features=df.columns

app.layout=html.Div([
    html.Div([
        dcc.Dropdown(id='xaxis',
                    options=[{'label':i,'value':i}for i in features],
                    value='displacement')],
       style={'width':'48%','display':'inline-block'}),
    html.Div([
        dcc.Dropdown(id='yaxis',
                    options=[{'label':i,'value':i}for i in features],
                    value='mpg')],
        style={'width':'48%','display':'inline-block'}
    ),
    dcc.Graph(id='graph')
])
@app.callback(Output('graph','figure'),[Input('xaxis','value'),Input('yaxis','value')])
def update_graph(xaxis,yaxis):
    return {'data':[go.Scatter(x=df[xaxis],
                                y=df[yaxis],
                                text=df['name'],
                                mode='markers'
                                )],
            'layout':go.Layout(title="Graaaaaph",
                            xaxis={'title':xaxis},
                            yaxis={'title':yaxis})}

if __name__ == "__main__":
    app.run_server()