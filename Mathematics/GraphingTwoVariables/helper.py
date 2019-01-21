import matplotlib.pyplot as plt
import plotly as py
import plotly.graph_objs as go
import numpy as np
import math
import ipywidgets as widgets
from astropy.table import Table, Column
from ipywidgets import interact, interactive, Layout
from IPython.display import display, Math, Latex, HTML

py.offline.init_notebook_mode(connected=True)

font = {'family' : 'sans-serif',
        'weight' : 'normal',
        'size'   : 14}

plt.rc('font', **font)


#code for User_Graph

class User_Graph:
    
    def __init__(self,x_dim,y_dim):
        
        #dimensions of the graph
        self.x_dim = x_dim
        self.y_dim = y_dim
        
        #create lists for x and y
        self.x_list = []
        self.y_list = []
       # self.title=" "
        
    
    def user_input(self):
           #ask users to input data points
            
           # provide a title
           # print('Give the graph a title:')
           # text_title = widgets.Text()
           # display(text_title)
            
            #get x values
            print('Enter the x-values as a list of the form [a,b,c,d,...]: ')
            text_x = widgets.Text()
            display(text_x)
            
            print('Enter the y-values as a list of the form [a,b,c,d,...]: ')
            text_y = widgets.Text()
            display(text_y)
            
            #get y values
            text_warning = widgets.HTML()
            
            def generate_data(button):
                text_warning.value=""
               # self.title=text_title.value
                data_is_correct=True
                try:
                    x_list = text_x.value
                    x_list = x_list.strip(']')
                    x_list = x_list.strip('[')
                    x_list = x_list.split(',')
                    for i in x_list:
                        j=i.replace(' ','')
                        x_val = float(j)
                        if x_val > self.x_dim[1] or x_val <self.x_dim[0]:
                            print("Note: this value of x: ", x_val, " is outside plot dimentions")
                        self.x_list.append(x_val)
                   
                    y_list = text_y.value
                    y_list = y_list.strip(']')
                    y_list = y_list.strip('[')
                    y_list = y_list.split(',')
                    for i in y_list:
                        j=i.replace(' ','')
                        y_val = float(j)
                        if y_val > self.y_dim[1] or y_val <self.y_dim[0]:
                            print("Note: this value of y: ", y_val, " is outside plot dimentions")
                        self.y_list.append(y_val)

                except:
                    text_warning.value="Entries must be real numbers! Try Again."
                    data_is_correct=False

                if len(self.x_list) != len(self.y_list):
                    text_warning.value="Must have an equal number of x and y values! Try Again."
                    data_is_correct=False
                
                if (data_is_correct):
                    button.disabled=True
                    self.make_graph()
                else:
                    self.x_list=[]
                    self.y_list=[]
                    text_x.value=""
                    text_y.value=""
                                 
            btn=widgets.Button(description='Generate plot')
            display(btn)
            btn.on_click(generate_data)    
            
            display(text_warning)
           
              
    def make_graph(self):
        #make a graph out of the available data points
        layout1 = go.Layout(
          #  title = self.title,
            yaxis = dict(
                title="Y Values",
                range = [self.y_dim[0], self.y_dim[1]]
            ),
            xaxis = dict(
                title="X Values",
                range = [self.x_dim[0], self.x_dim[1]]
            ),
        )

        trace = go.Scatter(
            x = self.x_list,
            y = self.y_list,
            mode = "lines+markers",
            name = "extend plot",
            line=dict(
                color = ('rgb(22, 96, 167)'),
                shape = "spline",
                dash = "dot"
            ) 
        )

        fig1 = go.Figure(data = [trace], layout = layout1)
        py.offline.iplot(fig1)
   
        
    def run_it(self):
        self.user_input()

            

#code for Double_Graph

