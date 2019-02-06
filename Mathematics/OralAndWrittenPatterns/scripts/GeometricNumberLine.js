var svg = d3.select('#GEO');

var numberline = [...Array(5).keys()];
requirejs.config({
    paths: { 
        'd3': ['//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3'], 
    },                                         // strip .js ^, require adds it back
});

require(['d3'], function(d3) {
d3.select("#geoButton")
    .on("click", function(){
    
        initValue = parseInt(document.getElementById("frm2_initGeo")
            .elements[0]
            .value);
            
        ratio = parseInt(document.getElementById("frm1_ratio")
            .elements[0]
            .value);
        if(initValue < 1 || initValue > 50){
            svg.selectAll('circle').remove();
            svg.selectAll('text').remove();
            svg.append('text').text("Oh no! The values you selected can't make a nice sequence, please select new differences and inital values")
            .attr('x', 10)
            .attr('y', 40).style("font-size", "18px")
            return
        }

        var data = [initValue]
                    
        if(ratio > 1 && ratio < 5 ){
                        
            var data = [...Array(50).keys()]
                        .map( (num,i) => initValue*(ratio**i))
                        .filter(num => num < 50)
                        .filter(num => (num > -1));
        }
        else{
            svg.selectAll('circle').remove();
            svg.selectAll('text').remove();
            svg.append('text').text("Oh no! The values you selected can't make a nice sequence, please select new differences and inital values")
            .attr('x', 10)
            .attr('y', 40).style("font-size", "18px")
            return
        }
                     
        // Setting up colour scale
        var colours = ["#FF512F","#F09819"];
        var colourRange = d3.range(0, 1, 1.0 / (colours.length - 1));
        colourRange.push(1);

        //Create color gradient
        var colorScale = d3.scale.linear()
            .domain(colourRange)
            .range(colours)
            .interpolate(d3.interpolateHcl);

        //Needed to map the values of the dataset to the color scale
        var colorInterpolate = d3.scale.linear()
                                 .domain(d3.extent(data))
                                 .range([0,1]);
            
            
        svg.selectAll('circle').remove();
        svg.selectAll('text').remove();
        svg.append('text')
            .text(0)
            .attr('x',0)
            .attr('y',85)
            .fill("black")
        svg.append('text')
            .text(50)
            .attr('x',970)
            .attr('y',85)
            .fill("black")
    
        let points = svg.selectAll('points')
                        .data(eval(data))
                        .enter()
                        .append('circle')
                        .classed('points', true)
                        .attr('r', 10)
                        .attr('fill', 'black')
                        .attr('cx', 30)
                        .attr('cy', 20)
                        .transition()
                            .delay(function(d,i){return 5*i})
                            .duration(function(d,i){return 200*(i+1)})
                            .attr('cx', function(d) { return d*20; })
                            .attr('cy', 50)
                            .style("fill", function (d,i) { return colorScale(colorInterpolate(d)); });

        let text = svg.selectAll('.indicies')
                      .data(eval(data))
                      .enter()
                      .append('text')                        
                      .classed('indicies', true)
                      .attr("opacity", 0)
                      .text(d => d)
                      .attr('x', function(d) { return d*20; })
                      .attr('y', 50)
                      .attr('text-anchor',"middle")
                      .attr('alignment-baseline',"central")
                      .attr('class',"heavy")
                      .transition()
                          .delay(function(d,i){return 5*i})
                          .duration(function(d,i){return 200*(i+1)})
                          .attr("fill", "black")
                          .attr("opacity", 1)
});

})