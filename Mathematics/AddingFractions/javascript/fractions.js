function circlePath(cx, cy, r) {
    return [
        "M", [cx + r, cy],
        "A", [r, r, 0, 0, 1, cx, cy + r],
        "A", [r, r, 0, 1, 1, cx + r, cy],
        "Z"
    ].join(" ");
}

function wedge(cx, cy, r, theta1, theta2) {
    var w = {};
    w.cx = cx;
    w.cy = cy;
    w.r = r;

    w.theta1 = theta1;
    w.theta2 = theta2;

    w.path = function() {
        var largeArc = theta2 - theta1 > Math.PI ? 1 : 0;
        var clockWise = 1;
        var x = this.cx + this.r * Math.cos(this.theta2);
        var y = this.cy + this.r * Math.sin(this.theta2);
        return [
            "M", [this.cx, this.cy],
            "L", [this.cx + this.r * Math.cos(this.theta1), this.cy + this.r * Math.sin(this.theta1)],
            "A", [this.r, this.r, 0, largeArc, clockWise, x, y],
            "Z"
        ].join(" ");
    }
    return w;
}

/*function pie(cx, cy, r, nSlices) {
    var p = {};
    p.cx = cx;
    p.cy = cy;
    p.r = r;
    p.nSlices = nSlices;
    p.path = function() {
        var ret = "";
        // For each slice, make a wedge.
        for (var i = 0; i < this.nSlices; i++) {
            var w = wedge(this.cx,
                          this.cy,
                          this.r,
                          2 * i       * Math.PI / this.nSlices,
                          2 * (i + 1) * Math.PI / this.nSlices);
            ret = ret + w.path();
        }
        return ret;
    }
    return p;
}

function filledPie(cx, cy, r, nColored, nSlices, fillColor, emptyColor) {
    var p = {};
    if (typeof(fillColor)  === "undefined") fillColor  = "#3399ff";
    if (typeof(emptyColor) === "undefined") emptyColor = "#ffffff";
    p.cx = cx;
    p.cy = cy;
    p.r = r;
    p.nColored = nColored;
    p.nSlices = nSlices;
    p.fillColor = fillColor;
    p.emptyColor = emptyColor;
    p.filledPath = function() {
        var ret = "";
        // For each colored slice, make a wedge.
        for (var i = 0; i < this.nSlices && i < this.nColored; i++) {
            var w = wedge(this.cx,
                          this.cy,
                          this.r,
                          2 * i       * Math.PI / this.nSlices,
                          2 * (i + 1) * Math.PI / this.nSlices);
            ret = ret + w.path();
        }
        return ret;
    }
    p.emptyPath = function() {
        var ret = "";
        // For each uncolored slice, make a wedge.
        for (var i = this.nColored; i < this.nSlices; i++) {
            var w = wedge(this.cx,
                          this.cy,
                          this.r,
                          2 * i       * Math.PI / this.nSlices,
                          2 * (i + 1) * Math.PI / this.nSlices);
            ret = ret + w.path();
        }
        return ret;
    }
    return p;
}*/

// Fractions should have denominator b > 0.
// Drawing the fraction will only make sense with a numerator a >= 0.
// x and y specify the coordinates at which the fraction is drawn.
// x and y is the center of the fraction's drawing's leftmost circle.
function fraction(a, b, x, y) {
    var frac = {};
    frac.numer = Number(a);
    frac.denom = Number(b);
    
    // Variables affecting rendering.
    frac.fillColor = "#33ff99";
    frac.emptyColor = "#ffffff";
    frac.circleRadius = 50;
    frac.circleSpacing = 10;
    frac.x = Number(x);
    frac.y = Number(y);

    frac.filledPath = function() {
        var ret = "";
        var a = this.numer, b = this.denom, k;

        // Special case if b = 1 (representation is a circle)
        if (b == 1) {
            for (var i = 0; i < a; i++)
                ret += circlePath(this.x + i * (2 * this.circleRadius + this.circleSpacing), this.y, this.circleRadius);
            return ret;
        }
        
        // Concatenate a whole bunch of wedges
        k = 0;
        while (k < a) {
            var iCircle, cx, cy, r, theta1, theta2;
            iCircle = Math.floor(k / b);
            if (iCircle < 0) iCircle = 0;
            cx = this.x + iCircle * (2 * this.circleRadius + this.circleSpacing);
            cy = this.y;
            r = this.circleRadius;
            theta1 = 2 * k * Math.PI / b;
            theta2 = 2 * (k + 1) * Math.PI / b;
            ret = ret + wedge(cx, cy, r, theta1, theta2).path();
            k = k + 1;
        }
        return ret;
    }

    frac.emptyPath = function() {
        var ret = "";
        var a = this.numer, b = this.denom, k;

        // Special case if b = 1 (representation is a circle)
        if ((b == 1) && (a == 0))
            return circlePath(this.x, this.y, this.circleRadius);

        // Concatenate a whole bunch of wedges
        k = a;
        while (k < b) {
            var iCircle, cx, cy, r, theta1, theta2;
            iCircle = Math.floor(k / b);
            if (iCircle < 0) iCircle = 0;
            cx = this.x + iCircle * (2 * this.circleRadius + this.circleSpacing);
            cy = this.y;
            r = this.circleRadius;
            theta1 = 2 * k * Math.PI / b;
            theta2 = 2 * (k + 1) * Math.PI / b;
            ret = ret + wedge(cx, cy, r, theta1, theta2).path();
            k = k + 1;
        }
        return ret;
    }
    
    return frac;
}



