## A class for the points of interest on a map

import ipyleaflet
import pandas as pd

class Markers():
    def __init__(self, Map):
        self.map = Map
        self.places = None
        self.markers = []
        self.popupTemplate = None
        self.popupCallback = None
        self.lat = None
        self.lon = None
        
    def read_data(self, fileName):
        self.places = pd.read_csv(fileName)
        
    
    def set_coordinates(lat=None, lon=None):
        self.lat = lat
        self.lon = lon
        
        if self.lat is None or self.lon is None:
            if self.places is None:
                print("Error: There is no data")
                return
            for i, col in enumerate(self.places.columns.values):
                if not self.lat:
                    if col.lower() == 'lat' or col.lower() == 'latitude':
                        self.lat = col
                if not self.lon:
                    if col.lower() == 'lon' or col.lower() == 'longitude':
                        self.lon = col
        if self.lat is None or self.lon is None:
            print("Warning: Could not find the coordinates, you will need to" +\
                  " manually set them")
    
    
    def set_default_popup(html, callback=None):
        self.popupTemplate = html
        self.popupCallback = callback
        
    
    def add_to_map(z_index_offset=0, draggable=True, keyboard=True, title='', alt='', 
                   rise_on_hover=False, opacity=1.0, visible=True, rise_offset=250):
        for i in range(len(self.places.columns.values)):
            self.markers.append(location=(self.lat[i], self.lon[i]), z_index_offset=0, 
                                draggable=True, keyboard=True, title='', alt='', 
                                rise_on_hover=False, opacity=1.0, visible=True, rise_offset=250)