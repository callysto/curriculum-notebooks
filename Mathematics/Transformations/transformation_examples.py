def reflection_example():
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




def rotation_example():
    from plotly.offline import init_notebook_mode, iplot, plot
    from ipywidgets import HBox
    import plotly.graph_objs as go
    import numpy as np
    import random
    from math import radians, cos, sin, sqrt, tan, atan
    import ipywidgets as widgets
    from IPython.display import Markdown
    from IPython.display import HTML, clear_output

    init_notebook_mode(connected=True)

    square_clicked4 = True
    triangle_clicked4 = False
    clockwise_rotation = True
    counterclockwise_rotation = False
    current_point = 0

    square_button4 = widgets.Button(
        description='Square',
        disabled=False,
        button_style='success', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Click me',
    )
    triangle_button4 = widgets.Button(
        description='Triangle',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Click me',
    )

    rotation_choice = widgets.Dropdown(
            options=[('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Point D', 4), ('Point E', 5), ('Origin', 6)],
            value=0,
            description='',
    )

    clockwise_button = widgets.Button(
        description='Clockwise',
        disabled=False,
        button_style='success', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Click me',
    )

    counterclockwise_button = widgets.Button(
        description='Counter-Clockwise',
        disabled=False,
        button_style='', # 'success', 'info', 'warning', 'danger' or ''
        tooltip='Click me',
    )

    text_widget4 = widgets.HTML("<strong>Object: </strong>")

    text2_widget4 = widgets.HTML("<strong>Rotation Direction: </strong>")

    text3_widget4 = widgets.HTML("<strong>Rotation Point: </strong>")

    choice_widget4 = widgets.HBox(children=[text_widget4, square_button4, triangle_button4])

    rotation_widget4 = widgets.HBox(children=[text2_widget4, clockwise_button, counterclockwise_button])

    point_widget4 = widgets.HBox(children=[text3_widget4, rotation_choice])

    input_widget4 = widgets.VBox(children=[choice_widget4, rotation_widget4, point_widget4])

    rotation_choice.layout.width = '150px' 

    def rotation(p):
        point = p

        data4 = []
        data4.append(dict(
            visible = True,
            line=dict(color='#00FF00', width=3),
            mode = 'lines+markers+text',
            name = 'Original',
            hoverinfo = 'x+y',
            text=['A','B','C','D',''],
            textposition='top left',
            textfont=dict(      
                color='#ff0000'
            ),
            x = [1, 1, 4, 4, 1],
            y = [1, 4, 4, 1, 1]))
        
        data4.append(dict(
            visible = True,
            line=dict(color='#00CED1', width=3),
            mode = 'lines+markers+text',
            name = 'Translation',
            hoverinfo = 'x+y',
            text=['A','B','C','D',''],
            textposition='top left',
            textfont=dict(      
                color='#ff0000'
            ),
            x = [1, 1, 4, 4, 1],
            y = [1, 4, 4, 1, 1]))
                
        temp_degrees = 0
        rotationX = 0
        rotationY = 0

        x0 = 0
        x1 = 0
        x2 = 0
        x3 = 0
        y0 = 0
        y1 = 0
        y2 = 0
        y3 = 0
        
        steps4 = []
        steps5 = []
        for i in range(37):       
            temp_degrees = radians((36-i)*10)
            if(point == 1):
                rotationX = 1
                rotationY = 1
                x0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                y0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                x2 = rotationX + cos(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                x3 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                y3 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))     
            elif(point == 2):
                rotationX = 1
                rotationY = 4    
                x0 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                y0 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                x1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                y1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(4-rotationY)**2))         
                x2 = rotationX + cos(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                x3 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                y3 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))     
            elif(point == 3):
                rotationX = 4
                rotationY = 4
                x0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                y0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                x1 = rotationX - cos(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                y1 = rotationY - sin(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                x3 = rotationX + cos(temp_degrees-1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                y3 = rotationY + sin(temp_degrees-1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2)) 
            elif(point == 4):
                rotationX = 4
                rotationY = 1
                x0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                y0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                x1 = rotationX - cos(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                y1 = rotationY - sin(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                x2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(4-rotationY)**2))            
                x3 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                y3 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2))      
            elif(point == 5):
                rotationX = (4-1)/2 + 1
                rotationY = (4-1)/2 + 1
                x0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                y0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                x1 = rotationX - cos(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))  
                y1 = rotationY - sin(temp_degrees+atan((4-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(4-rotationY)**2))
                x2 = rotationX + cos(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+atan((4-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(4-rotationY)**2))
                x3 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                y3 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
            elif(point == 6):
                rotationX = 0
                rotationY = 0
                tempX = rotationX + cos(temp_degrees+atan((2.5-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(2.5-rotationY)**2))
                tempY = rotationY + sin(temp_degrees+atan((2.5-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(2.5-rotationY)**2))
                x0T = tempX - 1.5
                y0T = tempY - 1.5
                x1T = tempX - 1.5
                y1T = tempY + 1.5
                x2T = tempX + 1.5
                y2T = tempY + 1.5
                x3T = tempX + 1.5
                y3T = tempY - 1.5
                rotationX = tempX
                rotationY = tempY
                x0 = rotationX - cos(temp_degrees+atan((y0T-rotationY)/(x0T-rotationX)))*(sqrt((x0T-rotationX)**2+(y0T-rotationY)**2))
                y0 = rotationY - sin(temp_degrees+atan((y0T-rotationY)/(x0T-rotationX)))*(sqrt((x0T-rotationX)**2+(y0T-rotationY)**2))
                x1 = rotationX - cos(temp_degrees+atan((y1T-rotationY)/(x1T-rotationX)))*(sqrt((x1T-rotationX)**2+(y1T-rotationY)**2))  
                y1 = rotationY - sin(temp_degrees+atan((y1T-rotationY)/(x1T-rotationX)))*(sqrt((x1T-rotationX)**2+(y1T-rotationY)**2))
                x2 = rotationX + cos(temp_degrees+atan((y2T-rotationY)/(x2T-rotationX)))*(sqrt((x2T-rotationX)**2+(y2T-rotationY)**2))
                y2 = rotationY + sin(temp_degrees+atan((y2T-rotationY)/(x2T-rotationX)))*(sqrt((x2T-rotationX)**2+(y2T-rotationY)**2))
                x3 = rotationX + cos(temp_degrees+atan((y3T-rotationY)/(x3T-rotationX)))*(sqrt((x3T-rotationX)**2+(y3T-rotationY)**2))
                y3 = rotationY + sin(temp_degrees+atan((y3T-rotationY)/(x3T-rotationX)))*(sqrt((x3T-rotationX)**2+(y3T-rotationY)**2))
            
            step = dict(
                method = 'update',  
                args = [{'x[0]':[1,x0],'x[1]':[1,x1],'x[2]':[4,x2],'x[3]':[4,x3],'x[4]':[1,x0],'y[0]':[1,y0],'y[1]':[4,y1],'y[2]':[4,y2],'y[3]':[1,y3],'y[4]':[1,y0]}],      
                label = str(i*10) + "&deg;"
            )
            steps4.append(step)
    
            step2 = dict(
                method = 'update',  
                args = [{'x[0]':[1,x0],'x[1]':[1,x1],'x[2]':[4,x2],'x[3]':[4,x3],'x[4]':[1,x0],'y[0]':[1,y0],'y[1]':[4,y1],'y[2]':[4,y2],'y[3]':[1,y3],'y[4]':[1,y0]}],        
                label = str((36-i)*10) + "&deg;"
            )
            steps5.insert(0,step2)
        
        if(clockwise_rotation):
            sliders4 = [dict(
                active = 0,
                currentvalue = {"prefix": "Clockwise Rotation: ", },
                pad = {"t": 35},
                steps = steps4
            )]
        else:
            sliders4 = [dict(
                active = 0,
                currentvalue = {"prefix": "Counter-Clockwise Rotation: ", },
                pad = {"t": 35},
                steps = steps5
            )]

        title = ''
        if(point == 1):
            title = 'Rotation about Point A'
        elif(point == 2):
            title = 'Rotation about Point B'
        elif(point == 3):
            title = 'Rotation about Point C'
        elif(point == 4):
            title = 'Rotation about Point D'
        elif(point == 5):
            title = 'Rotation about Point E'
        elif(point == 6):
            title = 'Rotation about the Origin'
            
        layout4 = go.Layout(
                title = title,
                sliders=sliders4,
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
                autosize=True,
                #width=750,
                height=725,
                annotations=[
                    dict(
                        x=1.0,
                        y=-0.10,
                        showarrow=False,
                        text='X Axis',
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
                        text='Y Axis',
                        textangle=-90,
                        xref='paper',
                        yref='paper',
                        font=dict(
                            size=14,
                        ),
                    ),
                ],
        )

        fig4 = dict(data=data4, layout=layout4)

        
        if(not(point == 0)):
            clear_output()
            display(Markdown("<img src='images/pointplot2.png' align='left'>"))
            display(input_widget4)
            iplot(fig4, filename = 'filename')
            
    
    def rotationT(p):
        pointT = p   

        dataT4 = []
        dataT4.append(dict(
            visible = True,
            line=dict(color='#00FF00', width=3),
            mode = 'lines+markers+text',
            name = 'Original',
            hoverinfo = 'x+y',
            text=['A','B','C',''],
            textposition='top left',
            textfont=dict(      
                color='#ff0000'
            ),
            x = [1, 2.5, 4, 1],
            y = [1, 4, 1, 1]))

        dataT4.append(dict(
            visible = True,
            line=dict(color='#00CED1', width=3),
            mode = 'lines+markers+text',
            name = 'Rotation',
            hoverinfo = 'x+y',
            text=['A','B','C',''],
            textposition='top left',
            textfont=dict(      
                color='#ff0000'
            ),
            x = [1, 2.5, 4, 1],
            y = [1, 4, 1, 1]))

        temp_degrees = 0
        rotationX = 0
        rotationY = 0
        
        xT0 = 0
        xT1 = 0
        xT2 = 0
        yT0 = 0
        yT1 = 0
        yT2 = 0
        
        stepsT4 = []
        stepsT5 = []
        for i in range(37):       
            temp_degrees = radians((36-i)*10)
            if(pointT == 1):
                rotationX = 1
                rotationY = 1
                xT0 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                yT0 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                xT1 = rotationX + cos(temp_degrees+atan((4-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                yT1 = rotationY + sin(temp_degrees+atan((4-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                xT2 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                yT2 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))     
            elif(pointT == 2):
                rotationX = 2.5
                rotationY = 4    
                xT0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                yT0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                xT1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                yT1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))         
                xT2 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                yT2 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))     
            elif(pointT == 3):
                rotationX = 4
                rotationY = 1
                xT0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                yT0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                xT1 = rotationX - cos(temp_degrees+atan((4-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                yT1 = rotationY - sin(temp_degrees+atan((4-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                xT2 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                yT2 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((4-rotationX)**2+(1-rotationY)**2))      
            elif(pointT == 4):
                rotationX = (4-1)/2 + 1
                rotationY = (4-1)/2 + 1
                xT0 = rotationX - cos(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                yT0 = rotationY - sin(temp_degrees+atan((1-rotationY)/(1-rotationX)))*(sqrt((1-rotationX)**2+(1-rotationY)**2))
                xT1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                yT1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((2.5-rotationX)**2+(4-rotationY)**2))
                xT2 = rotationX + cos(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
                yT2 = rotationY + sin(temp_degrees+atan((1-rotationY)/(4-rotationX)))*(sqrt((4-rotationX)**2+(1-rotationY)**2))
            elif(pointT == 5):
                rotationX = 0
                rotationY = 0
                tempTX = rotationX + cos(temp_degrees+atan((2.5-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(2.5-rotationY)**2))
                tempTY = rotationY + sin(temp_degrees+atan((2.5-rotationY)/(2.5-rotationX)))*(sqrt((2.5-rotationX)**2+(2.5-rotationY)**2))
                xT0T = tempTX - 1.5
                yT0T = tempTY - 1.5
                xT1T = tempTX
                yT1T = tempTY + 1.5
                xT2T = tempTX + 1.5
                yT2T = tempTY - 1.5
                rotationX = tempTX
                rotationY = tempTY
                xT0 = rotationX - cos(temp_degrees+atan((yT0T-rotationY)/(xT0T-rotationX)))*(sqrt((xT0T-rotationX)**2+(yT0T-rotationY)**2))
                yT0 = rotationY - sin(temp_degrees+atan((yT0T-rotationY)/(xT0T-rotationX)))*(sqrt((xT0T-rotationX)**2+(yT0T-rotationY)**2))
                xT1 = rotationX + cos(temp_degrees+1.5707963268)*(sqrt((xT1T-rotationX)**2+(yT1T-rotationY)**2))
                yT1 = rotationY + sin(temp_degrees+1.5707963268)*(sqrt((xT1T-rotationX)**2+(yT1T-rotationY)**2))
                xT2 = rotationX + cos(temp_degrees+atan((yT2T-rotationY)/(xT2T-rotationX)))*(sqrt((xT2T-rotationX)**2+(yT2T-rotationY)**2))
                yT2 = rotationY + sin(temp_degrees+atan((yT2T-rotationY)/(xT2T-rotationX)))*(sqrt((xT2T-rotationX)**2+(yT2T-rotationY)**2))
        
            step = dict(
                method = 'update',  
                args = [{'x[0]':[1,xT0],'x[1]':[2.5,xT1],'x[2]':[4,xT2],'x[3]':[1,xT0],'y[0]':[1,yT0],'y[1]':[4,yT1],'y[2]':[1,yT2],'y[3]':[1,yT0]}],      
                label = str(i*10) + "&deg;"
            )
            stepsT4.append(step)
    
            step2 = dict(
                method = 'update',  
                args = [{'x[0]':[1,xT0],'x[1]':[2.5,xT1],'x[2]':[4,xT2],'x[3]':[1,xT0],'y[0]':[1,yT0],'y[1]':[4,yT1],'y[2]':[1,yT2],'y[3]':[1,yT0]}],        
                label = str((36-i)*10) + "&deg;"
            )
            stepsT5.insert(0,step2)
        
        if(clockwise_rotation):    
            slidersT4 = [dict(
                active = 0,
                currentvalue = {"prefix": "Clockwise Rotation: ", },
                pad = {"t": 35},
                steps = stepsT4
            )]
        else:
            slidersT4 = [dict(
                active = 0,
                currentvalue = {"prefix": "Counter-Clockwise Rotation: ", },
                pad = {"t": 35},
                steps = stepsT5
            )]


        title = ''
        if(pointT == 1):
            title = 'Rotation about Point A'
        elif(pointT == 2):
            title = 'Rotation about Point B'
        elif(pointT == 3):
            title = 'Rotation about Point C'
        elif(pointT == 4):
            title = 'Rotation about Point D'
        elif(pointT == 5):
            title = 'Rotation about the Origin'
        
        layoutT4 = go.Layout(
                title = title,
                sliders=slidersT4,
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
                autosize=True,
                #width=750,
                height=725,
                annotations=[
                    dict(
                        x=1.0,
                        y=-0.10,
                        showarrow=False,
                        text='X Axis',
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
                        text='Y Axis',
                        textangle=-90,
                        xref='paper',
                        yref='paper',
                        font=dict(
                            size=14,
                        ),
                    ),
                ],
        )
        
        figT4 = dict(data=dataT4, layout=layoutT4)
        
        if(not(pointT == 0)):
            clear_output()
            display(Markdown("<img src='images/pointplot4.png' align='left'>"))
            display(input_widget4)
            iplot(figT4, filename = 'filename')
    

    def graph_rotation(change):
        global current_point
        
        current_point = change.new
        
        if(square_clicked4):
            rotation(change.new)
        elif(triangle_clicked4):
            rotationT(change.new)
        
        
    def square_update4(change):
        global square_clicked4
        global triangle_clicked4
        
        if(not(square_clicked4)):
            square_clicked4 = True
            triangle_clicked4 = False
            square_button4.button_style = 'success'
            triangle_button4.button_style = ''
            rotation_choice.options = [('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Point D', 4), ('Point E', 5), ('Origin', 6)]
            rotation_choice.value = 0
            clear_output()
            display(Markdown("<img src='images/pointplot2.png' align='left'>"))
            display(input_widget4)
        
    def triangle_update4(change):
        global square_clicked4
        global triangle_clicked4

        if(not(triangle_clicked4)):
            triangle_clicked4 = True
            square_clicked4 = False
            square_button4.button_style = ''
            triangle_button4.button_style = 'success'
            rotation_choice.options = options=[('',0),('Point A', 1), ('Point B', 2), ('Point C', 3), ('Point D', 4), ('Origin', 5)]
            rotation_choice.value = 0
            clear_output()
            display(Markdown("<img src='images/pointplot4.png' align='left'>"))
            display(input_widget4)

    def clockwise_update(change):
        global clockwise_rotation
        global counterclockwise_rotation
        global current_point
        
        if(not(clockwise_rotation)):
            clockwise_rotation = True
            counterclockwise_rotation = False
            clockwise_button.button_style = "success"
            counterclockwise_button.button_style = ""
            clear_output()
            if(square_clicked4):
                display(Markdown("<img src='images/pointplot2.png' align='left'>"))
                if(current_point == 0):
                    display(input_widget4)
                rotation(current_point)
            else:
                display(Markdown("<img src='images/pointplot4.png' align='left'>"))
                if(current_point == 0):
                    display(input_widget4)
                rotationT(current_point)
            
        
    def counterclockwise_update(change):
        global clockwise_rotation
        global counterclockwise_rotation
        global current_point
        
        if(not(counterclockwise_rotation)):
            clockwise_rotation = False
            counterclockwise_rotation = True
            clockwise_button.button_style = ""
            counterclockwise_button.button_style = "success"
            clear_output()
            if(square_clicked4):
                display(Markdown("<img src='images/pointplot2.png' align='left'>"))
                if(current_point == 0):
                    display(input_widget4)
                rotation(current_point)
            else:
                display(Markdown("<img src='images/pointplot4.png' align='left'>"))
                if(current_point == 0):
                    display(input_widget4)
                rotationT(current_point)
            
    square_button4.on_click(square_update4)

    triangle_button4.on_click(triangle_update4)

    clockwise_button.on_click(clockwise_update)

    counterclockwise_button.on_click(counterclockwise_update)

    rotation_choice.observe(graph_rotation, names='value')

    display(Markdown("<img src='images/pointplot2.png' align='left'>"))
    display(input_widget4)

    rotation(0)