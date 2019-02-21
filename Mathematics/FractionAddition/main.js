var mainCanvas = d3.select('#mainCanvas');
var answerCanvas = d3.select('#answerCanvas');

var leftBox = d3.select('#lOpperandDivisonBox');
var leftOpperand = {
    box: leftBox,
    width: Number(leftBox.attr('width')),
    height: Number(leftBox.attr('height')),
    xLoc: Number(leftBox.attr('x')),
    yLoc: Number(leftBox.attr('y')),
    numerator: Number(0),
    denominator: Number(0),
    colour: '#8a2df3',
    multiplier: Number(1),
    answer: {
        box: d3.select('#lOpperandDivisonBoxAnswer'),
        width: 120,
        height: 100,
        xLoc: 20,
        yLoc: 300
    }
};

var rightBox = d3.select('#rOpperandDivisonBox');
var rightOpperand = {
    box: rightBox,
    width: Number(rightBox.attr('width')),
    height: Number(rightBox.attr('height')),
    xLoc: Number(rightBox.attr('x')),
    yLoc: Number(rightBox.attr('y')),
    numerator: Number(0),
    denominator: Number(0),
    colour: '#f91750',
    multiplier: Number(1),
    answer: {
        box: d3.select('#rOpperandDivisonBoxAnswer'),
        width: 120,
        height: 100,
        xLoc: 20,
        yLoc: 300
    }
};

var divideBox = function (xVal, box, lineNum, isDashed) {
    var i = xVal;
    while (lineNum > 0) {
        addLine(i + box.xLoc, i + box.xLoc, 0 + box.yLoc, box.height + box.yLoc, isDashed, box);
        i += xVal;
        lineNum--;
    }
};

var fillNumerator = function (xVal, box) {
    d3.select('#' + box.box.attr('id') + 'Filled')
        .transition().delay(function (d, i) {
            return i * 300;
        }).duration(500)
        .attr('width', xVal)
        .style('fill', box.colour)
        .each('end', function () {
            d3.select('#' + box.box.attr('id') + 'Answer')
                .attr('width', xVal)
                .style('fill', box.colour);
        });
};

var initBox = function (numerator, denominator, box) {
    var sectionLen = box.width / denominator;
    fillNumerator((numerator * sectionLen), box);
    divideBox(sectionLen, box, denominator - 1);
    drawFractionText(numerator, denominator, Number(box.width) + 60, Number(box.yLoc) + 30, 'originalFraction');
    d3.select('#addBtn').style('display', 'block');
    d3.select('#resetBtn').style('display', 'block');
    initAnswerArea();
};

var drawFractionText = function (numerator, denominator, xPos, yPos, secondaryClass) {
    mainCanvas.append('text')
        .attr('class', 'fractionText resetRemove ' + secondaryClass)
        .text(numerator)
        .attr('x', function () {
            if (numerator < 10) {
                return xPos + 7;
            } else {
                return xPos;
            }
        })
        .attr('y', yPos);

    mainCanvas.append('text')
        .attr('class', 'fractionText resetRemove ' + secondaryClass)
        .text(denominator)
        .attr('x', function () {
            if (denominator < 10) {
                return xPos + 7;
            } else {
                return xPos;
            }
        })
        .attr('y', yPos + 30);

    mainCanvas.append('line')
        .attr('class', 'textFractionLine ' + secondaryClass + ' resetRemove')
        .attr('x1', xPos)
        .attr('x2', xPos + 25)
        .attr('y1', yPos + 5)
        .attr('y2', yPos + 5)
        .style('stroke', 'black')
        .style('stroke-width', 2);
}

var addLine = function (x1, x2, y1, y2, isDashed, box) {
    var dashed = '0,0';
    var name = '';
    var stroke = 2;
    if (isDashed) {
        dashed = '4,3';
        name = box.box.attr('id') + 'DashedDivLine';
        stroke = 1
    }
    mainCanvas.append('line')
        .attr('class', 'divLine ' + name + ' resetRemove')
        .attr('x1', x1)
        .attr('x2', x2)
        .attr('y1', y1)
        .attr('y2', y2)
        .style('stroke', 'black')
        .style('stroke-width', stroke)
        .attr('stroke-dasharray', dashed);
};

var isValid = function (numerator, denominator) {
    if (numerator < 0 || numerator > 12) {
        return false;
    }
    if (denominator <= 0 || denominator > 12) {
        return false;
    }
    return (numerator < denominator);
};

