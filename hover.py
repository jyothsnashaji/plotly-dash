import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json
import base64
def encode_image(img_file):
    encoded=base64.b64encode(open(img_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app=dash.Dash()

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\wheels.csv')

app.layout=html.Div([
                html.Div(dcc.Graph(id='wheels-plot',figure={'data':[go.Scatter(x=df['color'],y=df['wheels'],mode='markers')],'layout':go.Layout(hovermode='closest')})),
                html.Div(html.Img(id='hoverdata',src='children'))
])

@app.callback(Output('hoverdata','src'),[Input('wheels-plot','hoverData')]) #or clickData
def callback_image(hoverData):
    wheel=hoverData['points'][0]['y']
    color=hoverData['points'][0]['x'] 
    path='plotly\Plotly-Dashboards-with-Dash-master\Data\Images\\'
    return encode_image(path+df[(df['wheels']==wheel)& (df['color']==color)]['image'].values[0])

if __name__ == "__main__":
    app.run_server()