var colors = ["red", "green", "blue", "gray", "yellow", "teal", "aqua", "purple", "silver", "lime"];
// Variables for drag_handler
var startX = 0,
    startY = 0,
    draggedCircleIndex = 0,
    draggedCircleColors = [],
    permutedSets = [],
    numberOfSetsAllowed = 0,
    tableComplete = false,
    scrollingThreshold = 6;

var drag_handler = d3.behavior.drag()
  .on("drag", dragged)
  .on("dragstart", dragstart)
  .on("dragend", dragend);

function dragged(d) {
  d3.select(this)
    .attr("cx", d3.event.x  )
    .attr("cy", d3.event.y  );
}

function dragstart(d) {
  startX = d.x
  startY = d.y;
  draggedCircleIndex = 0;
  for(var i = 1; i < numberOfCircles*2; i=i+2) {
    if(startX == drivingData[i].x && startY == drivingData[i].y) {
      draggedCircleIndex = i;
      break;
    }
  }
}

function dragend(d) {
  var circle = d3.select(this),
      endX = Number(circle.attr("cx")),
      endY = Number(circle.attr("cy"));

  if(endY < circleLineHeight || (startY > circleLineHeight && endY < circleLineHeight)) {
      d3transtionBack(drivingData, circle, draggedCircleIndex);
  }
  else {
    var startingIndex = numberOfCircles*2;
    for(var i = startingIndex; i < drivingData.length; ++i) {
      if(endX <= drivingData[i].x && Math.abs(drivingData[i].x-endX) < (distanceBetweenCircles/2)) {
        if(isOccupied(drivingData[i], drivingData, numberOfCircles)) {
          d3transtionBack(drivingData, circle, draggedCircleIndex);
        }

        else {
          d3transitionTo(drivingData, circle, draggedCircleIndex, i, checkForEnd);
        }
        break;
      }

      else if(endX > drivingData[i].x && Math.abs(drivingData[i].x-endX) < (distanceBetweenCircles/2)) {
        if(isOccupied(drivingData[i], drivingData, numberOfCircles)) {
          d3transtionBack(drivingData, circle, draggedCircleIndex);
        }

        else {
          d3transitionTo(drivingData, circle, draggedCircleIndex, i, checkForEnd);
        }
        break;
      }

      else if(endX > drivingData[i].x && i == drivingData.length-1) {
        if(isOccupied(drivingData[i], drivingData, numberOfCircles)) {
          d3transtionBack(drivingData, circle, draggedCircleIndex);
        }

        else {
          d3transitionTo(drivingData, circle, draggedCircleIndex, i, checkForEnd);
        }
        break;
      }
    }
  }
}

// Interactive svg variables
var radius = 20,
    distanceBetweenCircles = 80,
    startingXNode = 40,
    circleLineHeight = 100,
    slider = document.getElementById("perm-range-slider"),
    output = document.getElementById("slider-output"),
    permutedSetsTable = d3.select("#correct-permutations").select("table").style("width", "100%"),
    permutedSetsTableHead = permutedSetsTable.append("thead"),
    permutedSetsTableBody = permutedSetsTable.append("tbody"),
    answeringTimeout,
    drivingData = [],
    numberOfCircles = slider.value,
    numberOfSetsAllowed = factorial(numberOfCircles);

output.innerHTML = slider.value; // Display the default slider value
// Create svg
var svg = d3.select("#experiment-full")
  .append("svg")
    .attr("width", "80%")
    .attr("height", "300px")
  .append("g");

// Initialize data
drivingData = initData(numberOfCircles);
// Create original circles
createCircles(drivingData, svg, drag_handler, numberOfCircles);

// Update the current slider value (each time you drag the slider handle)
slider.oninput = function() {
    output.innerHTML = this.value;
    if(tableComplete) {
      drivingData = [];
      svg.selectAll("circle").data(drivingData).exit().remove();
      drivingData = initData(numberOfCircles);
      createCircles(drivingData, svg, drag_handler, numberOfCircles);
      tableComplete = false;
      d3.select("#circles1-answer").text("").style("background-color", "transparent");
    }

    resetSets(permutedSetsTable, permutedSets);
    permutedSets = [];

    if(this.value > numberOfCircles) {
      addCircle();
    }

    else {
      removeCircle();

    }
    numberOfSetsAllowed = factorial(numberOfCircles);
}

// Create circles given some data, a root object, a callback for dragging functionalilty, and the number of circles.
function createCircles(data, d3Object, dragFunc, nCircles) {
    var circles = d3Object.selectAll("circle")
      .data(data)
        .enter()
          .append("circle")
            .attr("cx", function(d) { return d.x; })
            .attr("cy", function(d) { return d.y; })
            .attr("r", radius)
            .attr("fill", function(d) { return d.color;})
            .style("stroke", function(d) { return d.border; });

    d3Object.selectAll("circle").filter(function(d, i) { return i % 2 == 1 && i < nCircles*2; }).call(drag_handler);
}

