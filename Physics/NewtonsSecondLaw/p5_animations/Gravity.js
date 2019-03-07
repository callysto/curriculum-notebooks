var balls = [];
var star = [];
var state = 0;

function setup() {
  createCanvas(600, 400);
  reset();

  for (var i = 0; i < 500; i++) {
    var x = random(width);
    var y = random(height);
    star[i] = new Star(0.8, x, y);
  }
}

function reset() {
  var radius_old = 0;
  state = 0;
  
  for (var i = 0; i < 20; i++) {
    var mass = random(1, 6);
    var radius = mass*15;

    if (i == 0) {
    	balls[i] = new Ball(mass, radius/2, 100, radius);
    } else {
    	balls[i] = new Ball(mass, radius/2+radius_old, 100, radius);
    }

    radius_old += radius;
  }
}

function draw() {
  background(0);
  var gravity = createVector(0, 0.1);

  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }

  stroke(255);
  fill(255);

  if (state == 0) {
    new r_text("CLICK TO APPLY GRAVITATIONAL FORCE");
  } else if (state == 1) {
    new r_text("");
  } else {
    new r_text("CLICK TO RESET")
  }

  for (var i = 0; i < balls.length; i++) {
    if (state == 1) {
      balls[i].applyForce(gravity);
    }
    balls[i].display();
    balls[i].update();
    balls[i].stateEdges();
  }
};

function mousePressed() {
  if (state == 0) {
    state = 1;
  } else if (state == 2) {
    reset();
  } 
}

function r_text(str) {
	text(str, 200, 250);
}

function Ball(mass, start_x, start_y, radius) {
  this.location = createVector(start_x, start_y);
  this.velocity = createVector(0, 0);
  this.acceleration = createVector(0, 0);
  this.mass = mass;
  this.rad = radius;
};

Ball.prototype.applyForce = function(force) {
  this.acceleration.add(force);
};

Ball.prototype.update = function() {
  this.velocity.add(this.acceleration);
  this.location.add(this.velocity);
  this.acceleration.mult(0);
};

Ball.prototype.display = function() {
  stroke(0);
  strokeWeight(1);
  fill(199, 0, 57);
  ellipse(this.location.x, this.location.y, this.rad, this.rad);
};

Ball.prototype.stateEdges = function() {
  if (this.location.y > height) {
    this.velocity.y *= 1;
    this.location.y = height;
    state = 2;
  }
  if (this.location.y < 0) {
    this.velocity.y *= -1;
    this.location.y = 0;
  }
};

function Star(radius, x, y) {
  this.x = x;
  this.y = y;
  this.radius = radius;
};

Star.prototype.display = function() {
  noStroke();
  fill(255, 255, 255);
  ellipse(this.x, this.y, this.radius, this.radius);
};
