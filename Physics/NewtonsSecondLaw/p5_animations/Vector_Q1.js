var body;
var r = 10;
var arrow;
var check = 0;
var b = 0;
var j = 0;
var s;
function setup() {
	createCanvas(450,400);
	body = new Ball(3,width/2,height/2-100, 0, 32, 96);
	arrow = new drawArrowObj();
}

var rr = 254;
var rg = 199;
var rb = 0;
function draw() {
	background(255);
	var bodyCenter = createVector(body.location.x,body.location.y);	
	var F1 = createVector(bodyCenter.x + 70,bodyCenter.y);
	var F2 = createVector(bodyCenter.x - 80,bodyCenter.y - 70);
	var F3 = createVector(bodyCenter.x - 10 -150,bodyCenter.y - 70+250);
	var F4 = createVector(bodyCenter.x + 50 - 30,bodyCenter.y + 30+200);
	var F5 = createVector(bodyCenter.x + 80 + 100,bodyCenter.y -20 + 220);
	var offset = r;
	body.display();	
	drawArrow(bodyCenter,F1,offset,200, 5, 20);
	drawArrow(bodyCenter,F2,offset,200, 5, 20);
	
	var mouse = createVector(mouseX,mouseY);
	bodyCenter.y += 250
	bodyCenter.x -= 150

	drawArrow(bodyCenter,F3,offset, rr, rg, rb );
	bodyCenter = createVector(body.location.x,body.location.y);
	bodyCenter.y += 200
	bodyCenter.x -= 30
	drawArrow(bodyCenter,F4,offset, 254, 199, 0 );
	bodyCenter = createVector(body.location.x,body.location.y);
	bodyCenter.y += 220
	bodyCenter.x += 100
	drawArrow(bodyCenter,F5,offset, 254, 199, 0 );
	stroke(0)
	line(0,250,width,250)
	line(width/3,250,width/3,height)
	line(2*width/3,250,2*width/3,height)
	line(0,height-2,width,height-2)
	line(1,250,1,height)
	line(width-1.5,250,width-1.5,height)
	fill(255)
	textSize(12)
	text("Force 1",100,45)
	text("Force 2",270,90)
	
	if (mouseIsPressed && mouseX < width/3 && mouseY > 250 || j == 1) {
		var s = "Correct!";
		rr = 46;
		rg = 222;
		rb = 64;
		j = 1;
	}
	else if (j != 1) {
		var s = "";
	}
	fill( 46, 222, 64 )
	textSize(30)
	text(s,width/2-50,height/2)
}

var Ball = function(m,b_x,b_y,r,g,b) {
  this.location = createVector(b_x, b_y);
  this.mass = m;
  this.red = r;
  this.green = g;
  this.blue = b;
};

  
Ball.prototype.update = function(new_x,new_y) {
  this.location.x = new_x;
  this.location.y = new_y;
};

Ball.prototype.display = function(a) {
  strokeWeight(3);
  stroke(this.red,this.green,this.blue)
  fill(this.red,this.green,this.blue,a);
  ellipse(this.location.x,this.location.y,this.mass*20,this.mass*20);
};


function drawArrow(X1,X2,offset,r,g,b) {
    var x1 = X1;
    var x2 = X2;
    stroke(r,g,b);
    fill(r,g,b)
    line(x1.x,x1.y,x2.x,x2.y);
    push(); //start new drawing state
    var angle = atan2(x1.y - x2.y, x1.x - x2.x); //gets the angle of the line
    translate(x2.x, x2.y); //translates to the destination vertex
    rotate(angle-HALF_PI); //rotates the arrow point
    triangle(-offset*0.5, offset, offset*0.5, offset, 0, -offset/2); //draws the arrow point as a triangle
    pop();	
}

var drawArrowObj = function() {
	this.end1 = createVector(width/2,height/2);
	this.end2 = createVector(0,0);
}

drawArrowObj.prototype.display = function(offset,r,g,b) {
    var x1 = this.end1;
    var x2 = this.end2;
    stroke(r,g,b);
    fill(r,g,b)
    line(x1.x,x1.y,x2.x,x2.y);
    // push(); //start new drawing state
    var angle = atan2(x1.y - x2.y, x1.x - x2.x); //gets the angle of the line
    translate(x2.x, x2.y); //translates to the destination vertex
    rotate(angle-HALF_PI); //rotates the arrow point
    triangle(-offset*0.5, offset, offset*0.5, offset, 0, -offset/2); //draws the arrow point as a triangle
//     pop();
}
drawArrowObj.prototype.update = function() {
	this.end2.x = mouseX;
	this.end2.y = mouseY;
}