// Representation of the fraction (a + b)/c at the coordinate (x,y).
// Represents this as a circle cut into c equal-sized wedges.
// The first a wedges are in one color, and the next b wedges are in another color.
// These colors can be modified. E.g.
//
//    bf = bifraction(1, 2, 3, 100, 100)
//    bf.fillColor1 = "#ff0000"
//    bf.fillColor2 = "#0000ff"
//
// If (a + b) > c, then several circles (arranged horizontally) are used to represent the fraction.
function bifraction(a, b, c, x, y) {
    var frac = {};
    frac.numer1 = Number(a);
    frac.numer2 = Number(b);
    frac.denom = Number(c);
    
    // Variables affecting rendering.
    frac.fillColor1 = "#33ff99";
    frac.fillColor2 = "#ff9933";
    frac.emptyColor = "#ffffff";
    frac.circleRadius = 50;
    frac.circleSpacing = 10;
    frac.x = Number(x);
    frac.y = Number(y);

    frac.filledPath1 = function() {
        var ret = "";
        var a = this.numer1, b = this.numer2, c = this.denom, k;

        // Special case if c = 1 (representation is a circle)
        if (c == 1) {
            for (var i = 0; i < a; i++)
                ret = ret + circlePath(this.x + i * (2 * this.circleRadius + this.circleSpacing), this.y, this.circleRadius);
            return ret;
        }
        
        // Concatenate a whole bunch of wedges
        k = 0;
        while (k < a) {
            var iCircle, cx, cy, r, theta1, theta2;
            iCircle = Math.floor(k / c);
            if (iCircle < 0) iCircle = 0;
            cx = this.x + iCircle * (2 * this.circleRadius + this.circleSpacing);
            cy = this.y;
            r = this.circleRadius;
            theta1 = 2 * k * Math.PI / c;
            theta2 = 2 * (k + 1) * Math.PI / c;
            ret = ret + wedge(cx, cy, r, theta1, theta2).path();
            k = k + 1;
        }
        return ret;
    }

    frac.filledPath2 = function() {
        var ret = "";
        var a = this.numer1, b = this.numer2, c = this.denom, k;

        // Special case if c = 1 (representation is a circle)
        if (c == 1) {
            for (var i = a; i < a + b; i++)
                ret = ret + circlePath(this.x + i * (2 * this.circleRadius + this.circleSpacing), this.y, this.circleRadius);
            return ret;
        }
        
        
        // Concatenate a whole bunch of wedges
        k = a;
        while (k < a + b) {
            var iCircle, cx, cy, r, theta1, theta2;
            iCircle = Math.floor(k / c);
            if (iCircle < 0) iCircle = 0;
            cx = this.x + iCircle * (2 * this.circleRadius + this.circleSpacing);
            cy = this.y;
            r = this.circleRadius;
            theta1 = 2 * k * Math.PI / c;
            theta2 = 2 * (k + 1) * Math.PI / c;
            ret = ret + wedge(cx, cy, r, theta1, theta2).path();
            k = k + 1;
        }
        return ret;
    }

    frac.emptyPath = function() {
        var ret = "";
        var a = this.numer1, b = this.numer2, c = this.denom, k;
        var nCircles;
        if (a + b == 0) nCircles = 1;
        else            nCircles = Math.ceil((a + b) / c);

        if ((c == 1) && (a + b == 0))
            return circlePath(this.x, this.y, this.circleRadius);

        // Concatenate a whole bunch of wedges
        k = a + b;
        while (k < nCircles * c) {
            var iCircle, cx, cy, r, theta1, theta2;
            iCircle = Math.floor(k / c);
            if (iCircle < 0) iCircle = 0;
            cx = this.x + iCircle * (2 * this.circleRadius + this.circleSpacing);
            cy = this.y;
            r = this.circleRadius;
            theta1 = 2 * k * Math.PI / c;
            theta2 = 2 * (k + 1) * Math.PI / c;
            ret = ret + wedge(cx, cy, r, theta1, theta2).path();
            k = k + 1;
        }
        return ret;
    }
    
    return frac;
}