class Double_Graph:
    
    def __init__(self, y_dim, x_dim):
        
        #dimensions of the graph
        self.x_dim = x_dim
        self.y_dim = y_dim
       
        #create lists for x and y
        self.x1_list = []
        self.y1_list = []
        self.x2_list = []
        self.y2_list = []
       
    def user_input(self):
           #ask users to input data points
            
            print("Please enter data points for Quentin:")
            
            #get x values
            print('Enter the x-values as a list of the form [a,b,c,d,...]: ')
            text_x1 = widgets.Text()
            display(text_x1)
            
            #get y values
            print('Enter the y-values as a list of the form [a,b,c,d,...]: ')
            text_y1 = widgets.Text()
            display(text_y1)
            
            print("Please enter data points for Isabelle:")
            
            #get x values
            print('Enter the x-values as a list of the form [a,b,c,d,...]: ')
            text_x2 = widgets.Text()
            display(text_x2)
            
            #get y values
            print('Enter the y-values as a list of the form [a,b,c,d,...]: ')
            text_y2 = widgets.Text()
            display(text_y2)
                      
            text_warning = widgets.HTML()
            def generate_data(button):
                text_warning.value=""
               # self.title=text_title.value
                data_is_correct=True
                try:
                    x1_list = text_x1.value
                    x1_list = x1_list.strip(']')
                    x1_list = x1_list.strip('[')
                    x1_list = x1_list.split(',')
                    for i in x1_list:
                        j=i.replace(' ','')
                        x_val = float(j)
                        if x_val > self.x_dim[1] or x_val <self.x_dim[0]:
                            print("Note: this value of x: ", x_val, " is outside plot dimentions")
                        self.x1_list.append(x_val)
                   
                    y1_list = text_y1.value
                    y1_list = y1_list.strip(']')
                    y1_list = y1_list.strip('[')
                    y1_list = y1_list.split(',')
                    for i in y1_list:
                        j=i.replace(' ','')
                        y_val = float(j)
                        if y_val > self.y_dim[1] or y_val <self.y_dim[0]:
                            print("Note: this value of y: ", y_val, " is outside plot dimentions")
                        self.y1_list.append(y_val)
                except:
                    text_warning.value="Entries must be real numbers! Try Again."
                    data_is_correct=False
                    text_x1.value=""
                    text_y1.value=""

                if len(self.x1_list) != len(self.y1_list):
                    text_warning.value="Must have an equal number of x and y values! Try Again."
                    data_is_correct=False
                    text_x1.value=""
                    text_y1.value=""
                    
                try:
                    x2_list = text_x2.value
                    x2_list = x2_list.strip(']')
                    x2_list = x2_list.strip('[')
                    x2_list = x2_list.split(',')
                    for i in x2_list:
                        j=i.replace(' ','')
                        x_val = float(j)
                        if x_val > self.x_dim[1] or x_val <self.x_dim[0]:
                            print("Note: this value of x: ", x_val, " is outside plot dimentions")
                        self.x2_list.append(x_val)
                   
                    y2_list = text_y2.value
                    y2_list = y2_list.strip(']')
                    y2_list = y2_list.strip('[')
                    y2_list = y2_list.split(',')
                    for i in y2_list:
                        j=i.replace(' ','')
                        y_val = float(j)
                        if y_val > self.y_dim[1] or y_val <self.y_dim[0]:
                            print("Note: this value of y: ", y_val, " is outside plot dimentions")
                        self.y2_list.append(y_val)
                except:
                    text_warning.value="Entries must be real numbers! Try Again."
                    data_is_correct=False
                    text_x2.value=""
                    text_y2.value=""

                if len(self.x2_list) != len(self.y2_list):
                    text_warning.value="Must have an equal number of x and y values! Try Again."
                    data_is_correct=False
                    text_x2.value=""
                    text_y2.value=""    
                
                if (data_is_correct):
                    button.disabled=True
                    self.make_graph()
                else:
                    self.x1_list=[]
                    self.y1_list=[]
                    self.x2_list=[]
                    self.y2_list=[]
              
                                                 
            btn=widgets.Button(description='Generate plot')
            display(btn)
            btn.on_click(generate_data)    
            
            display(text_warning)
             
    def make_graph(self):
        #make a graph out of the available data points
        
        layout = go.Layout(
           # title = title,
            yaxis = dict(
                title="Y Values",
                range = [self.y_dim[0], self.y_dim[1]]
            ),
            xaxis = dict(
                title="X Values",
                range = [self.x_dim[0], self.x_dim[1]]
            ),
        )

        trace1 = go.Scatter(
            x = self.x1_list,
            y = self.y1_list,
            mode = "lines+markers",
            name = "Quentin",
            line=dict(
                color = ('rgb(22, 96, 167)'),
                dash = "dot"
            )
        )
        
        trace2 = go.Scatter(
            x = self.x2_list,
            y = self.y2_list,
            mode = "lines+markers",
            name = "Isabelle",
            line=dict(
                color = ('rgb(205, 12, 24)'),
                dash = "dot"
            )
        )
        fig = go.Figure(data = [trace1,trace2], layout = layout)
        py.offline.iplot(fig)
        
    def run_it(self):
        self.user_input()
        #self.function_2()
       # self.make_graph(title)

def check_input_numbers():
    print("The equation is: y = 3x + 2") 
    y_correct=[5,8,11,14,17]
    style = {'description_width': 'initial'}
    ans1=widgets.IntText(description="When x = 1, y = ",style=style,value=5)
    display(ans1)
    ans2=widgets.IntText(description="When x = 2, y = ",style=style)
    display(ans2)
    ans3=widgets.IntText(description="When x = 3, y = ",style=style)
    display(ans3)
    ans4=widgets.IntText(description="When x = 4, y = ",style=style)
    display(ans4)
    ans5=widgets.IntText(description="When x = 5, y = ",style=style)
    display(ans5)

    text_warning = widgets.HTML()  

    def check_results(change):
        y_entered=[]
        y_entered.append(ans1.value)
        y_entered.append(ans2.value)
        y_entered.append(ans3.value)
        y_entered.append(ans4.value)
        y_entered.append(ans5.value)
        if set(y_entered) == set(y_correct):
                text_warning.value="Correct!"
        else:
                text_warning.value="Incorrect, try again!"

    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 
    
