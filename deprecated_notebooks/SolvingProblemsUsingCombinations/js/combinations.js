let rectWidth = 50;
let rectHeight = 50;
let numberOfRows = 7;
let svg;
$(document).ready(function() {
    svg = initializeSvg("#pascals-triangle-container", "400", "400").style("margin-left", "30%")
                                                                        .style("margin-top", "50px");

    pascalTriangleData = createPascalData(svg, numberOfRows);
    buildPascalsTriangle(svg, pascalTriangleData);
});

function initializeSvg(containerId, width, height) {
    var svg = d3.select(containerId).append("svg")
                            .attr("width", width)
                            .attr("height", height);
    return svg;
}

function buildPascalsTriangle(svgObj, data) {
    svgObj.selectAll("rect")
        .data(data)
            .enter()
                .append("rect")
                    .attr("width", rectWidth)
                    .attr("height", rectHeight)
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; })
                    .attr("fill", "white")
                    .classed("pascal-element", true)
                    .on("mouseover", handleMouseOver)
                    .on("mouseout", handleMouseOut);

    svgObj.selectAll("text")
        .data(data)
            .enter()
                .append("text")
                    .attr("x", function(d) { return d.x + (rectWidth/2)-5; })
                    .attr("y", function(d) { return d.y + (rectHeight/2)+5; })
                    .text(function(d) { return d.value; })
                    .on("mouseover", handleMouseOver)
                    .on("mouseout", handleMouseOut);
}

function handleMouseOver(d, i) {
    let row = findRowOfElement(i);
    var sumRects = svg.selectAll("rect").filter(function(d, ind) {
        if(isLeftEdge(i)) {
            return ind == ((i - row) + 1);
        }

        else if(isRightEdge(i)) {
            return ind == (i - row);
        }

        else {
            return ind == (i - row) || ind == (i - row + 1);
        }
    })
    .transition()
    .duration(1000)
    .attr("fill", "orange");
}

function buildPascalsTriangleSolutions(svgObj, data) {
    svgObj.selectAll("text")
        .data(data)
            .enter()
                .append("text")
                    .attr("x", function(d) { return d.x; })
                    .attr("y", function(d) { return d.y; })
                    .text(function(d) { return d.value; })
}

function handleMouseOut(d, i) {
    let row = findRowOfElement(i);
    var sumRects = svg.selectAll("rect").filter(function(d, ind) {
        if(isLeftEdge(i)) {
            return ind == ((i - row) + 1);
        }

        else if(isRightEdge(i)) {
            return ind == (i - row);
        }

        else {
            return ind == (i - row) || ind == (i - row + 1);
        }
    })
    .transition()
    .duration(1000)
    .attr("fill", "white");
}

function scaled3Objects(d3Objects, scaleX, scaleY) {
    if(scaleY) {
        d3Objects.scale(scaleX, scaleY);
    }

    else if(scaleX) {
        d3Objects.scale(scaleX);
    }

    else {
        console.log("You must specify a number to scale by!")
    }
}

function createPascalData(svgObj, numberOfRows) {
    data = [];
    let startingX = Number(svgObj.attr("width")) / 2;

    let row = 1;
    let i = 0;
    while(row <= numberOfRows) {
        if(i == 0 || i == row-1) {
            data.push({ value: 1, x: startingX - ((rectWidth/2)*row) + (rectWidth*i), y: rectHeight*(row-1) });
        }

        else {
            let previousRow = findStartingIndex(row-1);
            data.push({ value: data[previousRow+(i-1)].value + data[previousRow+i].value, x: startingX - ((rectWidth/2)*row) + (rectWidth*i), y: rectHeight*(row-1) });
        }

        if(i == row-1) {
            i = 0;
            ++row;
        }

        else 
            ++i;
    }

    return data;
}

function createPascalSolutionData(svgObj, numberOfRows) {
    data = [];
    let startingX = Number(svgObj.attr("width")) / 2;

    let row = 0;
    let i = 0;
    while(row < numberOfRows) {
        let answer = factorial(row) / (factorial(i) * factorial(row - i));
        console.log(startingX - ((rectWidth/2) * (row+1)) + (rectWidth*i));
        data.push({ value: answer, x: startingX - ((rectWidth/2)*(row+1)) + (rectWidth*i), y: 35*(row) + 20 });


        if(i == row) {
            i = 0;
            ++row;
        }

        else 
            ++i;
    }

    console.log(data);
    return data;
}

