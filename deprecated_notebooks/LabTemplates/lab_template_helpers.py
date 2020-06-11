import pandas as pd
import numpy as np
import qgrid
from ipywidgets import interactive, HBox, VBox

# Prevents namespace conflict with plotly.
from ipywidgets import Layout as widg_layout

import ipywidgets as widgets
from IPython import display
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *


class easy_table:
    '''
    This class will make creating/loading interactive Qtables from CSV files much easier for a 
    non-technical user base. 
    
    I note that I may take these out of the class instance and just leave them as pure functions
    but I like importing the classes better than the functions. 
    '''

       
    
    @staticmethod
    def create_table(name):
        '''
        This function will guide a non-technical user through the process of creating a 
        CSV file for at custom Q table. 
        '''
        
         # Putting print statements as variables because I got sick of staring at them in the main code. 
        intro_message = "This will guide you through the creation of a custom empty table using your Jupyter notebook"
        column_message = "Please enter the names you would like to use for the columns of your table. Press enter on a blank entry when you're finished"
        row_message = '''Do you want to have custom row names? (y/n)'''
        row_names = '''Please type your custom row names here. Press enter on a blank entry when you are finished'''

        row_len_message = '''How many rows does your table need? '''
        print(intro_message)
        print(column_message)
        print()
        
        while True:
            cont = input("Continue to table creation (y/n)")
            if cont.lower() == 'y':
                break
            if cont.lower() == 'n':
                print("Exiting...")
                return
            else:
                print("Invalid entry, please type 'y' or 'n'")
        
        # ask user for column names
        headers = []
        col_n = 1
        while True:
            col_name = input("Please enter a name for column " + str(col_n) + " (Enter to finish): ")
            col_n += 1
            if col_name == "":
                break
            else:
                headers.append(col_name)
        
        # Find out if user wants boring row names (0->N) or custom ones.
        # if boring ask how many rows, if custom ask for row names. 
        while True:
            row_type = input(row_message + ":")

            if row_type.lower() == 'y':
                print(row_names)
                row_n = 0
                rows = []

                while True:
                    row_name = input("Please enter a name for row " + str(row_n) + " (Enter to finish): ")
                    row_n += 1
                    
                    if row_name == "":
                        break
                    else:
                        rows.append(row_name)
                break
            
            # Ask user how many rows they want with a double check if they want more than 50 just in case.
            if row_type.lower() == 'n':
                
                while True:
                    cycle = False
                    try:
                        num_rows = int(input(row_len_message))
                        if num_rows > 50:
                            while True:
                                check = input("Are you sure you want " + str(num_rows) + " rows? (y/n) ")
                                if check.lower() == "y":
                                    print("Okay...")
                                    break
                                if check.lower() == "n":
                                    print(str(num_rows) + " did seem like a lot")
                                    cycle = True
                                    break
                                else:
                                    print("Please enter 'y' or 'n'")
                                
                        if not cycle: 
                            rows = [i for i in range(num_rows)]
                            break
                    except ValueError:
                        print("Please only enter an integer number")

                break

            else:
                print("Please type only 'y' or 'n' (case insensitive)")

        df = pd.DataFrame(index=pd.Series(rows), columns=pd.Series(headers))
        df.to_csv(name)
        print("Sucessfully saved CSV for loading " + name)
    
    @staticmethod
    def load_table(name, external = False, sep = ','):
        '''
        This function loads a csv file to into a Qtable
        '''
        
        # Here we're just finding the delimiters in case someone 
        # wants tab separation or whatever other crazy formats 
        # someone might try to stuff through here. Note: Autodetecting
        # the delimiter with sniffer does not work very well for online 
        # csv files, at least how I tried it. So I guess we can write this:
        # TODO: figure out how to make csv.sniffer work well with online files
        # so we can autodetect the delimiters. 
 
        # Probably not the best way of doing this...
        extension = name.split(".")[-1]
        if extension != 'csv':
            print("The file " + name + " needs to be a .csv file to load properly")
            return
        
        # The tables made by the QtableWidget have a little bit of a different
        # format that caouses the index to be topsy-turvy as compared to regular
        # csv files, this flag prevents us from accidentally using data as an index
        try:
            if not external:
                df = pd.read_csv(name, index_col=0, sep = sep)
            if external:
                df =  pd.read_csv(name, sep = sep)
        
        except FileNotFoundError:
            print("Cannot find the file " + name + ", please check that the path is correct.")
            return

        return qgrid.QgridWidget(df=df, show_toolbar=True)
    @staticmethod
    def save_table(name, save_name):
        '''
        This function simply saves a modified Qtable to a csv file. 
        '''
        try:
            updated_table = name.get_changed_df()
            updated_table.to_csv(save_name)
            print("Saved file " + save_name + " successfully") 
            
         # Honestly, probably never going to get the Name error, but it makes me feel better.     
        except NameError:
            print("The variable " +str(name)+ " does not exist. Please make sure you entered the correct table") 
        
    
    
    