var resetBoxes = function () {
    d3.selectAll('.filledNum').attr('width', 0);
    d3.select('#lOpperandDivisonBoxAnswer').attr('y', leftOpperand.yLoc);
    d3.select('#rOpperandDivisonBoxAnswer').attr('x', rightOpperand.xLoc).attr('y', rightOpperand.yLoc);
    d3.selectAll('.resetRemove').remove();
    d3.selectAll('.resetDisplay').style('display', 'none');
    d3.select('#answerBox').attr('width', 0).attr('height', 0);
    leftOpperand.multiplier = 1;
    rightOpperand.multiplier = 1;

};

var resetInputs = function () {
    document.getElementById('lOppNumerator').value = '';
    document.getElementById('lOppDenominator').value = '';
    document.getElementById('rOppNumerator').value = '';
    document.getElementById('rOppDenominator').value = '';
    document.getElementById('answerNumerator').value = '';
    document.getElementById('answerDenominator').value = '';
    d3.selectAll('.answerArea').style('display', 'none');

};

var addingAnimation = function () {
    updateAnswerValues(leftOpperand.answer);
    updateAnswerValues(rightOpperand.answer);
    rightXValue = Number(d3.select('#lOpperandDivisonBoxFilled').attr('width'));
    rightXValue += Number(d3.select('#lOpperandDivisonBoxFilled').attr('x'));
    leftDivLines = document.getElementById('lOppNumerator').value;
    rightDivLines = document.getElementById('rOppNumerator').value;
    boxWidth = 400;
    isOver1 = false;
    if (rightXValue + Number(d3.select('#rOpperandDivisonBoxFilled').attr('width')) - 20 > 400) {
        boxWidth = 800;
        isOver1 = true;
    }

    d3.selectAll('.expandBtn').style('display', 'block');

    d3.select('#answerBox')
        .transition().delay(function (d, i) {
            return i * 300;
        }).duration(800)
        .attr('width', boxWidth)
        .attr('height', 100)
        .each('end', function () {
            if (boxWidth > 400) {
                mainCanvas.append('line')
                    .attr('class', 'divLine resetRemove')
                    .attr('x1', 420)
                    .attr('x2', 420)
                    .attr('y1', 300)
                    .attr('y2', 400)
                    .style('stroke', 'black')
                    .style('stroke-width', 3)
            }
        });

    d3.select('#lOpperandDivisonBoxAnswer')
        .style('outline', 'solid black 2px')
        .transition().delay(function (d, i) {
            return i * 300;
        }).duration(1000)
        .attr('y', 300)
        .each('end', function () {
            d3.select('#rOpperandDivisonBoxAnswer')
                .style('outline', 'solid black 2px')
                .transition().delay(function (d, i) {
                    return i * 300;
                }).duration(1000)
                .attr('y', 300)
                .attr('x', rightXValue)
                .each('end', function () {
                    var distance = d3.select('#lOpperandDivisonBoxAnswer').attr('width') / leftDivLines;
                    for (i = 0; i < leftDivLines; i++) {
                        addLine(20 + (distance * i), 20 + (distance * i), 300, 400);
                    }
                    distance = d3.select('#rOpperandDivisonBoxAnswer').attr('width') / rightDivLines;
                    for (i = 0; i < rightDivLines; i++) {
                        addLine(rightXValue + (distance * i), rightXValue + (distance * i), 300, 400);
                    };
                })
        });

    if (isSameDenominator(Number(leftOpperand.denominator), Number(rightOpperand.denominator))) {
        drawMatchingText();
    }
}

var updateAnswerValues = function (box) {
    var boxId = '#' + box.box.attr('id');
    box.width = Number(d3.select(boxId).attr('width'));
    box.height = Number(d3.select(boxId).attr('height'));
    box.xLoc = Number(d3.select(boxId).attr('x'));
    box.yLoc = Number(d3.select(boxId).attr('y'));
}

var addExpand = function (box, classText) {
    var name = box.box.attr('id') + classText;
    updateAnswerValues(box.answer);
    if (box.multiplier < 12) {
        d3.selectAll('.' + name).remove();
        d3.selectAll('.' + box.box.attr('id') + 'DashedDivLine').remove();
        d3.selectAll('.' + box.answer.box.attr('id') + 'DashedDivLine').remove();
        box.multiplier++
        drawExpand(box, name);
    }
    var lh = Number(leftOpperand.denominator) * (Number(leftOpperand.multiplier));
    var rh = Number(rightOpperand.denominator) * (Number(rightOpperand.multiplier));
    if (isSameDenominator(lh, rh)) {
        drawMatchingText();
    } else {
        d3.selectAll('.matchText').remove();
    }
}

