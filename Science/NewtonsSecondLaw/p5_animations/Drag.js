var balls = [];
var liquid;
var bub1 = [];
var bub2 = [];
var state = 0;

function setup() {
  createCanvas(750, 600);
  reset();
  liquid = new Friction(0, height/1.8, width, height/2, 0.1);
}

function reset() {
  var radius_old = 0;
  state = 0;

  for (var i = 0; i < 40; i++) {
    var mass = random(1, 11);
    var radius = mass*5;

    if (i == 0) {
    	balls[i] = new Ball(mass, radius/2, 100, radius);
    } else {
    	balls[i] = new Ball(mass, radius/2+radius_old, 100, radius);
    }

    radius_old += radius;
  }

  for (var i = 0; i < 50; i++) {
    bub1[i] = new Bubbles();
  }
  for (var i = 0; i < 50; i++) {
    bub2[i] = new Bubbles();
  }
}

function draw() {
  background(255);
  liquid.display();
  stroke(0);
  fill(0);

  if (state == 0) {
    new r_text("CLICK TO APPLY GRAVITATIONAL FORCE");
  } else if (state == 1) {
    new r_text("");
  } else {
    new r_text("CLICK TO RESET")
  }

  for (var i = 0; i < bub1.length; i++) {
    bub1[i].display();
    bub1[i].clr();
    bub1[i].floater(0.07);
  }

  for (var i = 0; i < balls.length; i++) {
    var gravity = createVector(0, 0.1*balls[i].mass);

    if (state != 0) {
      balls[i].applyForce(gravity);
    }

    balls[i].isInside(liquid);

    if (balls[i].edges == 1) {
      balls[i].Drag(liquid);
    }

    balls[i].display();
    balls[i].update();
    balls[i].checkEdges();
  }

  for (var i = 0; i < bub2.length; i++) {
    bub2[i].display();
    bub2[i].clr();
    bub2[i].floater(0.07);
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
	text(str, 255, 240);
}

function Bubbles() {
  this.location = createVector(random(0, width), random(height/1.8, height));
};

Bubbles.prototype.display = function() {
  stroke(105, 145, 207);
  strokeWeight(0.7);
  fill(105, 145, 207, 0.8);
  ellipse(this.location.x, this.location.y, 5, 5);
};

Bubbles.prototype.floater = function(flt_rate) {
  var B_x = this.location.x;
  var B_y = this.location.y;
  var mov = random(-1, 1)*0.1
  this.location.x += mov;
  this.location.y -= flt_rate;
};

Bubbles.prototype.clr = function() {
  if (this.location.y < height/1.78) {
    this.location.y = height;
    this.location.x = random(0, width);
  }
};

function Friction(X, Y, W, H, cd) {
  this.C = cd;
  this.x = X;
  this.y = Y;
  this.w = W;
  this.h = H;
};

Friction.prototype.display = function() {
  noStroke();
  fill(35, 98, 195);
  rect(this.x, this.y, this.w, this.h);
};

function Ball(m, start_x, start_y, R) {
  this.location = createVector(start_x, start_y);
  this.velocity = createVector(0, 0);
  this.acceleration = createVector(0, 0);
  this.mass = m;
  this.rad = R;
  this.edges = 0;
  this.drag = createVector(0, 0);
};

Ball.prototype.applyForce = function(f) {
  var grav = p5.Vector.div(f, this.mass);
  this.acceleration.add(grav);
};

Ball.prototype.update = function() {
  this.velocity.add(this.acceleration);
  this.location.add(this.velocity);
  this.acceleration.mult(0);
};

Ball.prototype.isInside = function(F) {
  if (this.location.y > F.y) {
    this.edges = 1;
  }
};

Ball.prototype.Drag = function(F) {
  var speed = this.velocity.mag();
  var forceMag = F.C * speed * speed;
  var force = createVector(this.velocity.x, this.velocity.y);
  force.mult(-1);
  force.normalize();
  force.mult(forceMag);
  var drag = p5.Vector.div(force, this.mass);
  this.acceleration.add(drag);
};

Ball.prototype.display = function() {
  stroke(0);
  strokeWeight(1);
  fill(199, 0, 57);
  ellipse(this.location.x, this.location.y, this.rad, this.rad);
};

Ball.prototype.checkEdges = function() {
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
