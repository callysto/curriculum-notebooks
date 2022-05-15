def two_slider_translation():
    import plotly.graph_objs as go
    data = []
    data.append(dict(
        visible = True,
        line=dict(color='#636EFA', width=3),
        mode = 'lines+markers+text',
        name = 'Original',
        hoverinfo = 'x+y',
        text=['A','B','C','D',''],
        textposition='top left',
        textfont=dict(color='#2CA02C'),
        x = [1, 1, 4, 4, 1],
        y = [1, 4, 4, 1, 1]))

    data.append(dict(
        visible = True,
        line=dict(color='#F1553B', width=3),
        mode = 'lines+markers+text',
        name = 'Translation',
        hoverinfo = 'x+y',
        text=['A','B','C','D',''],
        textposition='top left',
        textfont=dict(color='#2CA02C'),
        x = [1, 1, 4, 4, 1],
        y = [1, 4, 4, 1, 1]))

    steps = []
    for i in range(18):
        if((i-11) > 0):
            temp = "+" + str(i-11)
        else:
            temp = str(i-11)
        step = dict(
            method = 'restyle',  
            args = [{'x[0]':[1,-10+i],'x[1]':[1,-10+i],'x[2]':[4,-7+i],'x[3]':[4,-7+i],'x[4]':[1,-10+i]}],
            label = temp
        )
        steps.append(step)
    
    steps2 = []
    for i in range(18):
        if((i-11) > 0):
            temp = "+" + str(i-11)
        else:
            temp = str(i-11)
        step = dict(
            method = 'restyle',  
            args = [{'y[0]':[1,-7+i],'y[1]':[4,-10+i],'y[2]':[4,-10+i],'y[3]':[1,-7+i],'y[4]':[1,-7+i]}],
            label = temp
        )
        steps2.append(step)
    
    sliders = [dict(
        active = 11,
        currentvalue = {"prefix": "x axis translation: ", },
        pad = {"t": 35},
        steps = steps
    )]
    tempSlider = dict(
        active = 11,
        currentvalue = {"prefix": "y axis translation: ", },
        pad = {"t": 120},
        steps = steps2
    )
    sliders.append(tempSlider)

    layout = go.Layout(
            title = 'Translation on a Coordinate Plane',
            sliders=sliders,
            showlegend=False,
            hovermode = 'closest',
            yaxis = dict(
                title= '',
                ticklen= 5,
                dtick= 1,
                gridwidth= 2,
                range=[-10,10],
                showgrid=True,
            ),
            xaxis= dict(
                title= '',
                ticklen= 5,
                dtick=1,
                gridwidth= 2,
                range=[-10,10],
                showgrid=True,
            ),
            autosize=False,
            width=950,
            height=650,
            annotations=[
                dict(
                    x=1.0,
                    y=-0.16,
                    showarrow=False,
                    text='x axis',
                    xref='paper',
                    yref='paper',
                    font=dict(size=14),
                ),
                dict(
                    x=-0.06,
                    y=1.0,
                    showarrow=False,
                    text='y axis',
                    textangle=-90,
                    xref='paper',
                    yref='paper',
                    font=dict(size=14),
                ),
            ],
    )
    fig = go.Figure(data=data, layout=layout)
    fig.show()

