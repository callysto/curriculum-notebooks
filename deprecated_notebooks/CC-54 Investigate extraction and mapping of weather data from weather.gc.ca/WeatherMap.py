import re
import sys
import time
import requests
import ipyleaflet
from shared import *
from tqdm import tqdm
from constants import *
from threading import Timer
from ipywidgets import HTML
from MapEvents import MapEvents
from ipykernel.comm import Comm
from scipy.spatial import cKDTree
from bs4 import BeautifulSoup as bs
from IPython.display import HTML as HTML_DISPLAY
from ipyleaflet import Marker, Popup, MarkerCluster
from pickle_to_txt import read_stations, get_station_attr


class WeatherMap(MapEvents):
    def __init__(self, Map=None, center=None, zoom=None):
        if Map is None:
            self.center = center
            if not center:
                self.center = (52.585538631877306, 245.45105824782084)
                
            self.zoom = zoom
            if not zoom:
                self.zoom = 6
                
            self.map = ipyleaflet.Map(center=self.center, zoom=self.zoom, close_popup_on_click=False)
        else:
            self.map = Map
        super().__init__(self.map)
        
        self.stations = []
        self.popups = []
        self.markers = []
        self.current_station = None
        self.comm = None
        self.table_data = {'table': None, 'id': 0}

    # Overloading the mousemove callback function
    def mousemove(self, type, event, coordinates):
        self.station_find(coordinates)

    
    def build(self, fileName):
        self.stations = read_stations(fileName)
        self.num_of_stations = len(self.stations)
        self.markers = [None] * self.num_of_stations
        self.popups = [None] * self.num_of_stations
        self.load_data()
        self.init_kdTree()
        #self.open_table_comm('_table_')
  
        #self.table.hold_sync
        #self.open_comm('_button_')
        self.table_comm = Comm(target_name='_table_', data={'foo': 1})
        get_ipython().kernel.comm_manager.register_target('_table_callback_', self.table_callback_comm)
        self.table = HTML_DISPLAY(HTML_TABLE)
        #self.map.on_interaction(self.callback)
        
    
    def open_comm(self, label):
        get_ipython().kernel.comm_manager.register_target(label, self.comm_handler)
    
#     def open_table_comm(self, label):
#         self.open_table_comm = get_ipython().kernel.comm_manager.register_target(label, self.table_comm)
        
    def table_callback_comm(self, comm, msg):
        @comm.on_msg
        def _recv(msg):
            #self.comm = msg
            self.update_table(msg)
            self.table_comm.send(self.table_data)
    
#     def table_comm(self, comm, msg):
#         @comm.on_msg
#         def _recv(msg):
#             self.comm = msg
#             self.update_table()
#             self.open_table_comm.send(self.table_data);
#             #comm.send(self.table_data)
    
    def comm_handler(self, comm, msg):
        @comm.on_msg
        def _recv(msg):
            self.comm = msg            
            self.update_table()
            
    # Converts a month by string, into the index that it occures in order
    # eg. 'january' => 0, 'May' => 4
    def month_to_index(self, month):
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 
                  'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
        month = month.lower()[:3]
        return months.index(month)

    
#     def get_date_range(self, stationID):
#         url = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID={}'.format(stationID)
#         content = requests.get(url).content
#         soup = bs(content, 'lxml')
#         self.Log = 0
#         # Get the years that this station has been operating
#         year_select = soup.find_all('select', {'id': 'Year1'})
#         self.Log = year_select
#         year_select = year_select[0]
#         years = year_select.find_all('option')
#         year_range = []
#         for year in years:
#             year_range.append(year.attrib['value'])
#         self.Log = 1
#         # Get the months available for the most recent year
#         month_select = soup.find_all('select', {'id': 'Month1'})[0]
#         months = month_select.find_all('option')
#         end_month_range = []
#         for month in months:
#             end_month_range.append(month.attrib['value'])
#         self.Log = 2
#         # Get the days from the most recent month
#         table = soup.find_all('div', {'id': 'dynamicDataTable'})[0].find_all('tbody')[0]
#         rows = table.find_all('tr')
#         end_days = []
#         for row in rows:
#             try:
#                 day = int(row.find_all('td')[0].find('abbr').content[:2])
#                 end_days.append(day)
#             except:
#                 pass
#         self.Log = 3 
#         # Goto the page of the first year, first month
#         url += '&Year={}&Month=1'.format(year_range[0])
#         content = requests.get(url).content
#         soup = bs(content, 'lxml')
#         self.Log = 4
#         # Get the months from the first year available
#         month_select = soup.find_all('select', {'id': 'Month1'})[0]
#         months = month_select.find_all('option')
#         start_month_range = []
#         for month in months:
#             start_month_range.append(month.attrib['value'])
#         self.Log = 5
#         #url += '?Month={}'.format(month_range[0])
#         #content = requests.get(url).content
#         #soup = bs(content, 'lxml')
        