var minusExpand = function (box, classText) {
    var name = box.box.attr('id') + classText;
    if (box.multiplier > 1) {
        d3.selectAll('.' + name).remove();
        d3.selectAll('.' + box.box.attr('id') + 'DashedDivLine').remove();
        d3.selectAll('.' + box.answer.box.attr('id') + 'DashedDivLine').remove();
        box.multiplier--;
        drawExpand(box, name);
    }
    var lh = Number(leftOpperand.denominator) * (Number(leftOpperand.multiplier));
    var rh = Number(rightOpperand.denominator) * (Number(rightOpperand.multiplier));
    if (isSameDenominator(lh, rh)) {
        drawMatchingText();
    } else {
        d3.selectAll('.matchText').remove();
    }
}

var isSameDenominator = function (lh, rh) {
    if (lh === rh) {
        return true;
    }
}

var drawMatchingText = function () {
    setInstruction(steps.step7);
    mainCanvas.append('text')
        .attr('class', 'matchText resetRemove')
        .html('&#9989;')
        .attr('x', 620)
        .attr('y', 57)
        .attr('width', 100)
        .style('font', '20px sans-serif');

    mainCanvas.append('text')
        .attr('class', 'matchText resetRemove')
        .html('&#9989;')
        .attr('x', 620)
        .attr('y', 202)
        .attr('width', 100)
        .style('font', '20px sans-serif');


}

var drawExpand = function (box, classText) {
    drawFractionText(box.multiplier, box.multiplier, Number(box.width) + 110, Number(box.yLoc) + 30, classText);
    drawFractionText((Number(box.numerator) * Number(box.multiplier)), (Number(box.denominator) * Number(box.multiplier)), Number(box.width) + 170, Number(box.yLoc) + 30, classText);
    divideBox(box.width / (Number(box.multiplier) * Number(box.denominator)), box, Number(box.denominator) * Number(box.multiplier) - 1, true);
    divideBox(box.width / (Number(box.multiplier) * Number(box.denominator)), box.answer, Number(box.numerator) * Number(box.multiplier) - 1, true);
    mainCanvas.append('text')
        .attr('class', 'fractionText resetRemove ' + classText)
        .text('X')
        .attr('x', Number(box.width) + 91)
        .attr('y', Number(box.yLoc) + 41)
        .style('font', '20px sans-serif');

    mainCanvas.append('text')
        .attr('class', 'fractionText resetRemove ' + classText)
        .text('=')
        .attr('x', Number(box.width) + 146)
        .attr('y', Number(box.yLoc) + 41);
}

var setInstruction = function (stepNum) {
    if (!isScrolledIntoView(document.getElementById('pixelCat'))) {
        if (d3.select('#' + stepNum.id).style('display') === 'none') {
            d3.select('#arrow')
                .transition().delay(function (d, i) {
                    return i * 300;
                }).duration(500)
                .style('opacity', 1);
        }
    }
    if (stepNum.id != 'speech5') {
        d3.selectAll('.speechBubbles').style('display', 'none');
    }
    d3.select('#' + stepNum.id).style('display', 'block');
}

var initAnswerArea = function () {
    d3.selectAll('.answerArea').style('display', 'block');
    answerCanvas.append('text')
        .text(leftOpperand.numerator = document.getElementById('lOppNumerator').value)
        .attr('x', function () {
            if (leftOpperand.numerator > 9) {
                return 15;
            } else {
                return 22;
            }
        })
        .attr('y', 30)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('text')
        .text(leftOpperand.denominator = document.getElementById('lOppDenominator').value)
        .attr('x', function () {
            if (leftOpperand.denominator > 9) {
                return 15;
            } else {
                return 22;
            }
        })
        .attr('y', 60)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('line')
        .attr('x1', 15)
        .attr('x2', 40)
        .attr('y1', 36)
        .attr('y2', 36)
        .style('stroke', 'black')
        .style('stroke-width', 2)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('text')
        .text('+')
        .attr('x', 51)
        .attr('y', 45)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('text')
        .text(rightOpperand.numerator = document.getElementById('rOppNumerator').value)
        .attr('x', function () {
            if (rightOpperand.numerator > 9) {
                return 75;
            } else {
                return 82;
            }
        })
        .attr('y', 30)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('text')
        .text(rightOpperand.denominator = document.getElementById('rOppDenominator').value)
        .attr('x', function () {
            if (rightOpperand.denominator > 9) {
                return 75;
            } else {
                return 82;
            }
        })
        .attr('y', 60)
        .attr('class', 'fractionText resetRemove');

    answerCanvas.append('line')
        .attr('x1', 75)
        .attr('x2', 100)
        .attr('y1', 36)
        .attr('y2', 36)
        .style('stroke', 'black')
        .style('stroke-width', 2)
        .attr('class', 'fractionText resetRemove');

    d3.select("#answerCanvas").append('text')
        .text('=')
        .attr('x', 110)
        .attr('y', 45)
        .attr('class', 'fractionText resetRemove');
};

