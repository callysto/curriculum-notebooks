import re
import pickle as pk

# Constants
ATTR_DELIM = str(chr(3))
STATION_DELIM = str(chr(4))
ATTRS = {
    'name': 0,
    'prov': 1,
    'lat': 2,
    'lon': 3,
    'elevation': 4,
    'station_id': 5,
    'start_date': 6,
    'end_date': 7,
    'climate_id': 8,
    'wmo_id': 9,
    'tc_id': 10
}

ATTRS_LIST = ['Station Name', 'Province', 'Latitude', 'Longitude', 'Elevation',
              'Station ID', 'Start Date', 'End Date', 'Climate ID', 'WMO ID', 'TC ID']

# Information template for every individual station
class station(object):
    __slots__ = ('name', 'prov', 'lat', 'lon', 'elevation', 
                'station_id', 'start_date', 'end_date', 
                'climate_id', 'wmo_id', 'tc_id')
    def __init__(self):
        self.name = ''
        self.prov = ''
        self.lat = 0.0
        self.lon = 0.0
        self.elevation = ''
        self.station_id = ''
        self.start_date = ''
        self.end_date = ''
        self.climate_id = ''
        self.wmo_id = ''
        self.tc_id = ''

# Removes spaces before and after text
def remove_trailing_spaces(string):
    if string is None:
        return ''
    i = 0
    for i in range(len(string)):
        if string[i] != ' ':
            break
    string = string[i:]
    j = 0
    for j in range(len(string)-1, 0, -1):
        if string[j] != ' ':
            break
    string = string[:j+1]
    return string

# Converts pickle file(s) to a .txt file
def to_txt(pickle_files, txt_file_name):
    print("Unpickling...")
    string_of_stations = ''
    for pickle_name in pickle_files:
        with open(pickle_name,'rb') as f:
            new_stations =  pk.load(f)
            for j in range(len(new_stations)):
                string_of_stations += remove_trailing_spaces(new_stations[j].name) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].prov) + ATTR_DELIM
                string_of_stations += str(new_stations[j].lat) + ATTR_DELIM
                string_of_stations += str(new_stations[j].lon) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].elevation) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].station_id) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].start_date) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].end_date) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].climate_id) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].wmo_id) + ATTR_DELIM
                string_of_stations += remove_trailing_spaces(new_stations[j].tc_id) + ATTR_DELIM
                string_of_stations += STATION_DELIM

    with open(txt_file_name, 'w') as f:
        f.write(string_of_stations)
        
    print("Done")
    
# Returns a list of station strings
def read_stations(file_name):
    lst = []
    with open(file_name, 'r') as f:
        string = f.read()        
        lst = string.split(STATION_DELIM)
     
    # Get rid of empty stations
    keep = []
    for element in lst:
        if not element:
            continue
        keep.append(element)
        
    return keep

# Returns an attribute of a station when given a string from ATTRS (ie. 'name', 'prov'...)
def get_station_attr(station, attr):
    index = ATTRS[attr]
    try:
        return station.split(ATTR_DELIM)[index]
    except IndexError:
        print(station)
        return None

def to_csv(file_name):
    with open(file_name, 'r') as f:
        string = f.read()
        lst = string.split(STATION_DELIM)
        
    with open('alberta_stations_data.csv', 'w') as f:
        keep = []
        for element in lst:
            #keep.append(','.join(element.split(ATTR_DELIM)[:11]))
            attrs = element.split(ATTR_DELIM)
            for i in range(len(attrs)):
                attrs[i] = ''.join(attrs[i].split(','))
                #if attrs[i] == '     ':
                if re.match(r'^\W+', attrs[i]):
                    attrs[i] = ''
            keep.append(','.join(attrs[:11]))
        #print(keep[:5])
        f.write(','.join(ATTRS_LIST))
        f.write('\n')
        f.write('\n'.join(keep))
                    
                    
# Default if run not as a library
if __name__ == '__main__':
    to_csv('alberta_stations.txt')