def rectangle_reflection():
    import ipywidgets as widgets
    import plotly.graph_objects as go

    data3 = []
    data3.append(dict(
        visible = True,
        line=dict(color='#636EFA', width=3),
        mode = 'lines+markers+text',
        name = 'Original',
        hoverinfo = 'x+y',
        text=['A','B','C','D',''],
        textposition='top left',
        textfont=dict(color='#2CA02C'),
        x = [1, 1, 4, 4, 1],
        y = [1, 4, 4, 1, 1]))
    
    data3.append(dict(
        visible = True,
        line=dict(color='#F1553B', width=3),
        mode = 'lines+markers+text',
        name = 'Reflection',
        hoverinfo = 'x+y',
        text=['A','B','C','D',''],
        textposition='top left',
        textfont=dict(color='#2CA02C'),
        x = [1, 1, 4, 4, 1],
        y = [1, 4, 4, 1, 1]))
    
    '''
    data3.append(dict(
        visible = True,
        line=dict(color='#FF0000', width=3),
        mode = 'lines',
        name = 'reflection line',
        x = [-10, 10],
        y = [-10, 10]))
    '''

    updatemenus=list([
        dict(
            buttons=list([
                dict(
                    args=[{'x[0]': [1,1] ,'x[1]':[1,1],'x[2]':[4,4],'x[3]':[4,4],'x[4]':[1,1]}],
                    label='No Horizontal Reflection',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,5-(1-5)],'x[1]':[1,5-(1-5)],'x[2]':[4,5-(4-5)],'x[3]':[4,5-(4-5)],'x[4]':[1,5-(1-5)]}],
                    label='Reflection across x = 5',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,4-(1-4)],'x[1]':[1,4-(1-4)],'x[2]':[4,4-(4-4)],'x[3]':[4,4-(4-4)],'x[4]':[1,4-(1-4)]}],
                    label='Reflection across x = 4',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,3-(1-3)],'x[1]':[1,3-(1-3)],'x[2]':[4,3-(4-3)],'x[3]':[4,3-(4-3)],'x[4]':[1,3-(1-3)]}],
                    label='Reflection across x = 3',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,2-(1-2)],'x[1]':[1,2-(1-2)],'x[2]':[4,2-(4-2)],'x[3]':[4,2-(4-2)],'x[4]':[1,2-(1-2)]}],
                    label='Reflection across x = 2',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,1-(1-1)],'x[1]':[1,1-(1-1)],'x[2]':[4,1-(4-1)],'x[3]':[4,1-(4-1)],'x[4]':[1,1-(1-1)]}],
                    label='Reflection across x = 1',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,0-(1-0)],'x[1]':[1,0-(1-0)],'x[2]':[4,0-(4-0)],'x[3]':[4,0-(4-0)],'x[4]':[1,0-(1-0)]}],
                    label='Reflection across x = 0',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,-1-(1+1)],'x[1]':[1,-1-(1+1)],'x[2]':[4,-1-(4+1)],'x[3]':[4,-1-(4+1)],'x[4]':[1,-1-(1+1)]}],
                    label='Reflection across x = -1',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,-2-(1+2)],'x[1]':[1,-2-(1+2)],'x[2]':[4,-2-(4+2)],'x[3]':[4,-2-(4+2)],'x[4]':[1,-2-(1+2)]}],
                    label='Reflection across x = -2',
                    method='restyle'
                ),
                dict(
                    args=[{'x[0]':[1,-3-(1+3)],'x[1]':[1,-3-(1+3)],'x[2]':[4,-3-(4+3)],'x[3]':[4,-3-(4+3)],'x[4]':[1,-3-(1+3)]}],
                    label='Reflection across x = -3',
                    method='restyle'
                )           
            ]),
            showactive = True,
            x = 0.5,
            y = 1.2
        ),
        dict(
            buttons=list([
                dict(
                    args=[{'y[0]':[1,1],'y[1]':[4,4],'y[2]':[4,4],'y[3]':[1,1],'y[4]':[1,1]}],
                    label='No Vertical Reflection',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,5-(1-5)],'y[1]':[4,5-(4-5)],'y[2]':[4,5-(4-5)],'y[3]':[1,5-(1-5)],'y[4]':[1,5-(1-5)]}],
                    label='Reflection across y = 5',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,4-(1-4)],'y[1]':[4,4-(4-4)],'y[2]':[4,4-(4-4)],'y[3]':[1,4-(1-4)],'y[4]':[1,4-(1-4)]}],
                    label='Reflection across y = 4',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,3-(1-3)],'y[1]':[4,3-(4-3)],'y[2]':[4,3-(4-3)],'y[3]':[1,3-(1-3)],'y[4]':[1,3-(1-3)]}],
                    label='Reflection across y = 3',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,2-(1-2)],'y[1]':[4,2-(4-2)],'y[2]':[4,2-(4-2)],'y[3]':[1,2-(1-2)],'y[4]':[1,2-(1-2)]}],
                    label='Reflection across y = 2',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,1-(1-1)],'y[1]':[4,1-(4-1)],'y[2]':[4,1-(4-1)],'y[3]':[1,1-(1-1)],'y[4]':[1,1-(1-1)]}],
                    label='Reflection across y = 1',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,0-(1-0)],'y[1]':[4,0-(4-0)],'y[2]':[4,0-(4-0)],'y[3]':[1,0-(1-0)],'y[4]':[1,0-(1-0)]}],
                    label='Reflection across y = 0',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,-1-(1+1)],'y[1]':[4,-1-(4+1)],'y[2]':[4,-1-(4+1)],'y[3]':[1,-1-(1+1)],'y[4]':[1,-1-(1+1)]}],
                    label='Reflection across y = -1',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,-2-(1+2)],'y[1]':[4,-2-(4+2)],'y[2]':[4,-2-(4+2)],'y[3]':[1,-2-(1+2)],'y[4]':[1,-2-(1+2)]}],
                    label='Reflection across y = -2',
                    method='restyle'
                ),
                dict(
                    args=[{'y[0]':[1,-3-(1+3)],'y[1]':[4,-3-(4+3)],'y[2]':[4,-3-(4+3)],'y[3]':[1,-3-(1+3)],'y[4]':[1,-3-(1+3)]}],
                    label='Reflection across y = -3',
                    method='restyle'
                )           
            ]),
            showactive = True,
            x = 0.7,
            y = 1.2
        ),
    ])

    layout3 = go.Layout(
            title = 'Reflection on a Coordinate Plane',
            showlegend=False,
            updatemenus = updatemenus,
            hovermode = 'closest',
            yaxis = dict(
                title= '',
                ticklen= 5,
                dtick= 1,
                gridwidth= 2,
                range=[-10,10],
                showgrid=True,
            ),
            xaxis= dict(
                title= '',
                ticklen= 5,
                dtick=1,
                gridwidth= 2,
                range=[-10,10],
                showgrid=True,
            ),
            annotations=[
                dict(
                    x=1.0,
                    y=-0.16,
                    showarrow=False,
                    text='x axis',
                    xref='paper',
                    yref='paper',
                    font=dict(
                        size=14,
                    ),
                ),
                dict(
                    x=-0.06,
                    y=1.0,
                    showarrow=False,
                    text='y axis',
                    textangle=-90,
                    xref='paper',
                    yref='paper',
                    font=dict(
                        size=14,
                    ),
                ),
            ],
    )
    go.Figure(data=data3, layout=layout3).show()