// After circles have been given a new position, update the circles position.
function updateCircles(data, d3obj, nCircles, subset) {
  var circles = d3obj.selectAll("circle")
    .data(data)
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("fill", function(d) { return d.color; })
        .style("stroke", function(d) { return d.border; });
}

// Add a circle to the interactive module
function addCircle() {
  var match,
      newColor,
      i = 0;

  do {
    match = drivingData.find(function(d) { return d.color == colors[i]});
    if(!match) {
      newColor = colors[i];
    }
    ++i;
  } while(match)

  var draggedCircles = [];
  if(numberOfCircles*3 < drivingData.length)
     draggedCircles = drivingData.slice(numberOfCircles*3, drivingData.length);

  var indexOfLastFull = (numberOfCircles*2) + 2;
  var indexOfLastCircle = indexOfLastFull + (numberOfCircles+1);
  for(var k = numberOfCircles*2; k < indexOfLastFull; ++k) {
      if(k == drivingData.length) {
        drivingData.push({ x: (numberOfCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight - 50, color: newColor, border: "none"});
      }
      else {
        drivingData[k] ={ x: (numberOfCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight - 50, color: newColor, border: "none"};
      }
  }

  ++numberOfCircles;
  var index = indexOfLastFull;
  for(var k = 0; k < numberOfCircles; ++k, ++index) {
    if(index == drivingData.length) {
      drivingData.push({ x:(k*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"});
    }

    else {
      drivingData[index] = { x: (k*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"};
    }
  }

  for(var i = 0; i < draggedCircles.length; ++i) {
    drivingData.push(draggedCircles[i]);
  }

  var answerText = d3.select("#circle1-answer");
  updateCircles(drivingData, svg, numberOfCircles);
  var circles = svg.selectAll("circle")
                .data(drivingData)
                  .enter()
                    .append("circle")
                      .attr("cx", function(d) { return d.x; })
                      .attr("cy", function(d) { return d.y; })
                      .attr("r", radius)
                      .attr("fill", function(d) { return d.color; })
                      .style("stroke", function(d) { return d.border});


  svg.selectAll("circle").filter(function(d,i) { return i % 2 == 1 && i < numberOfCircles*2; }).call(drag_handler);
  svg.selectAll("circle").filter(function(d, i) {
    return i >= numberOfCircles*3;
  })
  .on("click", function(d) { destroyElement(drivingData, svg, d, numberOfCircles); });
}

function addDraggedCircle(data, d3obj, nCircles, subset) {
  var draggableIndex = 0;
  if(subset) {
    draggableIndex = nCircles*2+subset;
  }

  else {
    draggableIndex = nCircles*3;
  }

  var dCircles = data.slice(draggableIndex, data.length);
  dCircles.sort(function(a, b) { return a.x-b.x; });

  for(var i = draggableIndex; i < data.length; ++i) {
    data[i] = dCircles[i - draggableIndex];
  }

  updateCircles(data, d3obj, nCircles, subset);
  var circles = d3obj.selectAll("circle")
  .data(data)
    .enter()
      .append("circle")
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("r", radius)
        .attr("fill", function(d) { return d.color; })
        .style("stroke", function(d) { return d.border});


  //svg.selectAll("circle").filter(function(d,i) { return i % 2 == 1 && i < draggableIndex; }).call(drag_handler);
  d3obj.selectAll("circle").filter(function(d, i) {
    return i >= draggableIndex;
  })
  .on("click", function(d) { destroyElement(data, d3obj, d, nCircles, subset); });
}

function removeCircle() {
  removeDraggedCircles();
  var indexToRemove = (numberOfCircles * 2) - 2;
  var circlesToRemove = 2;
  for(var i = 0; i < circlesToRemove; ++i) {
    drivingData.splice(indexToRemove, 1);
  }

  --numberOfCircles;

  drivingData.splice(numberOfCircles*3, 1);


  var answerText = d3.select("#circle1-answer");
  updateCircles(drivingData, svg, numberOfCircles);
  svg.selectAll("circle").data(drivingData).exit().remove();
}

function removeDraggedCircles() {
  var indexToRemove = numberOfCircles * 3;
  var colorToRemove = drivingData[(numberOfCircles*2) - 1].color;
  if(indexToRemove < drivingData.length) {
    var i;
    for(i = indexToRemove; i < drivingData.length; ++i) {
      if(drivingData[i].color == colorToRemove) {
          drivingData.splice(i, 1);
      }
    }
  }
}

function isOccupied(obj, data, nCircles, subset) {
  var draggedCircleIndex = 0;
  if(subset) {
    draggedCircleIndex = nCircles*2+subset;
  }

  else {
    draggedCircleIndex = nCircles*3;
  }
  if(draggedCircleIndex < data.length) {
      for(var i = draggedCircleIndex; i < data.length; ++i) {
        if(obj.x == data[i].x && obj.y == data[i].y) {
          return true;
        }
      }
  }

  return false;
}

function d3transtionBack(data, obj, objIndex) {
  obj.transition()
   .attr("cx", function() { return data[objIndex].x; })
   .attr("cy", function() { return data[objIndex].y; });
}

function d3transitionTo(data, obj, objIndex, toIndex, callback) {
  obj.transition()
    .attr("cx", function() { return data[objIndex].x = data[toIndex].x; })
    .attr("cy", function() { return data[objIndex].y = data[toIndex].y; })
    .each("end", function(d, i) {
      moveTo(data, objIndex, objIndex-1);
      createCopy(data, obj, data[toIndex].x, data[toIndex].y);
      callback();
    });
}

function areFull(data, nCircles, subset) {
  var draggableIndex;
  var fullThreshold;
  if(subset) {
    draggableIndex = (nCircles*2) + subset;
    fullThreshold = subset;
  }

  else {
    draggableIndex = nCircles*3;
    fullThreshold = nCircles;
  }


  if(draggableIndex < data.length) {
    if((data.length - draggableIndex) == fullThreshold) {
      return true;
    }
  }

  return false;
}

function isEmpty(data, nCircles, subset) {
  var draggableIndex = 0;
  if(subset) {
    draggableIndex = nCircles*2 + subset;
  }
  else {
    draggableIndex = nCircles*3;
  }
  if(draggableIndex < data.length)
    return false;

  return true;
}

function isPermutation(data, nCircles, subset) {
  var i;
  if(subset) {
    i = (nCircles*2) + subset
  }
  else {
    i = nCircles*3;
  }

  for(; i < data.length-1; ++i) {
    for(var j = i+1; j < data.length; ++j) {
      if(data[i].color == data[j].color) {
        return false;
      }
    }
  }

  return true;
}

function moveTo(data, objIndex, toIndex) {
  data[objIndex].x = data[toIndex].x;
  data[objIndex].y = data[toIndex].y;
}

function resetCircles() {
  drivingData.splice(numberOfCircles*3, numberOfCircles);
  svg.selectAll("circle").data(drivingData).exit().remove();
  d3.select("#reset-circles").style("display", "none");
  d3.select("#circles1-answer").text("")
                              .style("background-color", "transparent");
  slider.disabled = false;
  updateCircles(drivingData, svg, numberOfCircles);
  clearTimeout(answeringTimeout);
}

function createCopy(data, obj, atX, atY) {
  data.push({x: atX, y: atY, color: obj.data()[0].color, border: "none"});
}

function destroyElement(data, d3obj, obj, nCircles, subset) {
  var draggableIndex = 0;
  if(subset) {
    draggableIndex = nCircles*2+subset;
  }

  else {
    draggableIndex = nCircles*3;
  }
  for(var i = draggableIndex; i < data.length; ++i) {
    if(obj.x == data[i].x && obj.y == data[i].y) {
      data.splice(i, 1);
      break;
    }
  }

  updateCircles(data, d3obj, nCircles, subset);
  d3obj.selectAll("circle").data(data).exit().remove();
}

function checkForEnd() {
  addDraggedCircle(drivingData, svg, numberOfCircles);
  var answer = d3.select("#circles1-answer");
  if(areFull(drivingData, numberOfCircles)) {
    var resetButton = d3.select("#reset-circles");
    clearTimeout(answeringTimeout);
    if(isPermutation(drivingData, numberOfCircles)) {

      if(permutedSets.length == 0) {
        permutedSetsTable.append("caption").text("Permuted Sets Made")
                                    .style("color", "black");
      }

      var set = getSet(drivingData, numberOfCircles);
      var indexOfSet = setMade(permutedSets, set);
      if(indexOfSet < 0) {
        permutedSets.push(set);
        updateTable(permutedSetsTable, permutedSets);
        if(permutedSets.length >= scrollingThreshold) {
          d3.select("#correct-permutations").style("overflow-y", "scroll");
        }
        else {
          d3.select("#correct-permutations").style("overflow-y", "hidden");
        }

        if(permutedSets.length == numberOfSetsAllowed) {
          tableComplete = true;
          disableDrag(drivingData, svg, numberOfCircles);
          answer.text("You made all the different sets you can! Good job! You many scroll the slider to make a new set.");
          answer.style("background-color", "green");
        }
        else {
          answer.style("background-color", "green");
          answer.text("Correct.");
        }
      }

      else {

        displaySet(permutedSetsTableBody, permutedSets, indexOfSet);
        answer.text("Permutation has already been made. Try again.");
        answer.style("background-color", "red");
      }
    }
    else {
      if(areDuplicates(drivingData, numberOfCircles)) {
        answer.text("Incorrect. You cannot use the same circle twice as there are no repetitions in the original set");
      }

      answer.style("background-color", "red");
    }
    if(!tableComplete) {
      resetButton.style("display", "block");
      slider.disabled = true;
    }
  }


  else {
      if(answeringTimeout)
        clearTimeout(answeringTimeout);

      if(!isEmpty(drivingData, numberOfCircles)){
        answer.text("Permuting...");
        answer.style("background-color", "yellow");
        answeringTimeout = setTimeout(function() {
          answer.style("background-color", "red");
          answer.text("Incorrect. You need to complete the set.");
        }, 5000);
      }

    else {
      answer.text("");
      answer.style("background-color", "transparent");
    }
  }
}

function getSet(data, nCircles, subset) {
    var draggableIndex = 0;
    var set = [];
    if(subset) {
      draggableIndex = nCircles*2 + subset;
    }
    else {
      draggableIndex = nCircles*3;
    }

    for(var i = draggableIndex; i < data.length; ++i) {
      set.push(data[i].color);
    }

    return set;
}

function updateTable(table, data) {
  table.select("tbody")
        .selectAll("tr")
          .data(data)
            .enter()
              .append("tr")
                .style("background-color", "white")
                  .selectAll("td")
                    .data(function(d) { return d; })
                      .enter()
                        .append("td")
                          .text(function(d) { return d; })
                          .style("width", (100 / numberOfCircles).toString() + "%")
                          .style("height", "50px")
                          .style("text-align", "center")
                          .classed("rendered_html", false);
}

function resetSets(table, data) {
  data = [];
  table.select("caption").remove();

  var tableBody = table.select("tbody");

  tableBody.selectAll("tr")
    .data(data)
      .selectAll("td")
        .data(function(d) { return d; })
          .text(function(d) { return d; })

  tableBody.selectAll("tr")
    .data(data)
      .exit()
        .remove();
}

function setMade(data, set) {
  var checkCount = 0;
  for(var i = 0; i < data.length; ++i) {
    checkCount = 0;
    for(var j = 0; j < data[i].length; ++j) {
      if(data[i][j] == set[j]) {
        checkCount += 1;
        if(checkCount == data[i].length) {
          return i;
        }
      }
    }
  }
  return -1
}

function displaySet(svgObject, data, index) {
  var setToTransition = svgObject.selectAll("tr")
  .data(data)
    .filter(function(d,i) {
      return i == index;
    });

  setToTransition.transition()
    .duration(1500)
    .style("background-color", "green")
    .each("end", function() {
    setToTransition.transition()
              .duration(1000)
              .style("background-color", "white");
  })
}

function disableDrag(data, d3Object, nCircles) {
  d3Object.selectAll("circle").filter(function(d, i) {
    if(i % 2 == 1 && i < nCircles*2) {
      data.splice(i, 1);
      return true;
    }
  })
  .remove();
}

function initData(nCircles, subset) {
  var data = [];
  for(var i = 0; i < numberOfCircles; ++i) {
    data.push({x:(i*distanceBetweenCircles)+startingXNode, y: circleLineHeight-50, color:colors[i], border: "none" });
    data.push({x:(i*distanceBetweenCircles)+startingXNode, y: circleLineHeight-50, color:colors[i], border: "none" });
  }

  var numberOfFills = subset ? subset : nCircles;

  for(var i = 0; i < numberOfFills; ++i) {
    data.push({ x: (i*distanceBetweenCircles)+startingXNode, y: circleLineHeight+50, color: "none", border: "black" });
  }

  return data;
}

function factorial(num)
{
    var rval=1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}

function areDuplicates(data, nCircles, subset) {
  var draggedIndex = 0;
  if(subset) {
    draggedIndex = nCircles*2 + subset;
  }

  else {
    draggedIndex = nCircles*3;
  }

  var currentColors = colors.slice(0, numberOfCircles);
  var colorCount = 0;
  for(var i = 0; i < currentColors.length; ++i) {
    for(var j = draggedIndex; j < data.length; ++j) {
      if(currentColors[i] == data[j].color) {
        ++colorCount;
        if(colorCount > 1) {
          return true;
        }
      }
    }
  }

  return false;
}
