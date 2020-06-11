function generateMap() {
    let width = 700,
        height = 580;

    let svg = d3.select("#interactive-map-container")
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    d3.json("canada.json", function(error, canada) {
      if(error) return console.error(error);

      svg.append("path")
        .datum(topojson.feature(canada, canada.objects.subunits))
        .attr("d", d3.geo.path().projection(d3.geo.mercator()));
    });
}
