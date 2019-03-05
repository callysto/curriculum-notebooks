colors = [ "green", "blue", "red", "yellow", "cyan"];
var radius = 20;
var distanceBetweenCircles = 80;
var startingXNode = 40;
var circleLineHeight = 100;
var sliderFull = document.getElementById("perm-fullsubset-range-slider");
var sliderFill = document.getElementById("perm-fillsubset-range-slider");
var outputFull = document.getElementById("slider-full-output");
var outputFill = document.getElementById("slider-fill-output");
var permutedSetsTable_subset = d3.select("#correct-subset-permutations-table").style("width", "100%");
var permutedSetsTableBody_subset = d3.select("#correct-subset-permutations-table").append("tbody");
var subsetAnsweringTimeout;
var tableComplete_subset = false;

var drivingSubsetData = [];
var draggedCircles_subset = [];
var permutedSets_subset = [];
var numberOfFullCircles = Number(sliderFull.value);
var numberOfFillCircles = Number(sliderFill.value);
var numberOfSetsAllowed_subset = factorial(numberOfFullCircles) / (factorial(numberOfFillCircles) * factorial(numberOfFullCircles - numberOfFillCircles));
var tableComplete_subset = false;

var startX = 0;
var startY = 0;
var draggedCircleIndex = 0;

