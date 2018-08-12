# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 13:12:32 2018

@author: Owner
"""
"Functions for CC-47 root finding algorithms"


# function to graph third order polynomial with given inputs

import numpy as np
import plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected = True)

def plot3(a,b,c,d):
    x = np.linspace(-50,50,1000)
    y = a*x**3 + d*x**2 + c*x + d   
    trace = go.Scatter(
        x = x,
        y = y
    )
    layout = go.Layout(
        xaxis = dict(
            title='x',
            titlefont=dict(
            family='Arial, serif',
            size=18,
            color='black'),
            showticklabels=True,
            tickangle=0,
            range = [-15,15],
            autotick=False,
            ticks='outside',
            tick0=0,
            dtick=1
        ),
        yaxis = dict(
            title='P(x)',
            titlefont=dict(
            family='Arial, serif',
            size=18,
            color='black'),
            range = [-15,15],
            autotick=False,
            ticks='outside',
            tick0=0,
            dtick=1
        ),
    )

    data = [trace]

    fig = go.Figure(data=data, layout=layout)

    iplot(fig)

    return 
        
