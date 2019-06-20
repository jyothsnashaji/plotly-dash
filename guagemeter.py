from plotly import tools
import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
import math
layout = go.Layout(images=[dict(
        source="https://upload.wikimedia.org/wikipedia/commons/thumb/6/64/Cisco_logo.svg/1280px-Cisco_logo.svg.png",
        xref="paper", yref="paper",
        x=1, y=1.05,
        sizex=0.2, sizey=0.2,
        xanchor="right", yanchor="bottom"
      )])

fig = tools.make_subplots(rows=2, cols=2, subplot_titles=('Router Health', 'HW Health',
                                                          'SW Health', 'N/W Health'))

base_chart = {
    "values": [40, 10, 10, 10],
    "domain": {"x": [0, .48]},
    "marker": {
        "colors": [
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)',
            'rgb(255, 255, 255)'
        ],
        "line": {
            "width": 1
        }
    },
    "name": "Gauge",
    "hole": .4,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 108,
    "showlegend": False,
    "hoverinfo": "none",
    "textinfo": "label",
    "textposition": "outside"
}
        
meter_chart_1 = {
    "values": [50,18,16,16],
    "labels": ["Router health", "Normal", "Warning", "Critical"],
    "marker": {
        'colors': [
            'rgb(255,255,255)',
            'rgb(191, 255, 0)',
            'rgb(255, 255, 0)',
            'rgb(255, 0, 0)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}
    
meter_chart_2 = {
    "values": [50, 10, 10, 10],
    "labels": ["H/W health", "Normal", "Warning", "Critical"],
    "marker": {
        'colors': [
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}
    
meter_chart_3 = {
    "values": [50, 10, 10, 10],
    "labels": ["S/W health", "Normal", "Warning", "Critical"],
    "marker": {
        'colors': [
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}
    
meter_chart_4 = {
   "values": [50, 10, 10, 10],
    "labels": ["N/W Health", "Normal", "Warning", "Critical"],
    "marker": {
        'colors': [
            'rgb(255, 255, 255)',
            'rgb(232,226,202)',
            'rgb(223,162,103)',
            'rgb(226,126,64)'
        ]
    },
    "domain": {"x": [0, 0.48]},
    "name": "Gauge",
    "hole": .3,
    "type": "pie",
    "direction": "clockwise",
    "rotation": 90,
    "showlegend": False,
    "textinfo": "label",
    "textposition": "inside",
    "hoverinfo": "none"
}

score=df[param].mean()

xco=0.24-0.15*math.cos(math.radians(1.8*score))
yco=0.5+0.15*math.sin(math.radians(1.8*score))

layout = {
    'xaxis1': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis1': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'xaxis2': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis2': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'xaxis3': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis3': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'xaxis4': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'yaxis4': {
        'showticklabels': False,
        'showgrid': False,
        'zeroline': False,
    },
    'shapes': [
        {
            'type': 'path',
            #'path': 'M 0.239 0.5 L 0.19 0.5 L 0.241 0.5 C Z',
            'path':'M 0.239 0.5 L '+str(xco) +' '+str(yco) +' L 0.241 0.5 C Z',
            'fillcolor': 'rgba(0,0,0)',
            'line': {
                'width': 0.5
            },
            'xref': 'paper',
            'yref': 'paper'
        }
    ],
    'annotations': [
        {
            'xref': 'paper',
            'yref': 'paper',
            'x': 0.23,
            'y': 0.45,
            'text': '50',
            'showarrow': False
        }
    ]
}


# we don't want the boundary now
base_chart['marker']['line']['width'] = 0


fig = {"data": [base_chart, meter_chart_1],
       "layout": layout}
pyo.plot(fig, filename='guage-meter.html')