function findStartingIndex(rowNumber) {
    if(rowNumber == 1) {
        return 0;
    }

    return findStartingIndex(rowNumber-1) + rowNumber-1;
}

function findRowOfElement(elementIndex) {
    if(elementIndex == 0) {
        return 1;
    }

    else {
        let row = 2;
        let left = 1;
        let right = row;

        while(row <= numberOfRows) {
            if(elementIndex >= left && elementIndex <= right)
                return row;

            else {
                ++row;
                left = right + 1;
                right += row;
            }
        }
    }

    return -1;
}

function isLeftEdge(elementIndex) {
    let row = findRowOfElement(elementIndex);
    let sum = 1; // first left edge
    let i = 2;
    while(i < row) {
        sum += i;
        ++i;
    }

    return sum == elementIndex;
}

function isRightEdge(elementIndex) {
    let row = findRowOfElement(elementIndex);
    let sum = 2; // first right edge
    let i = 3; 
    while(i <= row) {
        sum += i;
        ++i;
    }

    return sum == elementIndex;
}

function createCombinationTable(data) {
    let tableContainer = d3.select("#n-choose-r-table-container");
    let table = tableContainer.append("table");
    let thead = table.append("thead");
    let tbody = table.append("tbody");
    
    theadData = [-1, 0];

    thead.append("tr")
        .selectAll("th")
            .data(theadData)
                .enter()
                    .append("th")
                        .text(function(d) {
                            if(d == -1)
                                return "";
                            
                            return "$\\textit{r} = $ " + d;
                        })
                        .classed("rendered_html", false)
                        .style("text-align", "center");

    tbody.selectAll("tr")
        .data(data)
            .enter()
                .append("tr")
                    .selectAll("td")
                        .data(function(d) { return d; })
                            .enter()
                                .append("td")
                                    .style("width", "70px")
                                        .append("p")
                                            .text(function(d) {
                                                    if(d.r == -1)
                                                        return "$\\textit{n} = $ " + d.n;
                                                    else if(d.n == -1) 
                                                        return "$\\textit{r} = $ " + d.r;

                                                    return "$_" + d.n + "C_" + d.r +"$" 
                                                })
                                                .classed("rendered_html", false)
                                                .style("text-align", "center");

    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);

    tbody.selectAll("tr")
            .selectAll("td")
                .selectAll("p")
                    .filter(function(d) {
                        return d.n != -1 && d.r != -1;
                    })
                    .on("click", tableElementClicked);
}

function tableElementClicked(d, i) {
    let parentNode = d3.select(this.parentNode);
    this.remove();
    let input = parentNode.append("input")
                .attr("type", "text")
                .attr("width", "20px")
                .classed("table-input", true);

    input.node().focus();
}

function createCombinationData(nrows) {
    let n = 0;
    let r = 0;
    let data = [ [{n: n, r: -1}] ];
    while(n < nrows) {
        data[n].push({n: n, r: r});
        if(n == r) {
            ++n;
            if(n < nrows) {
                data[n-1].push({n:-1, r:r+1})
            }
            r = 0;
            if(n != nrows) {
                data.push([]);
                data[data.length-1].push({n: n, r: -1});
            }
        }

        else {
            ++r;
        }

    }

    console.log(data);
    return data;
}

function checkTable() {  
    let message = "";
    let minIncrease = 3;
    let maxIncrease = 4;
    let indexSubtractor = 1;
    let min = 1;
    let max = 2;
    
    let answeredQuestions = d3.select("#n-choose-r-table-container").selectAll("td").filter(function(d, i) {
         let tableContent = d3.select(this);
         if($(this).children().eq(0).is("input")) {
             if(i >= max) {
                min += minIncrease;
                max += maxIncrease;
                ++minIncrease;
                ++maxIncrease;
                indexSubtractor += 2;
             }
             
             if(i >= min && i < max) {
                 let correctIndex = i - indexSubtractor;
                 let n = findRowOfElement(correctIndex) - 1;
                 let r = correctIndex - findStartingIndex(n+1);
                 let correctAnswer = factorial(n) / (factorial(r) * factorial(n-r));
                 if(this.children[0].value == correctAnswer) {
                     tableContent.transition().style("background-color", "green");
                     return true;
                 }
             
                 message = "Some answers were incorrect and labelled in red. Please try again.";
                 tableContent.transition().style("background-color", "red");
                 return false;
             }
             
         }
    });
    
    d3.select("#show-table-solutions-button").classed("hidden", false);
}