class graph_table:
    '''
    This class will create a plotly graph from the tables created in the previous class. 
    I note that I may take these out of the class instance and just leave them as pure functions
    but I like importing the classes better than the functions. 
    '''
    @staticmethod
    def graph_from_table(table_name):
        '''
        This function creates an interactive plotly graph based on a Qtable taken as input.
        '''
  
        # Putting this here so we don't have to worry about it in the notebooks
        init_notebook_mode(connected=True)
        
        types = ['scatter', 'line', 'bar']
        
        try:
            updated_table = table_name.get_changed_df()
        except NameError:
            print("The variable " +str(name)+ " does not exist. Please make sure you entered the correct table") 
            return

        def graph(x_axes, y_axes,  kind,  title = '', y_name='', x_name=''):
            '''
            This function is to simplify creating a graph from an interactive Qtable and allows 
            us to use it with IPywidgets interactive
            '''
            # Choose plot type
            
            
            if kind == 'line':
                trace = Scatter(x=updated_table[x_axes],
                                y = updated_table[y_axes],
                                mode = 'lines+markers')
            if kind == 'bar':
                trace = Bar(x=updated_table[x_axes], 
                            y = updated_table[y_axes])

            if kind == 'scatter':
                trace = Scatter(x=updated_table[x_axes],
                                y = updated_table[y_axes],
                                mode = 'markers')

            # Choose axes stuff, as well as create defaults
            if x_name != '':
                x_lab = x_name
            else:
                x_lab = "Column: " + x_axes
            #
            if y_name != '':
                y_lab = y_name
            else:
                y_lab = "Column: " + y_axes

            layout = Layout(title = title,
                            xaxis = dict(title = x_lab), 
                            yaxis = dict(title = y_lab)
                           )

            fig = Figure(data = Data([trace]), layout = layout)

            iplot(fig)

        # Now we need to specify our widgets
        x_widget = widgets.Dropdown(
                                    options=updated_table.columns.tolist(),
                                    value=updated_table.columns.tolist()[0],
                                    description='X axis data',
                                    disabled=False,
                                    width = '250px'
                                )

        y_widget = widgets.Dropdown(
                                    options=updated_table.columns.tolist(),
                                    value=updated_table.columns.tolist()[1],
                                    description='Y axis data',
                                    disabled=False
                                )
        kind_widget = widgets.Dropdown(
                                    options=types,
                                    value=types[0],
                                    description='Plot Type',
                                    disabled=False
                                )

                            
        title_widget = widgets.Text(
                                value='',
                                placeholder='Enter plot title',
                                description='Plot title:',
                                disabled=False,
                                continuous_update=False
                                )
        x_name_widget = widgets.Text(
                                value='',
                                placeholder='X axis title',
                                description='X axis label:',
                                disabled=False,
                                continuous_update=False
                                )
        y_name_widget = widgets.Text(
                                value='',
                                placeholder='Y axis title',
                                description='Y axis label:',
                                disabled=False,
                                continuous_update=False
                                )


        graph_widg = interactive(graph, 
                 x_axes = x_widget,
                 y_axes = y_widget,
                 kind = kind_widget,
                 title = title_widget,
                 x_name = x_name_widget,
                 y_name = y_name_widget
                       )
        box_layout = widg_layout(display='flex',
                        flex_flow='column',
                        align_items='center',
                        border='solid',
                        width='100%')

        # Set up widget layout.
        left_box = widgets.VBox([graph_widg.children[i] for i in range(3)])
        right_box = widgets.VBox([graph_widg.children[i] for i in range(3,6)])

        widget_layout = widgets.HBox([left_box, right_box])

        # graph_widg.children[-1] is the output of interactive (plotly plot)
        to_display = widgets.VBox([graph_widg.children[-1], widget_layout], layout=box_layout)

        graph_widg.children = [to_display]
        
        display.display(graph_widg)
