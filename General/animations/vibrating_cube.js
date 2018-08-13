

var p = [];  
var N = 100; //particle number


function setup() {
  createCanvas(400, 400);
  // Create object
   for (var i = 0; i < N; i++) {
    	p[i] = new particle();
    }

}

function draw() {
  background(255);
  for (var i = 0; i < p.length; i++){
  	p[i].move();
  	p[i].display();
  }
}

// particle class
function particle() {
  this.x = random(width);
  this.y = random(height);
  this.diameter = 10;
  this.speed = 1;

  this.move = function() {
    this.x += random(-this.speed, this.speed);
    this.y += random(-this.speed, this.speed);
  };

  this.display = function() {
  	noStroke();
  	fill(81,226,235)
    ellipse(this.x, this.y, this.diameter, this.diameter);
  };
}