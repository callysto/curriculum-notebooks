var b;
var star = [];
function setup() {
  createCanvas(900,300);
  b = new Ball(4);
  for (var i = 0; i < 500; i++) {
    var x = random(width);
    var y = random(height);
    star[i] = new Star(0.8,x,y);
  }

};

function drawArrow(x0,y0,x1,y1) {
  strokeWeight(20);
  stroke(255, 87, 51);
  triangle(x1,y1+2,x1,y1-2,x1+3.5,y1);
  line(x0,y0,x1,y1);
};



function draw() {
  background(0);
  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }

  var wind = createVector(5,0); // MAYBE 
  if (mouseIsPressed && mouseX>0 && mouseX<70 && mouseY>height/2-10 && mouseY<height/2+10) {
    b.applyForce(wind);

  }
  drawArrow(0,height/2,50,height/2);  
  stroke(0)
  b.update();
  //m.checkEdges();
  b.display();

};


var Ball = function(m) {
  this.location = createVector(105, 150);
  this.velocity = createVector(0,0);
  this.acceleration = createVector(0,0);
  this.mass = m;
};

Ball.prototype.applyForce = function(force) {
  var f = p5.Vector.div(force,this.mass);
  this.acceleration.add(f);
};
  
Ball.prototype.update = function() {
  this.velocity.add(this.acceleration);
  this.location.add(this.velocity);
  this.acceleration.mult(0);
  this.velocity.limit(2);
};

Ball.prototype.display = function() {
  stroke(0);
  strokeWeight(1);
  fill(199,0,57);
  ellipse(this.location.x,this.location.y,this.mass*16,this.mass*16);
};

function Star(r, X, Y) {
  this.x = X;
  this.y = Y;
  this.radius = r;
 
Star.prototype.display = function() {
  noStroke();
  fill(255,255,255);
  ellipse(this.x,this.y,this.radius,this.radius);
};

};