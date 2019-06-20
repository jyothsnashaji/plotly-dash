import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as  pd
from numpy import random
from dash.dependencies import Input,Output
app=dash.Dash()

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\mpg.csv')
app.layout=html.Div([
    html.Div([
        dcc.Graph(id='mpgplot',figure={'data':[go.Scatter(x=df['model_year']+1900,y=df['mpg'],text=df['name'],hoverinfo='text',mode='markers')],
                                    'layout':go.Layout(title='MPG Data',xaxis={'title':'Model Year'},yaxis={'title':'MPG'},hovermode='closest'
                                        )})
            ],style={'width':'50%','display':'inline-block'}),
    html.Div([dcc.Graph(id='mpg_line',figure={'data':[go.Scatter(x=[0,1],y=[0,1],mode='lines')],
                                                'layout':go.Layout(margin={'l':0})})],
            style={'display':'inline-block'}),
    html.Div([dcc.Markdown(id='stats')])
])

@app.callback(Output('mpg_line','figure'),[Input('mpgplot','hoverData')])

def callback_graph(hD):

    v_index = hD['points'][0]['pointIndex']
    figure={'data':[go.Scatter(x=[0,1],y=[0,60/df.iloc[v_index]['acceleration']],mode='lines',line={'width':2*df.iloc[v_index]['cylinders']})],
            'layout':go.Layout(title=df.iloc[v_index]['name'],yaxis={'range':[0,60/df['acceleration'].min()]})}
    return figure

@app.callback(Output('stats','children'),[Input('mpgplot','hoverData')])

def callback_stats(hd):
    v_index = hd['points'][0]['pointIndex']
    stats="""
    {} cylinders
    {} displacement
    0 to 60mph {} acceleration""".format (df.iloc[v_index]['cylinders'],
                                    df.iloc[v_index]['displacement'],
                                    df.iloc[v_index]['acceleration'])
    return stats                    

if __name__ == "__main__":
    app.run_server()