var reduce = function (fraction) {
    var count = fraction.denominator;
    var myFraction = fraction;
    for (var i = count; i > 1; i--) {
        if (myFraction.numerator % i === 0 && myFraction.denominator % i === 0) {
            myFraction.numerator /= i;
            myFraction.denominator /= i;
        }
    }
    return myFraction;
};

var checkAnser = function (userAnswer, answer) {
    d3.selectAll('.answerStatusText').style('display', 'none');
    if (userAnswer.numerator / userAnswer.denominator === answer.numerator / answer.denominator) {
        var tmp = {
            numerator: userAnswer.numerator,
            denominator: userAnswer.denominator
        };
        tmp = reduce(tmp);
        if (tmp.numerator === userAnswer.numerator && tmp.denominator === userAnswer.denominator) {
            d3.select('#correct').style('display', 'block')
        } else {
            d3.select('#needRounding').style('display', 'block');
        }
    } else {
        d3.select('#incorrect').style('display', 'block');
    }
};


function isScrolledIntoView(elem) {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
    var elemBottom = elemTop + $(elem).height();

    return ((elemBottom <= docViewBottom) && (elemTop >= docViewTop));
};


document.getElementById('submitFraction').onclick = function () {
    resetBoxes();
    leftOpperand.numerator = document.getElementById('lOppNumerator').value;
    leftOpperand.denominator = document.getElementById('lOppDenominator').value;
    rightOpperand.numerator = document.getElementById('rOppNumerator').value;
    rightOpperand.denominator = document.getElementById('rOppDenominator').value;
    if (isValid(Number(leftOpperand.numerator), Number(leftOpperand.denominator)) && isValid(Number(rightOpperand.numerator), Number(rightOpperand.denominator))) {
        initBox(Number(leftOpperand.numerator), Number(leftOpperand.denominator), leftOpperand);
        initBox(Number(rightOpperand.numerator), Number(rightOpperand.denominator), rightOpperand);
        setInstruction(steps.step2);

    } else {
        alert('Make sure your factions are proper and the denominators less than or equal to 12. (ex. 3/8 + 6/12)');
    }
};

document.getElementById('resetBtn').onclick = function () {
    setInstruction(steps.step1);
    resetBoxes();
    resetInputs();
};

document.getElementById('addBtn').onclick = function () {
    if (isSameDenominator(leftOpperand.denominator, rightOpperand.denominator)) {
        setInstruction(steps.step3)
    } else {
        setInstruction(steps.step4);
        setInstruction(steps.step5);
    }
    addingAnimation();
};

document.getElementById('lOppExpandPlusBtn').onclick = function () {
    setInstruction(steps.step6);
    addExpand(leftOpperand, 'FractionText');
};

document.getElementById('lOppExpandMinusBtn').onclick = function () {
    setInstruction(steps.step6);
    minusExpand(leftOpperand, 'FractionText');
};

document.getElementById('rOppExpandPlusBtn').onclick = function () {
    setInstruction(steps.step6);
    addExpand(rightOpperand, 'FractionText');
};

document.getElementById('rOppExpandMinusBtn').onclick = function () {
    setInstruction(steps.step6);
    minusExpand(rightOpperand, 'FractionText');
};

document.getElementById('checkAnswer').onclick = function () {
    var answer = {
        numerator: (Number(leftOpperand.numerator) * Number(rightOpperand.denominator)) + (Number(rightOpperand.numerator) * Number(leftOpperand.denominator)),
        denominator: Number(leftOpperand.denominator) * Number(rightOpperand.denominator)
    };
    var userAnswer = {
        numerator: Number(document.getElementById('answerNumerator').value),
        denominator: Number(document.getElementById('answerDenominator').value)
    };
    answer = reduce(answer);
    if (userAnswer.numerator > 0 && userAnswer.denominator > 0) {
        checkAnser(userAnswer, answer);
    }
};

function showMeow() {
    document.getElementById('meow').style.display = "block";
};

function hideMeow() {
    document.getElementById('meow').style.display = "none";
};

document.getElementById('site').onscroll = function () {
    if (isScrolledIntoView(document.getElementById('pixelCat'))) {
        d3.select('#arrow')
            .transition().delay(function (d, i) {
                return i * 300;
            }).duration(500)
            .style('opacity', 0);
    }
}

var steps = {
    step1: {
        id: 'speech1'
    },
    step2: {
        id: 'speech2'
    },
    step3: {
        id: 'speech3'
    },
    step4: {
        id: 'speech4'
    },
    step5: {
        id: 'speech5'
    },
    step6: {
        id: 'speech6'
    },
    step7: {
        id: 'speech7'
    }
};