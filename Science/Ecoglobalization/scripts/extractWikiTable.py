from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

url = "https://en.wikipedia.org/wiki/List_of_countries_by_ecological_footprint";

page = urlopen(url);

soup = BeautifulSoup(page, 'html.parser');

json_data = { }

table = soup.find("table", class_="wikitable");



index = 0;
rowIndex = 0;
dataToAdd = [];
for tableRow in table.findAll("tr")[1:]:
    dataToAdd.append([]);
    for tableData in tableRow.findAll("td"):
        value = tableData.get_text();
        value = value.replace("\n", "");
        value = value.replace("\xa0", "");
        dataToAdd[rowIndex].append(value);

    rowIndex += 1;

#print(dataToAdd);

for i in range(0, len(dataToAdd)):
    json_data[str(i+1)] =  {
                                "Rank": dataToAdd[i][0],
                                "Country" : dataToAdd[i][1],
                                "Ecological Footprint" : dataToAdd[i][2],
                                "Biocapacity" : dataToAdd[i][3],
                                "Biocapacity deficit or reserve" : dataToAdd[i][4],
                                "Population (millions)" : dataToAdd[i][5],
                                "Total Biocapacity" : dataToAdd[i][6]
                            };

with open('./data/wiki_data.json', 'w') as outfile:
    json.dump(json_data, outfile)
