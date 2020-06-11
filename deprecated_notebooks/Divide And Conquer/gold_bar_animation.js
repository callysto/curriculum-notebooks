var svgWidth = 800,
    svgHeight = 400,
    numberOfBars = 7,
    spacing = 3
    barWidth = (svgWidth / 2) / ((numberOfBars+spacing) * 2), 
    barHeight = 100,
    data4 = [], // Split the data into two different categories, so we can make groups for transitions
    data2 = [],
    data1 = { };

var day_text = d3.select("body").append("p")
                            .text("Day 0")
                            .attr("id", "day-counter")
                            .style("width", svgWidth + "px")
                            .style("text-align", "center")
                            .style("font-size", "1.5em");

var title_container = d3.select("body").append("div")
                            .style("width", svgWidth + "px")
                            .style("display", "flex")
                            .style("justify-content", "space-between");

title_container.append("p").text("Available Gold").style("margin-left", "50px");

title_container.append("p").text("Paid to Worker").style("margin-right", "50px");


var svg = d3.select("body")
                .append("svg")
                    .attr("width", svgWidth)
                    .attr("height", svgHeight);

var offset = 0;
for(let i = 0; i < 4; ++i) {
    data4.push({x: (barWidth*offset) + barWidth, y: (svgHeight - ((svgHeight/2) + (barHeight/2))), width: barWidth, height: barHeight, color: "#FFDF00" });
    ++offset;
}

for(let i = 0; i < 2; ++i) {
    data2.push({x: (barWidth*offset) + barWidth, y: (svgHeight - ((svgHeight/2) + (barHeight/2))), width: barWidth, height: barHeight, color: "#FFDF00" })
    ++offset;
}

data1 = [ { x: (barWidth*offset) + barWidth, y: (svgHeight - ((svgHeight/2) + (barHeight/2))), width: barWidth, height: barHeight, color: "#FFDF00" } ]

svg.append("g").attr("id", "rect-4")
    .selectAll("rect")
        .data(data4)
            .enter()
                .append("rect")
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; })
                    .attr("width", function(d) { return d.width; })
                    .attr("height", function(d) { return d.height; })
                    .attr("id", "rect-4")
                    .style("fill", function(d) { return d.color; })
                    .style("stroke", "rgb(0,0,0)");

svg.append("g").attr("id", "rect-2")
    .selectAll("rect")
        .data(data2)
            .enter()
                .append("rect")
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; })
                    .attr("width", function(d) { return d.width; })
                    .attr("height", function(d) { return d.height; })
                    .style("fill", function(d) { return d.color; })
                    .style("stroke", "rgb(0,0,0)");

svg.append("g").attr("id", "rect-1")
    .selectAll("rect")
        .data(data1)
            .enter()
                .append("rect")
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; })
                    .attr("width", function(d) { return d.width; })
                    .attr("height", function(d) { return d.height; })
                    .style("fill", function(d) { return d.color; })
                    .style("stroke", "rgb(0,0,0)");

var workerHeight = svgHeight / 2,
    workerWidth = 100,
    workerX = svgWidth - workerWidth,
    workerY = svgHeight / 2,
    startingPaidPosition = (workerX - (workerWidth/2));

// Worker image
svg.append("image").attr("xlink:href", "worker.jpg")
                    .attr("width", workerWidth)
                    .attr("height", workerHeight)
                    .attr("x", workerX)
                    .attr("y", workerY - (workerHeight/2));

var buttonContainer = d3.select("body")
                            .append("div")
                                .attr("id", "gold-bar-btn-container")
                                .style("display", "flex")
                                .style("justify-content", "center")
                                .style("width", svgWidth + "px");

var cutButton = d3.select("#gold-bar-btn-container").append("input")
                    .attr("type", "button")
                    .attr("value", "Cut Bar")
                    .attr("onclick", "cut_bar_animation()");

var payButton = d3.select("#gold-bar-btn-container").append("input")
                    .attr("type", "button")
                    .attr("value", "Pay Worker")
                    .attr("onclick", "pay_worker_animation()")
                    .style("display", "none");

var complete_text = buttonContainer.append("p")
                        .text("The algorithm is complete!")
                        .style("display", "none");


function cut_bar_animation() {
    d3.select("#rect-1").selectAll("rect")
        .transition()
            .attr("x", function(d) {
                return d.x + (2*barWidth);
            })
            .duration(1000)
            .each("end", function() {
                d3.select("#rect-2").selectAll("rect")
                    .transition()
                    .attr("x", function(d) {
                        return d.x + barWidth;
                    })
                    .duration(1000)
                    .each("end", function() {
                        cutButton.style("display", "none");
                        payButton.style("display", "block");
                    })
            })
}

var day = 0;
function pay_worker_animation() {
    if(day === 0) {
        d3.select("#rect-1").select("rect")
            .transition()
                .attr("x", startingPaidPosition)
                .duration(1000)
        ++day;
        d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 1) {
        d3.select("#rect-1").select("rect")
        .transition()
            .attr("x", (numberOfBars+(spacing-1)) * barWidth)
            .duration(1000)
            .each("end", function() {
                d3.select("#rect-2").selectAll("rect")
                    .transition()
                        .attr("x", function(d, i) {
                            return startingPaidPosition - (barWidth * i);
                        })
                        .duration(1000)
            })
        
        ++day;
        d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 2) {
        d3.select("#rect-1").select("rect")
            .transition()
                .attr("x", startingPaidPosition - (barWidth * 3))
                .duration(1000);
    
        ++day;
        d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 3) {
        d3.select("#rect-2").selectAll("rect")
            .transition()
                .attr("x", function(d, i) {
                    return ((data4.length + spacing-1) * barWidth) + (barWidth*i);
                })
                .duration(1000)
                .each("end", function(d, i) {
                    d3.select("#rect-1").select("rect")
                        .transition()
                            .attr("x", (numberOfBars+(spacing-1)) * barWidth)
                            .duration(1000)
                            .each("end", function(d, i) {
                                d3.select("#rect-4").selectAll("rect")
                                    .transition()
                                        .attr("x", function(d, i) {
                                            return startingPaidPosition - (barWidth * i)
                                        })
                                        .duration(1000);
                            })

                })

            ++day;
            d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 4) {
        d3.select("#rect-1").select("rect")
            .transition()
                .attr("x", startingPaidPosition - (barWidth * (data4.length+1)))
                .duration(1000);

        ++day;
        d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 5) {
        d3.select("#rect-1").select("rect")
            .transition()
                .attr("x", ((spacing-1)) * barWidth)
                .duration(1000)
                .each("end", function() {
                    d3.select("#rect-2").selectAll("rect")
                        .transition()
                            .attr("x", function(d, i) {
                                return startingPaidPosition - (barWidth*(data4.length+2)) + (barWidth*i);
                            })
                            .duration(1000);
                })

        ++day;
        d3.select("#day-counter").text("Day " + day);
    }

    else if(day === 6) {
        d3.select("#rect-1").select("rect")
            .transition()
                .attr("x", startingPaidPosition - (barWidth * (data4.length + data2.length + 2)))
                .duration(1000);

        ++day;
        d3.select("#day-counter").text("Day " + day);
    }
}