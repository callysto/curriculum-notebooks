createQuestions();

function createQuestions() {
    d3.json("./data/restriction_solutions.json", function(data) {
        var jsonArray = [];
        jsonLength = Object.keys(data).length;
        for(var i = 0; i < jsonLength; ++i) {
            jsonArray.push([])
            jsonArray[i].push((i+1).toString() + ") " + data[(i+1).toString()].question);
        }

        var exerciseDivs = d3.select("#restriction-questions-container")
            .selectAll("div");
        
        exerciseDivs.data(jsonArray)
                    .enter()
                        .append("div")
                            .classed("restriction-exercise-container", true)
                                .selectAll("p")
                                    .data(function(d) { return d; })
                                        .enter()
                                            .append("p")
                                                .text(function(d) { return d; });
        

        d3.select("#restriction-questions-container")
            .selectAll("div")
                .data(jsonArray)
                    .append("input")
                        .attr("type", "text")
                        .classed("restriction-answers", true);

        d3.select("#restriction-questions-container")
            .selectAll("div")
                .data(jsonArray)
                    .append("p")
                        .classed("hidden", true)
                        .classed("restriction-feedback", true);

        d3.select("#restriction-questions-container")
            .selectAll("div")
                .data(jsonArray)
                    .append("div")
                        .classed("clear-float", true);

        d3.select("#restriction-questions-container")
            .append("div")
                .attr("id", "restrictions-button-container");
        
        d3.select("#restrictions-button-container")
            .append("input")
                .attr("type", "button")
                .attr("value", "Submit Answers")
                .attr("onclick", "submitRestrictions()")
                .attr("id", "submit-restrictions-button");

        d3.select("#restrictions-button-container")
            .append("input")
                .attr("type", "button")
                .attr("value", "Show Solutions")
                .attr("onclick", "showRestrictionSolutions()")
                .attr("id", "restriction-solutions-button")
                .classed("hidden", true);

        d3.select("#restriction-questions-container")
            .append("div")
                .classed("clear-float", true);
});
}

function submitRestrictions() {
    d3.json("./data/restriction-solutions.json", function(data) {
        var correctIndexes = [];
        var correctAnswers = d3.selectAll(".restriction-answers")
                                .filter(function(d, i) {
                                   if(this.value == parseInt(data[(i+1).toString()].answer, 10))
                                         correctIndexes.push(i);
                                });
        
        var incorrectIndexes = [];
        var incorrectAnswers = d3.selectAll(".restriction-answers")
                                    .filter(function(d, i) {
                                       if(this.value != parseInt(data[(i+1).toString()].answer, 10))
                                         incorrectIndexes.push(i);
                                    });
        console.log(correctIndexes);
        console.log(incorrectIndexes);
        var correctFeedback = d3.selectAll(".restriction-feedback")
                                .filter(function(d, i) {
                                   for(var j = 0; j < correctIndexes.length; ++j) {
                                      if(i == correctIndexes[j]) {
                                          return true;
                                      }
                                   }
                                })
                                .classed("correct", true)
                                .classed("incorrect", false)
                                .classed("centered", true)
                                .classed("hidden", false)
                                .classed("rendered_html", false)
                                .style("text-align", "center")
                                .text("Correct!");
 
        var incorrectFeedback = d3.selectAll(".restriction-feedback")
                                .filter(function(d, i) {
                                   for(var j = 0; j < incorrectIndexes.length; ++j) {
                                      if(i == incorrectIndexes[j]) {
                                          return true;
                                      }
                                   }
                                })
                                .classed("incorrect", true)
                                .classed("correct", false)
                                .classed("hidden", false)
                                .classed("rendered_html", false)
                                .style("text-align", "center")
                                .text("Incorrect.");
        
        console.log(incorrectFeedback);
        
        d3.select("#restriction-solutions-button").classed("hidden", false);
      });
 }
 
 function showRestrictionSolutions() {
     d3.json("./data/restriction-solutions.json", function(data) {
          var jsonArray = [];
          jsonLength = Object.keys(data).length;
          jsonKeysLength = Object.keys(data["1"]).length - 1;
          for(var i = 0; i < jsonLength; ++i) {
              jsonArray.push([]);
              jsonArray[i].push(data[(i+1).toString()].explaination);
              jsonArray[i].push(data[(i+1).toString()].solution);
          }
          
         console.log(jsonArray);
          d3.select("#restriction-solutions-container")
              .classed("hidden", false)
                  .selectAll("div")
                     .data(jsonArray)
                         .enter()
                             .append("div")
                                 .classed("restriction-solutions", true)
                                     .selectAll("p")
                                         .data(function(d) { return d; })
                                             .enter()
                                                 .append("p")
                                                     .text(function(d) { return d; });
         
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
     });
 }