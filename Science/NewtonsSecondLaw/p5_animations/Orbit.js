var sun = [];
var orbiter;
var star = [];
var html_r = 232;
var html_b = 34;
var step = 0.03;
var m_old = 6;
var html_g  = [];
var sun_mass = [];

function setup() {
  createCanvas(600,500);
  for (var i = 0; i < 150; i++) {
    html_g[i] = 75 + i;
    sun_mass[i] = m_old - step;
    m_old -= step;
  }
  for (var i = 0; i < html_g.length; i++) {
    sun[i] = new Ball(sun_mass[i],width/2,height/2,html_r,html_g[i],html_b);
    m_old -= step;
  }

  orbiter = new Ball(2,width/2+200,height/2, 85, 184, 241 );
  for (var i = 0; i < 500; i++) {
    var x = random(width);
    var y = random(height);
    star[i] = new Star(0.8,x,y);
  }
};


var head = 10;
var theta = 0;
function draw() {
  background(0);
  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }

  for (var i = 0; i < sun.length; i++) {
    sun[i].display(15);
  }
  theta += 0.004
  var new_x = 200*cos(theta) + width/2;
  var new_y = 200*sin(theta) + height/2;

  stroke(255);
  strokeWeight(1);
  var vec_x = 100*cos(theta) + width/2;
  var vec_y = 100*sin(theta) + height/2;
  var bodyCenter = createVector(new_x,new_y);
  var mid_radius = createVector(vec_x,vec_y);
  var x_rot = cos(-PI/2)*(vec_x-new_x) - sin(-PI/2)*(vec_y-new_y) + new_x;
  var y_rot = sin(-PI/2)*(vec_x-new_x) + cos(-PI/2)*(vec_y-new_y) + new_y;
  var v = createVector(x_rot,y_rot);
  drawArrow(bodyCenter,v,head, 183, 35, 227 );
  drawArrow(bodyCenter,mid_radius,head, 227, 38, 35 );
  orbiter.display();
  orbiter.update(new_x,new_y);
  stroke(255);
  fill(255);
  text("Gravitational Force",width-200,20);
  text("Velocity",width-200,40);
  stroke(183, 35, 227);
  strokeWeight(10);
  line(width-148,37,width-128,37);
  stroke(227, 38, 35);
  line(width-88,17,width-68,17);
};


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
  noStroke();
  strokeWeight(0);
  fill(this.red,this.green,this.blue,a);
  ellipse(this.location.x,this.location.y,this.mass*20,this.mass*20);
};



function earth(e_x,e_y) {
  this.location = createVector(e_x,e_y);

earth.prototype.display = function(I) {
  imageMode(CENTER);
  image(I,this.location.x,this.location.y,I.width/14,I.height/14);
};

earth.prototype.update = function(en_x,en_y) {
  this.location.x = en_x;
  this.location.y = en_y;
}
}

function Star(r, X, Y) {
  this.x = X;
  this.y = Y;
  this.radius = r;
 
Star.prototype.display = function() {
  stroke(255,255,255);
  strokeWeight(0);
  fill(255,255,255);
  ellipse(this.x,this.y,this.radius,this.radius);
};

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
};