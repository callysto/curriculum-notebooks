var combinationExercises = d3.select("#combination-exercises-container")

d3.json("./data/exercises.json", function(data) {
      let jsonArray = [];
      jsonLength = Object.keys(data).length;
      for(var i = 0; i < jsonLength; ++i) {
            jsonArray.push([])
            jsonArray[i].push((i+1).toString() + ") " + data[(i+1).toString()].question);
      }

    
    
      let exerciseDivs = combinationExercises.selectAll("div")
                            .data(jsonArray)
                                .enter()
                                    .append("div")
                                       .classed("clear-floats", true);

    exerciseDivs.selectAll("p")
        .data(function(d) { return d; })
            .enter()
                .append("p")
                    .text(function(d) { return d; });
    
    exerciseDivs.selectAll("input")
        .data(function(d) { return d; })
            .enter()
                .append("input")
                    .style("type", "text")
                    .style("float", "left")
                    .style("text-align", "center")
                    .classed("exercise-answers", true)
                    .classed("rendered_html", false);
    
    exerciseDivs.append("p")
                   .classed("exercise-feedback", true);
    
    exerciseDivs.append("div").classed("clear-floats", true);
});