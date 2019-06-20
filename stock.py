import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader.famafrench import get_available_datasets
from dash.dependencies import State,Output,Input
import datetime
import plotly.graph_objs as go


app=dash.Dash()
df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\NASDAQcompanylist.csv')
df.set_index('Symbol',inplace=True)
options=[]
for val in df.index:
    options.append({'label':val,'value':val})


app.layout=html.Div([
            html.Div([
                html.H1(children="Stock Dashboard",style={'textAlign':'center'})]),
            html.Div([
                dcc.Dropdown(id='dropdown',options=options,multi=True,placeholder="Select Source(s)")
             ],style={'float':'left','display':'inline-block','width':'48%','paddingTop':'20px'}),
            html.Div([
                dcc.DatePickerRange(id='date',display_format="MMMM,YY",end_date=datetime.datetime.now().date(),minimum_nights=60)
            ],style={'display':'inline-block','width':'48%','paddingTop':'20px','float':'right'}),
            html.Div([
                html.Button(id='button',n_clicks=0,children='Submit')
            ],style={'textAlign':'center'}),
            html.Div([
                dcc.Graph(id='graph')
            ],style={'paddingTop':'100px'})
    
])


@app.callback(Output('graph','figure'),[Input('button','n_clicks')],
                                        [State('dropdown','value'),
                                        State('date','start_date'),
                                        State('date','end_date')])
def update_graph(n_clicks,values,start_date,end_date):
    traces=[]
    for value in values:
        df1=web.DataReader(name=value,data_source='google',start=start_date,end=end_date)
        traces.append(go.Scatter(x=df1.index,y=df1['close'],mode='lines'))

    figure={'data':traces,'layout':go.Layout()}
    return figure

if __name__ == "__main__":
    app.run_server()
