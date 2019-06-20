import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app=dash.Dash()

np.random.seed(42)
x=np.random.randint(1,101,100)
y=np.random.randint(1,101,100)

app.layout=html.Div([dcc.Graph(id='scatterplot',
                                figure={'data':[go.Scatter(x=x,y=y,mode='markers',
                                                            marker={'symbol':'pentagon'})],
                                        'layout':go.Layout(title='Scatterplot')} ),
                    dcc.Graph(id='scatterplot2',
                                figure={'data':[go.Scatter(x=x,y=y,mode='markers',
                                                            marker={'symbol':'pentagon'})],
                                        'layout':go.Layout(title='Scatterplot')} )])

if __name__=='__main__':
    app.run_server()