function showTableSolutions() {
    d3.select("#show-table-solutions-button").style("display", "none");
    
    let svg = d3.select("#pascal-triangle-solutions-container").append("svg")
                                                                .attr("width", 400)
                                                                .attr("height", 250)
                                                                .style("margin-left", "25%");
    
    
    let solutionData = createPascalSolutionData(svg, numberOfRows);
    
    buildPascalsTriangleSolutions(svg, solutionData);
    
    let detailedSolutionData = createTableSolutionData(numberOfRows);
    let solutionTable = d3.select("#detailed-table-solutions").append("table").style("width", "100%");
    let tableBody = solutionTable.append("tbody");
    tableBody.selectAll("tr")
        .data(detailedSolutionData)
            .enter()
                .append("tr")
                    .selectAll("td")
                        .data(function(d) { return d; })
                            .enter()
                                .append("td")
                                    .text(function(d) { return d; })
                                    

    MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
}

function createTableSolutionData(numberOfRows) {
    let data = [ [] ];
    let n = 0;
    let r = 0;
    
    while(n < numberOfRows) {
        let answer = factorial(n) / (factorial(r) * factorial(n-r));
        data[n].push("$_" + n + "C_" + r + " = \\frac{" + n + "!}{" + r + "!" + (n-r) + "!} = " + answer + "$");
        if(r == n) {
           r = 0;
           ++n;
           data.push([]);
        }
        
        else {
           ++r;
        }
    }
    
    return data;
}

function checkExercises() {
    let answers = d3.selectAll(".exercise-answers");
    
    d3.json("./data/exercises.json", function(data) {
        let jsonArray = [];
        jsonLength = Object.keys(data).length;
        for(let i = 0; i < jsonLength; ++i) {
            jsonArray.push(data[(i+1).toString()].answer);
        }
    
    
        let feedback = d3.selectAll(".exercise-feedback")
        
        let correctAnswers = answers.filter(function(d,i) {
            if(this.value == "")
                 return false;
            
            let answer = this.value.toLowerCase();
            
            if(answer == jsonArray[i]) {
                d3.select(feedback[0][i])
                              .classed("hidden", false)
                              .classed("green", true)
                              .classed("red", false)
                              .text("Correct!");
                return true;
            }
            
            console.log("Incorrect.");
            d3.select(feedback[0][i])
                        .classed("hidden", false)
                        .classed("green", false)
                        .classed("red", true)
                        .text("Incorrect");

            
        });
    });
    
    answeredQuestions = answers.filter(function(d) { 
        if(this.value == "")
            return false;
        
        return true;
    });
    
    if(answeredQuestions[0].length >= 3) {
        d3.select("#show-exercise-solutions-button").classed("hidden", false);
        d3.select("#exercise-error-message").classed("hidden", true);
    }
    else
        d3.select("#exercise-error-message").classed("hidden", false)
                                            .text("You must answer at least 3 questions before seeing the solutions.")
                                            .classed("red", true);
}

function showExerciseSolutions() {
    let exerciseContainer = d3.select("#combination-exercises-solutions-container");
    
    d3.json("./data/exercises.json", function(data) {
        let jsonArray = [];
        jsonLength = Object.keys(data).length;
        for(let i = 0; i < jsonLength; ++i) {
            jsonArray.push([]);
            jsonArray[i].push(data[(i+1).toString()].explaination);
            if(data[(i+1).toString()].solution != "")
                jsonArray[i].push(data[(i+1).toString()].solution);
        }
        
        let questionNumber = 1;
        exerciseContainer.selectAll("div")
                      .data(jsonArray)
                             .enter()
                                .append("div")
                                        .classed("exercise-solution-container", true)
                                            .selectAll("p")
                                                .data(function(d) { return d; })
                                                     .enter()
                                                          .append("p")
                                                              .text(function(d, i) {
                                                                        if(i == 0)
                                                                            return questionNumber++ + ") " + d;
                                                                        else
                                                                            return d;
                                                                });
        
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    });
}

function factorial(num)
{
    var rval=1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}