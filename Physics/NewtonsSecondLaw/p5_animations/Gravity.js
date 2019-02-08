var b = [];
var M;
var R;
var star = [];

function setup() {
  createCanvas(600,400);
  var r_old = 0;
  for (var i = 0; i < 20; i++) {
    M = random(1,6);
    R = M*15;
    if (i == 0)
    {
    	b[i] = new Ball(M,R/2,100,R);
    }
    else 
    {
    	b[i] = new Ball(M,R/2+r_old,100,R);
    }
    r_old += R;
  }
  for (var i = 0; i < 500; i++) {
    var x = random(width);
    var y = random(height);
    star[i] = new Star(0.8,x,y);
  }

};

var check = 0;

function draw() {
  background(0);
  var gravity = createVector(0,0.1);

  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }

  stroke(255);
  fill(255);

  if (check == 0) {
    var txt = new r_text("CLICK TO APPLY GRAVITATIONAL FORCE");
  }
  else {
    var txt = new r_text("");
  }

  if (mouseIsPressed) {
    check = 1;
  }

  for (var i = 0; i < b.length; i++) {
    if (check == 1) {
      b[i].applyForce(gravity);
    }
    b[i].display();
    b[i].update();
    b[i].checkEdges();
  }

};


function r_text(str) {
	text(str,200,250);
}

function Ball(m,start_x,start_y,R) {
  this.location = createVector(start_x, start_y);
  this.velocity = createVector(0,0);
  this.acceleration = createVector(0,0);
  this.mass = m;
  this.rad = R;

Ball.prototype.applyForce = function(force) {
  var f = force;
  this.acceleration.add(f);
};
  
Ball.prototype.update = function() {
  this.velocity.add(this.acceleration);
  this.location.add(this.velocity);
  this.acceleration.mult(0);
};

Ball.prototype.display = function() {
  stroke(0);
  strokeWeight(1);
  fill(199,0,57);
  ellipse(this.location.x,this.location.y,this.rad,this.rad);
};


Ball.prototype.checkEdges = function() {
  if (this.location.y > height) {
    this.velocity.y *= 1;
    this.location.y = height;
  }
  if (this.location.y < 0) {
    this.velocity.y *= -1;
    this.location.y = 0;
  }
};
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