var subset_drag_handler = d3.behavior.drag()
  .on("drag", function(d) {
        d3.select(this)
          .attr("cx", d3.event.x  )
          .attr("cy", d3.event.y  );
  })
  .on("dragstart", function(d) {
    startX = d.x
    startY = d.y;
    draggedCircleIndex = 0;
    for(var i = 1; i < numberOfFullCircles*2; i=i+2) {
      if(startX == drivingSubsetData[i].x && startY == drivingSubsetData[i].y) {
        draggedCircleIndex = i;
        console.log(draggedCircleIndex);
        break;
      }
    }
  })
  .on("dragend", function(d) {
    var circle = d3.select(this);
    console.log(circle);
    var endX = Number(circle.attr("cx"));
    var endY = Number(circle.attr("cy"));
    console.log("endX" + endX + " endY " + endY);
    if(endY < circleLineHeight || (startY > circleLineHeight && endY < circleLineHeight)) {
      d3transtionBack(drivingSubsetData, circle, draggedCircleIndex);
    }
    else {
      var startingIndex = numberOfFullCircles*2;
      for(var i = startingIndex; i < drivingSubsetData.length; ++i) {
        if(endX <= drivingSubsetData[i].x && Math.abs(drivingSubsetData[i].x-endX) < (distanceBetweenCircles/2)) {
          if(isOccupied(drivingSubsetData[i], drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
            d3transtionBack(drivingSubsetData, circle, draggedCircleIndex);
          }

          else {
            d3transitionTo(drivingSubsetData, circle, draggedCircleIndex, i, checkForSubsetEnd);
          }
          break;
        }

        else if(endX > drivingSubsetData[i].x && Math.abs(drivingSubsetData[i].x-endX) < (distanceBetweenCircles/2)) {
          if(isOccupied(drivingSubsetData[i], drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
            d3transtionBack(drivingSubsetData, circle, draggedCircleIndex);
          }

          else {
            d3transitionTo(drivingSubsetData, circle, draggedCircleIndex, i, checkForSubsetEnd)
          }
          break;
        }

        else if(endX > drivingSubsetData[i].x && i == drivingSubsetData.length-1) {
          if(isOccupied(drivingSubsetData[i], drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
            d3transtionBack(drivingSubsetData, circle, draggedCircleIndex);
          }

          else {
            d3transitionTo(drivingSubsetData, circle, draggedCircleIndex, i, checkForSubsetEnd)
          }
          break;
        }
      }
    }

  });

for(var i = 0; i < numberOfFullCircles; ++i) {
  drivingSubsetData.push({x:(i*distanceBetweenCircles)+startingXNode, y: circleLineHeight-50, color:colors[i], border: "none" });
  drivingSubsetData.push({x:(i*distanceBetweenCircles)+startingXNode, y: circleLineHeight-50, color:colors[i], border: "none" });
}

for(var i = 0; i < numberOfFillCircles; ++i) {
  drivingSubsetData.push({ x: (i*distanceBetweenCircles)+startingXNode, y: circleLineHeight+50, color: "none", border: "black" });
}

outputFull.innerHTML = sliderFull.value; // Display the default slider value
outputFill.innerHTML = sliderFill.value;
// Create svg
var subsetSvg = d3.select("#experiment-subset")
  .append("svg")
    .attr("width", "100%")
    .attr("height", "300px")
  .append("g");

// Create original circles
createCircles(drivingSubsetData, subsetSvg, subset_drag_handler, numberOfFullCircles);

// Update the current slider value (each time you drag the slider handle)
sliderFull.oninput = function() {
    outputFull.innerHTML = this.value;
    if(tableComplete_subset) {
      drivingSubsetData = [];
      subsetSvg.selectAll("circle").data(drivingSubsetData).exit().remove();
      drivingSubsetData = initData(numberOfFullCircles, numberOfFillCircles);
      createCircles(drivingData, svg, drag_handler, numberOfCircles);
      tableComplete_subset = false;
    }

    resetSets(permutedSetsTable_subset, permutedSets);
    permutedSets_subset = [];

    if(this.value > numberOfFullCircles) {
      addFullCircle();
    }

    else {
      removeFullCircle();
    }
    numberOfSetsAllowed_subset = factorial(numberOfFullCircles) / factorial(numberOfFullCircles - numberOfFillCircles);
    clearTimeout(subsetAnsweringTimeout);
        var answer = d3.select("#circles-subset-answer").text("").style("background-color", "transparent");
    answer.text("");
}

sliderFill.oninput = function() {
    outputFill.innerHTML = this.value;
    if(tableComplete_subset) {
      drivingSubsetData = [];
      subsetSvg.selectAll("circle").data(drivingSubsetData).exit().remove();
      drivingSubsetData = initData(numberOfFullCircles, numberOfFillCircles);
      createCircles(drivingData, svg, drag_handler, numberOfCircles);
      tableComplete_subset = false;
    }

    resetSets(permutedSetsTable_subset, permutedSets);
    permutedSets_subset = [];

    if(this.value > numberOfFillCircles) {
      addFillCircle();
    }

    else {
      removeFillCircle();
    }
    numberOfSetsAllowed_subset = factorial(numberOfFullCircles) / factorial(numberOfFullCircles - numberOfFillCircles);
    clearTimeout(subsetAnsweringTimeout);
    var answer = d3.select("#circles-subset-answer").text("").style("background-color", "transparent");
    answer.text("");
}

function addFullCircle() {
    var match;
    var newColor;
    var i = 0;
    do {
      match = drivingSubsetData.find(function(d) { return d.color == colors[i]});
      if(!match) {
        newColor = colors[i];
      }
      ++i;
    } while(match)
  
    var draggedCircles = [];
    var draggedCircleIndex = (numberOfFullCircles*2)+numberOfFillCircles;
    if(draggedCircleIndex < drivingSubsetData.length)
       draggedCircles = drivingSubsetData.slice(draggedCircleIndex, drivingSubsetData.length);

    var indexOfLastFull = (numberOfFullCircles*2) + 2;
    for(var k = numberOfFullCircles*2; k < indexOfLastFull; ++k) {
        if(k == drivingSubsetData.length) {
          drivingSubsetData.push({ x: (numberOfFullCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight - 50, color: newColor, border: "none"});
        }
        else {
          drivingSubsetData[k] = { x: (numberOfFullCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight - 50, color: newColor, border: "none"};
        }
    }

    var index = indexOfLastFull;
    for(var k = 0; k < numberOfFillCircles; ++k, ++index) {
        if(index == drivingSubsetData.length) {
            drivingSubsetData.push({ x:(k*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"});
        }
    
        else {
            drivingSubsetData[index] = { x: (k*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"};
        }
    }
    
    for(var i = 0; i < draggedCircles.length; ++i) {
      drivingSubsetData.push(draggedCircles[i]);
    }

    updateCircles(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);

    ++numberOfFullCircles;
    var circles = subsetSvg.selectAll("circle")
                .data(drivingSubsetData)
                    .enter()
                    .append("circle")
                        .attr("cx", function(d) { return d.x; })
                        .attr("cy", function(d) { return d.y; })
                        .attr("r", radius)
                        .attr("fill", function(d) { return d.color; })
                        .style("stroke", function(d) { return d.border});


    subsetSvg.selectAll("circle").filter(function(d,i) { return i % 2 == 1 && i < numberOfFullCircles*2; }).call(subset_drag_handler);
    subsetSvg.selectAll("circle").filter(function(d, i) {
      return i >= numberOfFullCircles*2+numberOfFillCircles;
    })
    .on("click", function(d) { destroyElement(drivingSubsetData, subsetSvg, d, numberOfFullCircles, numberOfFillCircles); });
}

function addFillCircle() {
    var draggedCircleIndex = numberOfFullCircles*2+numberOfFillCircles;
    var draggedCircles = drivingSubsetData.slice(draggedCircleIndex, drivingSubsetData.length);
    if(draggedCircles.length == 0) {
      drivingSubsetData.push({ x:(numberOfFillCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"});
    }
    else {
      drivingSubsetData[draggedCircleIndex++] =  { x:(numberOfFillCircles*distanceBetweenCircles) + startingXNode, y: circleLineHeight + 50, color: "none", border: "black"};
      for(var i = 0; i < draggedCircles.length; ++i) {
        if(i == drivingSubsetData.length) {
          drivingSubsetData.push(draggedCircles[i])
        }
        else {
          drivingSubsetData[draggedCircleIndex++] = draggedCircles[i];
        }
      }
    }
    ++numberOfFillCircles;
    updateCircles(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
    var circles = subsetSvg.selectAll("circle")
      .data(drivingSubsetData)
          .enter()
          .append("circle")
              .attr("cx", function(d) { return d.x; })
              .attr("cy", function(d) { return d.y; })
              .attr("r", radius)
              .attr("fill", function(d) { return d.color; })
              .style("stroke", function(d) { return d.border});

    subsetSvg.selectAll("circle").filter(function(d, i) {
      return i >= numberOfFullCircles*2+numberOfFillCircles;
    })
    .on("click", function(d) { destroyElement(drivingSubsetData, subsetSvg, d, numberOfFullCircles, numberOfFillCircles); });
}

function removeFullCircle() {
    var indexToRemove = (numberOfFullCircles*2) - 2;
    var colorToRemove = drivingSubsetData[indexToRemove].color;

    drivingSubsetData.splice(indexToRemove, 2);
    --numberOfFullCircles;
    draggedCircleIndex = numberOfFullCircles*2+numberOfFillCircles;
    if(draggedCircleIndex < drivingSubsetData.length) {
      for(var i = draggedCircleIndex; i < drivingSubsetData.length; ++i) {
        if(drivingSubsetData[i].color == colorToRemove) {
          drivingSubsetData.splice(i--, 1);
        }
      }
    }

    subsetSvg.selectAll("circle").data(drivingSubsetData).exit().remove();
    updateCircles(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
}

function removeFillCircle() {
    var indexToRemove = (numberOfFullCircles*2+numberOfFillCircles) - 1;
    for(var i = numberOfFullCircles*2+numberOfFillCircles; i < drivingSubsetData.length; ++i) {
        if(drivingSubsetData[indexToRemove].x == drivingSubsetData[i].x && drivingSubsetData[indexToRemove].y == drivingSubsetData[i].y) {
            drivingSubsetData.splice(i, 1);
            break;
        }
    }
    drivingSubsetData.splice(indexToRemove, 1);
    --numberOfFillCircles;
    updateCircles(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
    subsetSvg.selectAll("circle").data(drivingSubsetData).exit().remove();
}

  
function resetCircles_subset() {
  draggedCircleIndex = numberOfFullCircles*2+numberOfFillCircles;
  drivingSubsetData.splice(draggedCircleIndex, numberOfFillCircles);
  subsetSvg.selectAll("circle").data(drivingSubsetData).exit().remove();
  clearTimeout(subsetAnsweringTimeout);

  d3.select("#reset-circles-subset").style("display", "none");
  d3.select("#circles-subset-answer").text("")
                              .style("background-color", "transparent");
  sliderFull.disabled = false;
  sliderFill.disabled = false;
  updateCircles(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
}

function checkForSubsetEnd() {
  console.log("Checking for end");
  addDraggedCircle(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
  var answer = d3.select("#circles-subset-answer");
  if(areFull(drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
    var resetButton = d3.select("#reset-circles-subset");
    clearTimeout(subsetAnsweringTimeout);
    if(isPermutation(drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
        
      if(permutedSets_subset.length == 0) {
        permutedSetsTable_subset.append("caption").text("Permuted Sets Made")
                                    .style("color", "black");
      }
      
      var set = getSet(drivingSubsetData, numberOfFullCircles, numberOfFillCircles);
      var indexOfSet = setMade(permutedSets_subset, set);
      if(indexOfSet < 0) {
        permutedSets_subset.push(set);
        updateTable(permutedSetsTable_subset, permutedSets_subset);
        if(permutedSets_subset.length >= scrollingThreshold) {
          d3.select("#correct-subset-permutations").style("overflow-y", "scroll");
        }

        else {
          d3.select("#correct-subset-permutations").style("overflow-y", "hidden");
        }

        if(permutedSets_subset.length == numberOfSetsAllowed_subset) {
          tableComplete_subset = true;
          disableDrag(drivingSubsetData, subsetSvg, numberOfFullCircles, numberOfFillCircles);
          answer.text("You made all the different sets you can! Good job! You many scroll the slider to make a new set.");
          answer.style("background-color", "green");
        }
        else {
          answer.style("background-color", "green");
          answer.text("Correct.");
        }
      }

      else {
        displaySet(permutedSetsTableBody_subset, permutedSets_subset, indexOfSet)
        answer.text("Permutation has already been made. Try again.");
      }

    }
    else {
      
      answer.style("background-color", "red");
    }
    if(!tableComplete_subset) {
      resetButton.style("display", "block");
      sliderFull.disabled = true;
      sliderFill.disabled = true;
    }
  }
  

  else {
    if(subsetAnsweringTimeout)
      clearTimeout(subsetAnsweringTimeout);

    if(!isEmpty(drivingSubsetData, numberOfFullCircles, numberOfFillCircles)) {
      answer.text("Permuting...");
      answer.style("background-color", "yellow");
      subsetAnsweringTimeout = setTimeout(function() {
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

function factorial(num)
{
    var rval=1;
    for (var i = 2; i <= num; i++)
        rval = rval * i;
    return rval;
}

function createCopy(data, obj, atX, atY) {
  data.push({x: atX, y: atY, color: obj.data()[0].color, border: "none"});
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

function updateCircles(data, d3obj, nCircles, subset) {
  var circles = d3obj.selectAll("circle")
    .data(data)
        .attr("cx", function(d) { return d.x; })
        .attr("cy", function(d) { return d.y; })
        .attr("fill", function(d) { return d.color; })
        .style("stroke", function(d) { return d.border; });
}

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

var draggableCircles = d3Object.selectAll("circle").filter(function(d, i) { return i % 2 == 1 && i < nCircles*2; }).call(dragFunc);

  // d3.v4
  // draggableCircles = svg.selectAll("circle").filter(function(d, i) { return i % 2 == 1 && i < numberOfCircles*2; });
  //drag_handler(draggableCircles);
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
  let k = 0;
  for(let i = 0; i < data.length; ++i) {
    let cp = data[i];
    for(let j = 0; j < cp.length; ++j) {
      if(set[k] == cp[j]) {
        cp.splice(j, 1);
        if(cp.length == 0) {
          return i;
        }
        ++k;
        j = -1;
      }
    }
    k = 0;
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

// function moveTo(data, objIndex, toIndex) {
//   data[objIndex].x = data[toIndex].x;
//   data[objIndex].y = data[toIndex].y;
// }