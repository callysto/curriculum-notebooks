
var numberline = [...Array(5).keys()];

requirejs.config({
    paths: { 
        'd3': ['//cdnjs.cloudflare.com/ajax/libs/d3/3.5.6/d3'], 
    },                                         // strip .js ^, require adds it back
});

require(['d3'], function(d3){
    d3.select("#arithButton")
    .on("click", function(){
            initValue = parseInt(document.getElementById("frm2_initArith")
                                            .elements[0]
                                            .value);
            difference = parseInt(document.getElementById("frm1_diff")
                                            .elements[0]
                                            .value);

            if(initValue < 0 || initValue > 5 || difference == 0){
                svg2.selectAll('circle').remove();
                svg2.selectAll('text').remove();
                svg2.append('text').text("Oh no! The values you selected can't make a nice sequence, please select new differences and inital values")
                .attr('x', 10)
                .attr('y', 40).style("font-size", "18px")
                return
            }
        
            var data = [initValue]
            var svg2 = d3.select('#ARITH');
            if(difference){

                var data = [...Array(50).keys()]
                                .map( (num,i) => initValue + i*difference)
                                .filter(num => (num < 50))
                                .filter(num => (num > -1));
            }

            // Setting up colour scale
            var colours = ["#E55D87","#5FC3E4"];
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

            svg2.selectAll('circle').remove();
            svg2.selectAll('text').remove();
            svg2.append('text')
                .text(0)
                .attr('x',0)
                .attr('y',85)
                .fill("black")
            svg2.append('text')
                .text(50)
                .attr('x',970)
                .attr('y',85)
                .fill("black")

            let points = svg2.selectAll('points')
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

            let text = svg2.selectAll('.indicies')
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
                    .attr("opacity", 1)
                    .attr("fill", "black");
            
            });
    })