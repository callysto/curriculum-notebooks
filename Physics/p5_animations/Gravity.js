// // var b = [];
// var star = [];
// function setup() {
//   createCanvas(600,500);
//   // for (var i = 0; i < 10; i++) {
//   // 	var M = random(3,7);
//   // 	if (i == 0) 
//   // 	{
// 		// b[i] = new Ball(M,M*2,40);
//   // 	} 
//   // 	else 
//   // 	{
//   // 		b[i] = new Ball(M,(M+m_old)*2,40);
//   // 	}
//   // 	var m_old = M;
//   // }




// };


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
    star[i] = new Star(0.5,x,y);
  }

};

// function drawArrow(x0,y0,x1,y1) {
//   strokeWeight(20);
//   stroke(255, 87, 51);
//   triangle(x1,y1+2,x1,y1-2,x1+3.5,y1);
//   line(x0,y0,x1,y1);
// };


var check = 0;
function draw() {
  background(0);
  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }
  var gravity = createVector(0,0.32);
  stroke(0);
  fill(0);
  if (check == 0) {
  	var txt = new r_text("CLICK TO APPLY GRAVITATIONAL FORCE");
   } 
   else 
   {
   	var txt = new r_text(" ");
   }
  
  for (var i = 0; i < b.length; i++) {
  	if (mouseIsPressed) {
  		check = 1;
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
  this.velocity.limit(0.6);
};

Ball.prototype.display = function() {
  stroke(0);
  strokeWeight(1);
  fill(199,0,57);
  ellipse(this.location.x,this.location.y,this.rad,this.rad);
};


Ball.prototype.checkEdges = function() {
  // if (this.location.x > width) {
  //   this.location.x = width;
  //   this.velocity.x *= -1;

  // } else if (this.location.x < 0) {
  //   this.velocity.x *= -1;
  //   this.location.x = 0;
  // }
  
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
  stroke(255,255,255);
  fill(255,255,255);
  ellipse(this.x,this.y,this.radius,this.radius);
};

};