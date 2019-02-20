var answers = [];
var solutionsShowed = false;
d3.json("./data/p_choose_n.json", function(data) {
    for(var i = 0; i < data.length; ++i) {
        answers.push(data[i].answer);
    }
    columnNames = [ "available", "selected" ];
    function tabulate(data, columns) {
        var table = d3.select("#permutation-table");
        var thead = table.append("thead");
        var tbody = table.append("tbody");
        thead.append("tr")
            .selectAll("th")
                .data(columns)
                    .enter()
                        .append("th")
                            .text(function(d) { return d; })
                            .style("width", "15%")
                            .style("text-align", "center")
                            .classed(".rendered_html", false);
        thead.select("tr")
                .append("th")
                    .text("Answers")
                    .classed("hidden", true)
                    .classed(".rendered_html", false)
                    .style("text-align", "center")
                    .attr("id", "table-feedback-header")
                    .style("width", "20%");

        thead.select("tr")
                .append("th")
                    .text("Solutions")
                    .classed("hidden", true)
                    .classed(".rendered_html", false)
                    .attr("id", "table-solution-header")
                    .style("width", "50%")
                    .style("text-align", "center");
        
        var rows = tbody.selectAll("tr")
            .data(data)
                .enter()
                    .append("tr")
                    .style("text-align", "center")
                    .classed(".rendered_html", false);

        var cells = rows.selectAll('td')
            .data(function(row) {
                return columnNames.map(function(column) {
                    return {column: column, value: row[column] };
                })
            }).enter()
            .append("td")
                .text(function(d) { return d.value; })
                .classed(".rendered_html", false)
                .style("text-align", "center")
        
        rows.append("td")
                .append("input")
                .classed("table-answers", true)
                .style("text-align", "center")
                .classed(".rendered_html", false)
                .style("width", "100%");

        rows.append("td")
                .classed("table-feedback", true)
                .classed("hidden", true)
                .style("text-align", "center")
                .classed(".rendered_html", false);

        rows.append("td")
            .classed("table-solution", true)
            .classed("hidden", true)
            .style("text-align", "center")
            .classed(".rendered_html", false);

        return table;
    }

    tabulate(data, ['Number Of Circles', 'Number Of Slots', 'Number Of Ways To Rearrange']);
})

function showFeedback() {
    var correctIndexes = [];

    var correctAnswers = d3.selectAll(".table-answers")
        .filter(function(d, i) {
            if(checkAnswer(this, i)) {
                correctIndexes.push(i);
                return true;
            }
        });

    var incorrectIndexes = [];

    var incorrectAnswers = d3.selectAll(".table-answers")
        .filter(function(d, i) {
            if(!checkAnswer(this, i)) {
                incorrectIndexes.push(i);
                return true;
            }
        });
    
    var correctFeedback = d3.selectAll(".table-feedback")
        .filter(function(d, i) {
            for(var j = 0; j < correctIndexes.length; ++j) {
                if(i == correctIndexes[j]) {
                    return true;
                }
            }
        })
        .classed("correct", true)
        .classed("hidden", false)
        .classed("incorrect", false)
        .text("Correct!");


        var incorrectFeedback = d3.selectAll(".table-feedback")
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
        .text("Incorrect.");
        var showSolutionsButton = d3.select("#show-solutions-button");
        var unshowSolutionsButton = d3.select("#unshow-solutions-button");
        if(unshowSolutionsButton.classed("hidden") && showSolutionsButton.classed("hidden"))
            d3.select("#show-solutions-button").classed("hidden", false);
    
        var feedbackHeader = d3.select("#table-feedback-header");
        if(feedbackHeader.classed("hidden")) {
           feedbackHeader.classed("hidden", false);
        }
}

function checkAnswer(obj, i, indexes) {
    return obj.value == answers[i];
}

function showTableSolution() {
    if(!solutionsShowed) {
        solutionsShowed = true;
        d3.json("./data/pchoosenData.json", function(data) {
            d3.selectAll(".table-solution")
                .classed("hidden", false)
                    .data(data)
                        .text(function(d) {
                            var numerator = d.available.toString();
                            var denominator = (d.available - d.selected).toString();
                            for(var i = d.available-1; i >= 1; --i) {
                                numerator += " * " + i;
                            }

                            for(var i = (d.available-d.selected)-1; i >= 1; --i) {
                                denominator += " * " + i;
                            }
                            return "$$_" + d.available + "P_" + d.selected + " = \\frac{" + d.available + "!}{(" + d.available + "-" + d.selected + ")!} = \\frac{" + numerator + "}{" + denominator + "} = " + d.answer + "$$";
                        });

            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        });
    }

    else {
        d3.json("pchoosenData.json", function(data) {
            d3.selectAll(".table-solution")
                .classed("hidden", false)
                    .data(data)
                        .text(function(d) {
                            var numerator = d.available.toString();
                            var denominator = (d.available - d.selected).toString();
                            for(var i = d.available-1; i >= 1; --i) {
                                numerator += " * " + i;
                            }

                            for(var i = (d.available-d.selected)-1; i >= 1; --i) {
                                denominator += " * " + i;
                            }
                            return "$$_" + d.available + "P_" + d.selected + " = \\frac{" + d.available + "!}{(" + d.available + "-" + d.selected + ")!} = \\frac{" + numerator + "}{" + denominator + "} = " + d.answer + "$$";
                        });

            MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
        });
    }
    d3.select("#table-solution-header").classed("hidden", false);
    d3.select("#show-solutions-button").classed("hidden", true);
    d3.select("#unshow-solutions-button").classed("hidden", false);
}

function unshowTableSolution() {
    d3.selectAll(".table-solution").classed("hidden", true);
    d3.select("#table-solution-header").classed("hidden", true);
    d3.select("#unshow-solutions-button").classed("hidden", true);
    d3.select("#show-solutions-button").classed("hidden", false);
}