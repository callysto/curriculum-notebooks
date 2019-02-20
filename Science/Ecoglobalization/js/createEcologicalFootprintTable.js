var jsonArray = [],
    tableBuilt = false,
    currentData = [],
    topEnd = 20,
    bottomStart = 20;

var filters = Object.freeze({ ALL: 0, TOP: 1, BOTTOM: 2 }),
    currentFilter = filters.TOP;

function buildEcoTable(userScore) {
      if(!tableBuilt) {
          d3.json("./data/wiki_data.json", function(data) {
              d3.select("#ecological-footprint-countries-container").classed("rendered_html", false);
              let index = 1;
              let wikiTable = d3.select("#wikitable").style("width", "100%").classed("rendered_html", false);
              let headings = [ "Rank", "Country", "Ecological Footprint", "Biocapacity", "Biocapacity deficit or reserve", "Population (millions)", "Total Biocapacity"];
              wikiTable.append("thead").append("tr")
                .selectAll("th")
                  .data(headings)
                    .enter()
                      .append("th")
                        .text(function(d) { return d; } )
                        .style("text-align", "center")
                        .classed("rendered_html", false);


              let numberOfEntriesToDisplay = 20;
              let keyLength = Object.keys(data).length;
              for(let i = 1; i <= keyLength; ++i) {
                let objectKeyLength = Object.keys(data[i.toString()]).length;
                jsonArray.push([]);
                jsonArray[i-1].push(data[i.toString()].Rank);
                jsonArray[i-1].push(data[i.toString()].Country);
                jsonArray[i-1].push(data[i.toString()]["Ecological Footprint"]);
                jsonArray[i-1].push(data[i.toString()].Biocapacity);
                jsonArray[i-1].push(data[i.toString()]["Biocapacity deficit or reserve"]);
                jsonArray[i-1].push(data[i.toString()]["Population (millions)"]);
                jsonArray[i-1].push(data[i.toString()]["Total Biocapacity"]);
              }

              user = [0,"You",userScore, "-", "-", "-", "-"];
              jsonArray.push(user);

              jsonArray.sort(function(a, b) {
                  return b[2] - a[2];
              });

              for(let i = 0; i < jsonArray.length; ++i) {
                  jsonArray[i][0] = i+1;
              }

              wikiTable.append("tbody")
                  .selectAll("tr")
                    .data(jsonArray)
                      .enter()
                        .append("tr")
                          .selectAll("td")
                             .data(function(d) { return d; })
                              .enter()
                                 .append("td")
                                    .text(function(d) { return d; })
                                    .style("text-align", "center")
                                    .classed("rendered_html", false);

               wikiTable.selectAll("tr").filter(function(d, i) {
                  if(i > 0 && d[1] === "You")
                      return true;
               }).classed("user-score", true);

            if(currentFilter === filters.TOP) {
                filter("top");
            }
            else if(currentFilter === filters.BOTTOM) {
                filter("bottom");
            }
            tableBuilt = true;
      });
    }
    
    else { 
        // Update data using the users score
        for(let i = 0; i < jsonArray.length; ++i) {
            if(jsonArray[i][1] === "You") {
                jsonArray[i][2] = userScore;
                break;
            }
        }
        
        jsonArray.sort(function(a, b) {
             return b[2] - a[2];
        });
        
        for(let i = 0; i < jsonArray.length; ++i) {
           jsonArray[i][0] = i+1;
        }
        
        if(currentFilter === filters.ALL) {
           console.log("Filtering ALL");
           filter("all");
        }
        
        else if(currentFilter === filters.TOP) {
            filter("top");
        }
        
        else {
            filter("bottom");
        }
    }
}

function filter(str) {
   if(typeof(str) != "string") {
       console.error("filter must get a string argument that is either \"top\", \"bottom\", or \"all\"");
       return;
   }
   
   let wikiTable = d3.select("#wikitable");
   if(str === "top") {
       currentFilter = filters.TOP;
       currentData = jsonArray.slice(0, topEnd);
       updateTable();
       
       d3.selectAll(".selected").classed("selected", false);
       d3.select("#top-btn").classed("selected", true);
   }
    
    else if(str === "bottom") {
       currentFilter = filters.BOTTOM;
       currentData = jsonArray.slice(jsonArray.length - bottomStart);
       updateTable();
        
       d3.selectAll(".selected").classed("selected", false);
       d3.select("#bottom-btn").classed("selected", true);
    }
    
    else if(str === "all") {
        currentFilter = filters.ALL;
        currentData = jsonArray;
        updateTable();
        
        wikiTable.select("tbody")
            .selectAll("tr")
                .data(jsonArray)
                  .enter()
                    .append("tr")
                      .selectAll("td")
                         .data(function(d) { return d; })
                            .enter()
                                .append("td")
                                .text(function(d) { return d; })
                                .style("text-align", "center")
                                .classed("rendered_html", false);
        
       wikiTable.selectAll("tr").filter(function(d, i) {
         if(i > 0 && d[1] === "You")
           return true;
       }).classed("user-score", true);
        
       d3.selectAll(".selected").classed("selected", false);
       d3.select("#all-btn").classed("selected", true);    
    }
}

function updateTable() {
   let wikiTable = d3.select("#wikitable");

   wikiTable.select("tbody").selectAll("tr")
                               .data(currentData)
                                 .exit()
                                   .remove();

   wikiTable.select("tbody").selectAll("tr")
        .classed("rendered_html", false)
            .data(currentData)
                  .selectAll("td")
                     .data(function(d) { return d; })
                            .text(function(d) { return d; })
                            .style("text-align", "center")
                            .classed("rendered_html", false);

   d3.selectAll(".user-score").classed("user-score", false);
          
   wikiTable.selectAll("tr").filter(function(d, i) {
         if(i > 0 && d[1] === "You")
          return true;
    }).classed("user-score", true);
}