#         # Get the days from the first year available
#         table = soup.find_all('div', {'id': 'dynamicDataTable'})[0].find_all('tbody')[0]
#         rows = table.find_all('tr')
#         start_days = []
#         for row in rows:
#             try:
#                 day = int(row.find_all('td')[0].find('abbr').content[:2])
#                 start_days.append(day)
#             except:
#                 pass
#         self.Log = 6
#         return {'years': year_range, 'start': (start_days, start_month_range), 
#                 'end': (end_days, end_month_range)}
   
    
    def weather_data(self, station_id, year=None, month=None):
        station_id = get_station_attr(self.stations[station_id], 'station_id')
        return self.get_table(station_id, year, month)
    
    def get_table(self, stationID, year=None, month=None):
        url = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID={}'.format(stationID)
        if year is not None and month is not None:
            url += '&Year={}&Month={}'.format(year, month)
        EMPTY = '\xa0'
        MISSING = '<a '
        DATE_RANGE_RE = re.compile(r'var maxMin ?= ?\[([\'\"].*[\'\"]).*\]')
        self.Log = url
        site = requests.get(url)
        content = site.content
        soup = bs(content, 'lxml')
        table = soup.find('tbody')
        days = table.find_all('tr')[1:]

        if days[0].find_all('td')[2].contents[0] == EMPTY or days[0].find_all('td')[2].contents[0] == MISSING:
            print(days[0].find_all('td')[2].contents[0])

        table = {'day': [], 'temp': [], 'rain': [], 'wind': [], 'date': '--'}
        # Attempt to find the date on each day if needed
        for day in days:
            try:
                date = day.find_all('td')[0].contents[0].attrs['title']
                split_date = date.split(' ')
                table['date'] = '%s %s' % (split_date[0], split_date[-1])
                break
            except Exception as e:
                self.Log = e

        for i in range(len(days)-4):
            entries = days[i].find_all('td')

            meanTemp  = None
            totalRain = None
            windSpeed = None
            date      = None
            number    = None
            
            try:
                date = entries[0].contents[0].attrs['title']
            except:
                pass
            try:
                number = entries[0].contents[0].text
            except:
                pass
            
            if entries[3].contents[0] != EMPTY and entries[3].contents[0].name is None:
                meanTemp = entries[3].contents[0] 
            if entries[8].contents[0] != EMPTY and entries[8].contents[0].name is None:
                totalRain = entries[8].contents[0]
            if entries[11].contents[0] != EMPTY and entries[11].contents[0].name is None:
                windSpeed = entries[8].contents[0]        

            table['day'].append(number)
            table['temp'].append(meanTemp)
            table['rain'].append(totalRain)
            table['wind'].append(windSpeed)

        # Try to get a tuple representing the last day that whether was recorded
        # in the form ((int)day, (int)month, (int)year)
        try:
            date = table['date'].split(' ')
            month = date[0]
            month = self.month_to_index(month)
            last_day = 0
            for day in reversed(table['day']):
                # Looking for last day that has is a number
                # Some numbers have a qualifier like 23T
                try:
                    last_day = int(day[:2])
                    break
                except:
                    pass
            table['last_day'] = (last_day, month, int(date[1]))
        except:
            table['last_day'] = (0, 0, 0)

        #try:
        #    date_range = self.get_date_range(stationID)
        #    table['range'] = ((date_range['start'][0][0], date_range['start'][1][0], date_range['years'][0]),
        #                      (date_range['end'][0][-1], date_range['end'][1][-1], date_range['years'][-1]))
        #except Exception as e:
        #    pass#self.Log = e
        date_range = 'start'
        date_range = DATE_RANGE_RE.findall(site.text)[0] 
        date_range = ''.join(list(filter(lambda x: x != ' ' and x != '"' and x != "'", list(date_range))))
        table['range'] = date_range.split(',')
        return table
    
    
    def load_data(self):
        # Put a marker on the map for each station
        for i, station in enumerate(tqdm(self.stations)):
            marker = Marker(location=(float(get_station_attr(station, 'lat')), 
                                      float(get_station_attr(station, 'lon'))), 
                            draggable=False)
            self.markers[i] = marker
            
        marker_cluster = MarkerCluster(markers=self.markers)
        self.map.add_layer(marker_cluster)
        
    
    # Initialize the kdtree so queries can be made
    def init_kdTree(self):
        data = [None] * self.num_of_stations
        for i, station in enumerate(self.stations):
            lat = float(get_station_attr(station, 'lat'))
            lon = float(get_station_attr(station, 'lon'))
            data[i] = (lat, lon)

        self.kdTree = cKDTree(data)

        
    # This is a log(n) search for a station using a kdtree to query
    #     pos = (lat, lon)
    def station_find(self, pos):
        query = self.kdTree.query(pos)
        index = query[1]

        if self.popups[index] is None:
            name = get_station_attr(self.stations[index], 'name').title()
            station_id = get_station_attr(self.stations[index], 'station_id')
            lat = get_station_attr(self.stations[index], 'lat')[:6]
            lon = get_station_attr(self.stations[index], 'lon')[:6]
            end = get_station_attr(self.stations[index], 'end_date')
            #self.popups[index] = HTML(value='<p>'+name+'</p>\n<p>Latitude: '+lat+\
            #                          '<br>Longitude: '+lon+'<br>End Date: '+end+\
            #                          '</p>'+HTML_BUTTON,
            #                     placeholder='',
            #                     description='')
            #self.popups[index] = HTML(HTML_POPUP % (name, lat, lon, index))
            self.popups[index] = HTML(HTML_COMM % (name, lat, lon, index))
            #self.popups[index] = HTML_DISPLAY(HTML_RANGE_SLIDER)
            self.markers[index].popup = self.popups[index]
            
            
    def get_last_temp(stationID):
        url = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID={}'.format(stationID)
        EMPTY = '\xa0'
        MISSING = '<a '

        content = requests.get(url).content
        soup = bs(content, 'lxml')
        table = soup.find('tbody')
        days = table.find_all('tr')[1:]

        if days[0].find_all('td')[2].contents[0] == EMPTY or days[0].find_all('td')[2].contents[0] == MISSING:
            return days[0].find_all('td')[2].contents[0]

        for i in range(len(days)-5, 0, -1):
            entries = days[i].find_all('td')

            # Need a better gaurd
            if entries[3].contents[0] != EMPTY and entries[3].contents[0].name is None:
                return "The mean temp for {} is {}C".format(entries[0].contents[0].attrs['title'],
                                                            entries[3].contents[0])
                break;


    
    # Updates the information in the display table using the comm data from our html
    def update_table(self, msg):
#         if self.comm is None:
#             return
        index = int(msg['content']['data']['index'])
        name = get_station_attr(self.stations[index], 'name').title()
        lat = get_station_attr(self.stations[index], 'lat')[:6]
        lon = get_station_attr(self.stations[index], 'lon')[:6]
        stationId = get_station_attr(self.stations[index], 'station_id')
        #self.table_data = {'table': name}        
        self.index = stationId
        try:
            year = int(msg['content']['data']['year'])
            month = int(msg['content']['data']['month'])
            self.table_data = {'table': self.get_table(stationId, year=year, month=month), 'id': index}
        except Exception as e:
            self.table_data = {'table': self.get_table(stationId), 'id': index}
        #self.table.value = (HTML_TABLE % (name, lat, lon))