def ask_slope():
    print("What is the value of the slope of the above graph?") 
    ans1=widgets.IntText()
    display(ans1)

    text_warning = widgets.HTML()  

    def check_results(change):
        if ans1.value ==-2 :
                text_warning.value="Good stuff!"
        else:
                text_warning.value="Try Again! Remember, the equation for the slope of a line is: Slope = (y2 - y1)/(x2 - x1)"

    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 
    
def ask_equation():
    print("What is the equation of the linear function shown on the graph? (Enter your answer as: y = mx + b)")
    ans1=widgets.Text()
    display(ans1)

    text_warning = widgets.HTML() 
    def check_results(change):
        if ans1.value in ["y = -2x + 10", "y = -(2)x + 10", "y = (-2)x + 10", "y=-2x+10"]:
            text_warning.value="Good job!"
        else:
            text_warning.value="Try Again! Hint: Remeber that slope = m, and the y intercept = b "
            #display(Latex("Hint: Remeber that slope = $m$, and the $y$ intercept = $b$"))
    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 

def ask_question1():
    print("At what point did the person walk past their destination? (Enter your answer as (x,y)) ")
    ans1=widgets.Text()
    display(ans1)
    
    text_warning = widgets.HTML()
    def check_results(change):
        if ans1.value in ["(5,0)"]:
            text_warning.value="Way to go!"
        else:
            text_warning.value="Try Again! Hint: At what point is the person 0 meters away from their destination, but then keeps going?"
       # display(Latex("Hint: At what point is the person 0 meters away from their destination, but then keeps going?"))
    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 
    
def ask_question2():
    print("At what distance do Quentin and Isabelle make the same amount of money? (Enter your answer as a whole number) ")
    ans1=widgets.IntText()
    display(ans1)
    
    text_warning = widgets.HTML()
    def check_results(change):
        if ans1.value ==6:
            text_warning.value="You got it!"
        else:
            text_warning.value="Try Again! Hint: What is the x coordinate where the two functions cross?"
            #display(Latex("Hint: What is the $x$ coordinate where the two functions cross?"))
    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 
    
def ask_question3():
    print("Who makes the most money after running 10 kilometers? (Enter: Quentin, or Isabelle) ")
    ans1=widgets.Text()
    display(ans1)
    
    text_warning = widgets.HTML()
    def check_results(change):
        if ans1.value in ["Isabelle"]:
            text_warning.value="Nice work!"
        else:
            text_warning.value="Try Again! Hint: Who has the highest y value when x = 10?"
        #display(Latex("Hint: Who has the highest $y$ value when $x = 10$?"))
    
    btn=widgets.Button(description='Check results')
    display(btn)
    btn.on_click(check_results)      
    display(text_warning) 
    
def lin_or_non1(val):
    if val == "Linear":
        display(Latex("Correct!"))
        display(Latex("This equation has no exponent on either variable, and is therefore linear."))
    elif val == "Non-Linear":
        display(Latex("Try Again!"))

def lin_or_non2(val):
    if val == "Linear":
        display(Latex("Try Again!"))
    elif val == "Non-Linear":
        display(Latex("Right on!"))
        display(Latex("Because $x$ is raised to the power of 2, this function is not linear."))


def lin_or_non3(val):
    if val == "Linear":
        display(Latex("Try Again!"))
    elif val == "Non-Linear":
        display(Latex("Way to go!"))
        display(Latex("This graph does not resemble a straight line, therefore, it is not linear."))
        display(Latex("The equation for this function is:"))
        display(Math("y = x^2"))

        
def lin_or_non4(val):
    if val == "Linear":
        display(Latex("Good job!"))
        display(Latex("This graph is a straight line, and is therefore linear."))
        display(Latex("The equation for this function is:"))
        display(Math("y = -x - 6"))
    elif val == "Non-Linear":
        display(Latex("Try Again!"))
        
def wage(val):
    if val == "W (Wage)":
        display(Latex("Correct!"))
        display(Latex("The amount of money you make depends on your wage, and your wage is free to change. It is therefore the independent variable."))
    elif val == "M (Money Made)":
        display(Latex("Try Again!"))
    
        
        
        

## Above, we are importing all the necessary modules in order to run the notebook. 
## Numpy allows us to define arrays of values for our variables to plot them
## matplotlib is what we use to create the figures
## the display and widgets are to make the notebook look neat
