import requests
from ipywidgets import HTML
from scipy.spatial import cKDTree
from bs4 import BeautifulSoup as bs
from pickle_to_txt import read_stations, get_station_attr

STRING_CHECKBOX='''<html>
<body>
<p>Display some text when the checkbox is checked:</p>
Checkbox: <input type="checkbox" id="myCheck"  onclick="myFunction()">
<p id="text" style="display:block">Checkbox is CHECKED!</p>

<script>
function myFunction() {
    var checkBox = document.getElementById("myCheck");
    var text = document.getElementById("text");
    alert('Goodbye World!');
    if (checkBox.checked == true){
        text.style.display = "block";
        alert('Hello World!');
    } else {
       text.style.display = "none";
    }
}
</script>
</body>
</html>'''

STRING_BUTTON='''<html>
<body>
<p id="show_in_table" hidden>no</p>
<button type="button" onclick="document.getElementById('show_in_table').innerHTML = 'yes'">Show in table</button>
 
</body>
</html>'''

class KElementHeap():
    def __init__(self, k):
        self.k = k
        self.heap = [None] * k
        self.index = [None] * k
        
    def add(self, n, index, pos):
        last_elem = None
        last_index = None
        
        for i in range(len(self.heap)):
            last_elem = self.heap[i]
            last_index = self.index[i]
            self.heap[i] = n
            self.index[i] = index
            n = last_elem
            index = last_index
                
    def push(self, n, index):
        for i in range(len(self.heap)):
            if self.heap[i] is None or n < self.heap[i]:
                self.add(n, index, i)
                break
                
    def get_best(self):
        return self.index

    
def init_kdtree(Stations):
#    dim = 2
#    data = [[None]*len(Stations)] * dim
#    for i, station in enumerate(Stations):
#        lat = float(get_station_attr(station, 'lat'))
#        lon = float(get_station_attr(station, 'lon'))
#        data[0][i] = lat
#        data[1][i] = lon
    data = [None] * len(Stations)
    for i, station in enumerate(Stations):
        lat = float(get_station_attr(station, 'lat'))
        lon = float(get_station_attr(station, 'lon'))
        data[i] = (lat, lon)
    
    return cKDTree(data)

# This is a log(n) search for a station
#     pos = (lat, lon)
def kdtree_station_find(kdtree, Stations, Markers, Popups, pos):
    query = kdtree.query(pos)
    index = query[1]
    
    if Popups[index] is None:
            name = get_station_attr(Stations[index], 'name')
            station_id = get_station_attr(Stations[index], 'station_id')
            lat = get_station_attr(Stations[index], 'lat')[:6]
            lon = get_station_attr(Stations[index], 'lon')[:6]
            end = get_station_attr(Stations[index], 'end_date')
            #msg = '<p>' + name + '</p><p>' + get_mean_temp(station_id) + '</p>'
            Popups[index] = HTML(value='<p>'+name+'</p>\n<p>Latitude: '+lat+'<br>Longitude: '+lon+'<br>End Date: '+end+'</p>'+STRING_BUTTON,
                                 placeholder='',
                                 description='')
#            Popups[index] = HTML_HIDE
            Markers[index].popup = Popups[index]
#            print(Markers[index].options)
    

# This is a slow implementation, if to slow make a quad-tree
#     pos is (lat, lon)
#     k is the how many to find
def linear_station_find(Stations, Markers, Popups, pos, k=1):
    
    top = KElementHeap(k)
    for i, station in enumerate(Stations):
        lat = float(get_station_attr(station, 'lat'))
        lon = float(get_station_attr(station, 'lon'))
        dist = (pos[0]-lat)**2 + (pos[1] - lon)**2
        top.push(dist, i)
     
    best = top.get_best()
    for index in best:
        if Popups[index] == None:
            name = get_station_attr(Stations[index], 'name')
            lat = get_station_attr(Stations[index], 'lat')
            lon = get_station_attr(Stations[index], 'lon')
            #station_id = get_station_attr(Stations[index], 'station_id')
            msg = '<p>' + name + '</p><p>' + get_mean_temp(station_id) + '</p>' + HTML_CHECKBOX
            Popups[index] = HTML(value=msg,
                                 placeholder='',
                                 description='')

            Markers[index].popup = Popups[index]
    
        
def dec_to_deg(num):
    decimal = num - int(num)
    minutes = decimal * 60
    leftover = minutes - int(minutes)
    seconds = leftover * 60
    
    return (int(num), int(minutes), seconds)

def get_mean_temp(station_id):
    url = 'http://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID={}'.format(station_id)
    EMPTY = '\xa0'

    content = requests.get(url).content
    soup = bs(content, 'lxml')
    table = soup.find('tbody')
    days = table.find_all('tr')[1:]

    data = days[0].find_all('td')[2].contents[0]
    if data == EMPTY or data.name is not None:
        return 'Sorry I could not find the teperature'

    for i in range(len(days)-5, 0, -1):
        entries = days[i].find_all('td')
        data = entries[3].contents[0]
        if data != EMPTY and data.name is None:
            return "The last recorded temp was on {} and it was a mean tempurature of {}&deg;C".format(entries[0].contents[0].attrs['title'],
                                                                            entries[3].contents[0])
    return 'Sorry I could not find the teperature'