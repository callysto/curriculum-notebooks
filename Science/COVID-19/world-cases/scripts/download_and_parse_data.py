# Author: Laura Gutierrez Funderburk
# Created on: April 2020
# Last modified on: Sep 2020

"""
This script pulls COVID 19 data and creates interactive plots of COVID 19 cases in the world. 

"""
#!pip install pycountry_convert 
#!pip install requests 
#!pip install pandas 
#!pip install plotly 
import requests as r
import pandas as pd
import plotly.io as pio
import pycountry_convert as pc
import plotly.offline as offline 
import plotly.graph_objs as go
import numpy as np
from ipywidgets import widgets
from IPython.display import display, Javascript, Markdown, HTML, clear_output
from ipywidgets import interact, interact_manual, widgets, Layout, VBox, HBox, Button,fixed,interactive


def extract_latest(final_df):
    # This function gets latest for each country
    conf_dic = {}
    latest_arr = []
    cont_code_arr = []
    country_arr = []
    for country in final_df['country']:
        latest = float(final_df[final_df['country']==country]['latest'].sum())

        cont_code = final_df[final_df['country']==country]['continent code'].unique()[0]

        latest_arr.append(latest)
        cont_code_arr.append(cont_code)
        country_arr.append(country)

    conf_dic['country'] = country_arr
    conf_dic['continent code'] = cont_code_arr
    conf_dic['latest'] = latest_arr
    
    

    conf_df = pd.DataFrame(conf_dic)
    
    return conf_df



def generate_levels(df,case_type):
    # The sunburst plot requires weights (values), labels, and parent (region, or World)
    # We build the corresponding table here
    # Inspired and adapted from https://pypi.org/project/world-bank-data/ 
    columns = ['labels','parents',  'values']

    # Build the levels 
    # Level 1 - Countries
    level1 = df.copy()
    # Rename columns
    level1.columns = columns
    # Add a text column - format values column
    level1['text'] = level1['values'].apply(lambda pop:' ' +  str(case_type)+  ' Cases: {:,.0f}'.format(pop))
    level1['World total'] = level1['values'].sum()

    # Create level 2 - Continents
    #Group by continent code
    level2 = level1.groupby(['parents']).values.sum().reset_index()[['parents', 'parents', 'values']]
    # Rename columns
    level2.columns = columns
    level2['parents'] = 'World'
    # move value to text for this level
    level2['text'] = level2['values'].apply(lambda pop: ' ' + str(case_type)+  ' Cases: {:,.0f}'.format(pop))

    ## Create level 3 - world total as of latest date
    level3 = pd.DataFrame({'parents': ['World'], 'labels': ['World'],
                       'values': [level1.groupby("parents").sum().sum()[0]], 'text':['{:,.0f}'.format(level1.groupby("parents").sum().sum()[0])]})
    #Create master dataframe with all levels
    all_levels = pd.concat([level1,level2], axis=0,sort=True)

    return all_levels

def plot_sunburst(df,case_type):
    last_date = pd.to_datetime('today').date()
    fig = offline.iplot(dict(
        data=[dict(type='sunburst', hoverinfo='text', **df,name='Overview')],
        layout=dict(title='COVID-19'  + ' ' + str(case_type) + ' Cases as of ' + str(last_date),
                    width=800,height=800,insidetextorientation='radial')),validate=False)
    return fig



# Define a function to drop the history.prefix
# Create function drop_prefix
def drop_prefix(self, prefix):
    self.columns = self.columns.str.lstrip(prefix)
    return self

# Call function
pd.core.frame.DataFrame.drop_prefix = drop_prefix

# Define function which removes history. prefix, and orders the column dates in ascending order
def order_dates(flat_df):

    # Drop prefix
    flat_df.drop_prefix('history.')
    flat_df.drop_prefix("coordinates.")
    # Isolate dates columns
    flat_df.iloc[:,6:].columns = pd.to_datetime(flat_df.iloc[:,6:].columns)
    # Transform to datetim format
    sub = flat_df.iloc[:,6:]
    sub.columns = pd.to_datetime(sub.columns)
    # Sort
    sub2 = sub.reindex(sorted(sub.columns), axis=1)
    sub3 = flat_df.reindex(sorted(flat_df.columns),axis=1).iloc[:,-5:]
    # Concatenate
    final = pd.concat([sub2,sub3], axis=1, sort=False)
    return final


