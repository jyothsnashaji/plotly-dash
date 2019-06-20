import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
df=pd.read_csv('plotly\\Plotly-Dashboards-with-Dash-master\\Data\\OldFaithful.csv')
app= dash.Dash()

app.layout=html.Div([dcc.Graph(id='plot',figure={'data':[go.Scatter(x=df['X'],y=df['Y'],mode='markers')]})])




if __name__ == "__main__":
    app.run_server()
