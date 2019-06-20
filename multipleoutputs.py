import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\wheels.csv')

app=dash.Dash()


def encode_image(img_file):
    encoded=base64.b64encode(open(img_file,'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout=html.Div([
    dcc.RadioItems(id='wheels',
                    options=[{'label':i,'value':i}for i in df['wheels'].unique()],
                    value=1),
    html.Div(id='wheels_output'),
    html.Hr(),
    dcc.RadioItems(id='colors',
                     options=[{'label':i,'value':i}for i in df['color'].unique()],
                     value='blue'),
 
    html.Div(id='colors_output'),
    html.Img(id='img',src='children',height=300)

])

@app.callback(Output('wheels_output','children'),[Input('wheels','value')])
def callback_wheel(wheelsval):
    return "you choose {}".format(wheelsval)

@app.callback(Output('colors_output','children'),[Input('colors','value')])

def callback_colors(colorsval):
    return "you choose {}".format(colorsval)

@app.callback(Output('img','src'),
            [Input('wheels','value'),Input('colors','value')])
def callback_image(wheel,color):
    path='plotly\Plotly-Dashboards-with-Dash-master\Data\Images\\'
    return encode_image(path+df[(df['wheels']==wheel)& (df['color']==color)]['image'].values[0])

if __name__ == "__main__":
    app.run_server()