require.config({
  paths: {
    d3: "https://d3js.org/d3.v4.min",
    d3geo: "https://d3js.org/d3-geo.v1.min",
    array: "https://d3js.org/d3-array.v1.min",
    config: "/js/config.js"
  }
});
require(['d3'], function(d3) {
    // define the width and height of the svg
    let width = 1280,
        height = 1000;

    console.log("hello");
    // create the svg using d3.js
    let canadaSVG = d3.select("#map")
        .append("svg")
          .attr("width", width)
          .attr("height", height);

    // append a grouping of drawings to the svg
    var g = canadaSVG.append("g");

    // The scale at which we see the map. Modify if you wish the initial size to be smaller or larger.
    var scalar = 300;

    // Create zoom functionality.
    var zoom = d3.zoom()
    .scaleExtent([1, 8])
    .on("zoom", zoomed);

    canadaSVG.call(zoom);

    // Define the projection to use for the map of Canada
    var projection = d3.geoMercator()
                        .scale([scalar])
                        .center([-45.5017, 73.5673])

    // Translate the projection to the "center"
    projection.translate([ (width / 2) + 100, (height / 2) - 100]);

    // Push the projection we used to the generator to generate the paths needed
    var geoGenerator = d3.geoPath()
      .projection(projection);

    // Create a tooltip which will show when hovering on a particular plane
    var tooltip = d3.select("body")
                      .append("div")
                      .attr("class", "tooltip")
                      .style("opacity", 0);

    // Create the map using the json file provided
    d3.json("./data/canada.json", function(error, canada) {
        if(error) return console.error(error);

        // Draw the paths which make up Canada using the json data
        g.selectAll("path")
          .data(canada.features)
              .enter()
                .append("path")
                  .attr("d", geoGenerator)
                    .style("fill", "#42f4b0");

        // Now, draw the plans on the map of Canada using the air traffic data
        d3.json("./data/air-traffic.json", function(error, airTraffic) {
          if(error) return console.error(error);

          g.selectAll("circle")
            .data(airTraffic.states)
              .enter()
                .append("circle")
                  .attr("cx", function(d) {
                    return projection([ d[5], d[6] ])[0];
                  })
                  .attr("cy", function(d) {
                    return projection([ d[5], d[6] ])[1];
                  })
                  .attr("r", 2)
                  .style("fill", "red")
                  .on("mouseover", mouseOverHandler)
                  .on("mouseout", mouseOutHandler);

          // Now we can filter some data using the configuration file that you edited.
          g.selectAll("circle").filter(function(d) {
            if(d[8]) {
              return true;
            }
          })
          .style("fill", "green")
          .attr("r", 2);
        });
    });

    // The zoom function to allow use to zoom in and out of the map.
    function zoomed() {
      g.attr("transform", d3.event.transform);
    }

    // mouseOverHandler is the functionality which makes the tooltip appear over a place.
    function mouseOverHandler(d) {
      tooltip.style(left)
    }

    // mouseOutHandler makes the tooltip disappear when you hover outside of a plane.
    function mouseOutHandler(d) {

    } 
});