# We will plot the log projection along with the cumulative number of cases
def plot_log_function(country,final_df,type_case,case):
    
    latest_arr = []
    date_arr = []
    for item in final_df[final_df.index==country].iloc[:,0:-5].columns:
        date_arr.append(item)
        latest_arr.append(final_df[final_df.index==country][item].sum())

    final_confirmed_red = pd.DataFrame({"Date":date_arr,"CumulativeTotal":latest_arr})
    non_cumulative_cases = final_confirmed_red.diff(axis=0)
    
    
    x = final_confirmed_red.Date
    if case==True:
        y = final_confirmed_red.CumulativeTotal
    else:
        y = non_cumulative_cases.CumulativeTotal
    
    npy = np.array(y.to_list())
    l_y = np.log10(npy, where=0<npy, out=np.nan*npy)


    trace1 = go.Bar(x=x,y=y,name=country)
    trace2 = go.Scatter(x=x,y=l_y,name='Log ' + str(country),yaxis='y2')
    layout = go.Layout(
        title= ('Number of ' + str(type_case) + ' cases for ' + str(country)),
        yaxis=dict(title='Total Number of ' + str(type_case).capitalize() + ' Cases',\
                   titlefont=dict(color='blue'), tickfont=dict(color='blue')),
        yaxis2=dict(title=str(type_case).capitalize()  + ' Cases (logarithmic scale)', titlefont=dict(color='red'), \
                    tickfont=dict(color='red'), overlaying='y', side='right'),
        showlegend=False)
    fig = go.Figure(data=[trace1,trace2],layout=layout)
    fig.update_yaxes(showgrid=True)
    fig.show()   
    
def draw_results(b):
    country = all_the_widgets[0].value
    case = all_the_widgets[1].value
    clear_output()
    display(tab)  ## Have to redraw the widgets
    plot_log_function(country,final_confirmed,"confirmed",case)
    plot_log_function(country,final_deaths,"fatal",case)

if __name__ == "__main__":

    # Get the latest data
    # Confirmed
    try:
        API_response_confirmed = r.get("https://covid19api.herokuapp.com/confirmed")
        data = API_response_confirmed.json() # Check the JSON Response Content documentation below
        confirmed_df = pd.json_normalize(data,record_path=["locations"])

        print("Confirmed cases download was successful!")
    except:
        print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")
    # Deaths
    try:
        API_response_death = r.get("https://covid19api.herokuapp.com/deaths")
        data1 = API_response_death.json() # Check the JSON Response Content documentation below
        death_df = pd.json_normalize(data1,record_path=["locations"])

        print("Fatal cases download was successful!")
    except:
        print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")
    # Latest
    try:
        API_summary = r.get("https://covid19api.herokuapp.com/latest")
        data2 = API_summary.json()
        summary  = pd.json_normalize(data2)
        print("Latest cases download was successful!")
    except:
        print("Error: check GitHub is functioning appropriately, check https://covid19api.herokuapp.com/ is not down, check fields were not renamed")
        
        
    # Assign continent codes for sunburst plot
    cont_codes = []
    for item in confirmed_df["country_code"]:
        try:
            cont_code = pc.country_alpha2_to_continent_code(item)
            cont_codes.append(cont_code)
        except:
            cont_codes.append(item)

    confirmed_df["continent code"] = cont_codes
    death_df["continent code"] = cont_codes
    print("Continent codes appended.")
    
    
   # Get latest cases, sum and remove duplicates
    conf_df = extract_latest(confirmed_df)
    deat_df = extract_latest(death_df)

    conf_df['Total'] = conf_df.groupby(['country', 'continent code'])['latest'].transform('sum')
    no_duplicates_conf_df = conf_df.drop_duplicates(subset=['country', 'continent code'])

    deat_df['Total'] = deat_df.groupby(['country', 'continent code'])['latest'].transform('sum')
    no_duplicates_deat_df = deat_df.drop_duplicates(subset=['country', 'continent code'])

    # Subset data
    conf_df = no_duplicates_conf_df[['country','continent code','latest']]
    deat_df = no_duplicates_deat_df[['country','continent code','latest']]
    
    
    ##################
    
    # Flattening the data 
    flat_confirmed = pd.json_normalize(data=data['locations'])
    flat_death = pd.json_normalize(data=data1['locations'])
    flat_confirmed.set_index('country', inplace=True)
    flat_death.set_index('country', inplace=True)



    # Apply function
    final_confirmed = order_dates(flat_confirmed)

    final_deaths = order_dates(flat_death)
    countries_regions = final_confirmed.index.unique().tolist()
    
    # User menu
    countries_regions = final_confirmed.index.unique().tolist()

    style = {'description_width': 'initial'}

    all_the_widgets = [widgets.Combobox(
        # value='John',
        placeholder='Choose a country',
        options=countries_regions,
        description='Choose a country:',
        ensure_option=True,
        disabled=False,
        style=style
    ),
widgets.Checkbox(
    value=False,
    description='Get cumulative results',
    disabled=False,
    indent=False,
    style=style
)]

    # Button widget
    CD_button = widgets.Button(
        button_style='success',
        description="Cumulative Case Count", 
        layout=Layout(width='15%', height='30px'),
        style=style
    )
    

    # Connect widget to function - run subsequent cells
    CD_button.on_click( draw_results )

    # user menu using categories found above
    tab3 = VBox(children=[HBox(children=all_the_widgets[0:2]),HBox(children=all_the_widgets[2:5]),
                          CD_button])
    tab = widgets.Tab(children=[tab3])
    tab.set_title(0, 'Choose Parameters')
    

