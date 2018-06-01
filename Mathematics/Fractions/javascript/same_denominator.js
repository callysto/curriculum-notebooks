var numer1, denom1, numer2, denom2;

function lcm(a,b) {
    // Using the convention that the lcm is non-negative and lcm(a,0) = 0.
    if (a < 0) return lcm(-a, b);
    if (b < 0) return lcm(a, -b);
    if (a == 0) return 0;
    if (b == 0) return 0;
    
    var aa = a, bb = b;
    while (aa != bb) {
        if (aa < bb)
            aa = aa + a;
        else
            bb = bb + b;
    } 
    return aa;
}

function animateAdd() {
    // Disable "Reset" button so animation cannot be interrupted.
    d3.select("#button")
        .attr("disabled", "disabled")
        .attr("value", "Reset")
        .on("click", reset);
    
    var duration = 1000;               // Duration of animation (milliseconds)
    var tPerWedge = duration / numer1; // Duration of animation per wedge.
    for (var i = 1; i <= numer1; i++)
        setTimeout(draw, tPerWedge * i, numer1, denom1, numer2, denom2, i);

    // Reenable "Reset" button after the animation ends
    setTimeout(() => d3.select("#button").attr("disabled", null), duration);
}

function draw(n1, d1, n2, d2, diff) {
    svg.selectAll("path").remove();
    svg.selectAll("text").remove();

    var f1 = bifraction(0, n1 - diff, d1, 120, 80);
    var f2 = bifraction(n2, diff, d2, 120, 80 + 2 * f1.circleRadius + f1.circleSpacing);
    
    svg.append("text")
        .text((Number(n1) - Number(diff)) + "/" + d1)
        .attr("x", 0)
        .attr("y", 80);
    svg.append("text")
        .text((Number(n2) + Number(diff)) + "/" + d2)
        .attr("x", 0)
        .attr("y", 80 + 2 * f1.circleRadius + f1.circleSpacing);
    svg.append("path")
        .attr("d", f1.filledPath1())
        .attr("stroke", "#000000")
        .attr("fill", f1.fillColor1);
    svg.append("path")
        .attr("d", f1.filledPath2())
        .attr("stroke", "#000000")
        .attr("fill", f1.fillColor2);
    svg.append("path")
        .attr("d", f1.emptyPath())
        .attr("stroke", "#000000")
        .attr("fill", f1.emptyColor);
    svg.append("path")
        .attr("d", f2.filledPath1())
        .attr("stroke", "#000000")
        .attr("fill", f2.fillColor1);
    svg.append("path")
        .attr("d", f2.filledPath2())
        .attr("stroke", "#000000")
        .attr("fill", f2.fillColor2);
    svg.append("path")
        .attr("d", f2.emptyPath())
        .attr("stroke", "#000000")
        .attr("fill", f2.emptyColor);
}

function reset() {
    numer1 = defaultNumer1;
    denom1 = defaultDenom1;
    numer2 = defaultNumer2;
    denom2 = defaultDenom2;

    draw(numer1, denom1, numer2, denom2, 0);
    
    d3.select("#button")
        .attr("value", "Add")
        .on("click", animateAdd);
}

function divide() {
    var l = lcm(defaultDenom1, defaultDenom2);
    denom1 = l
    denom2 = l;
    numer1 = defaultNumer1 * l / defaultDenom1;
    numer2 = defaultNumer2 * l / defaultDenom2;
    draw(numer1, denom1, numer2, denom2, 0);
    d3.select("#button")
        .attr("value", "Add")
        .on("click", animateAdd);
}

var svg = d3.select("svg");

//reset();
