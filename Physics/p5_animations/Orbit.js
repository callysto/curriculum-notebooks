var sun = [];
var orbiter;
var star = [];
var html_r = 232;
var html_b = 34;
var step = 0.03;
var m_old = 6;
var html_g  = [];
var sun_mass = [];
var img;
function setup() {
  createCanvas(600,500);
  img = loadImage("test.JPG"); 
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



var theta = 0;
function draw() {
  background(0);
  image(img,100,100);
  for (var i = 0; i < star.length; i++) {
    star[i].display();
  }

  for (var i = 0; i < sun.length; i++) {
    sun[i].display(15);
  }
  theta += 0.003
  var new_x = 200*cos(theta) + sun[0].location.x;
  var new_y = 200*sin(theta) + sun[0].location.y;
  orbiter.display(255);
  orbiter.update(new_x,new_y);
  stroke(255);
  strokeWeight(1);
  line(width/2,height/2,orbiter.location.x,orbiter.location.y);

  var x_rot = cos(-PI/2)*(width/2-new_x) - sin(-PI/2)*(height/2-new_y) + new_x;
  var y_rot = sin(-PI/2)*(width/2-new_x) + cos(-PI/2)*(height/2-new_y) + new_y;
  stroke(190,85,236);
  line(orbiter.location.x,orbiter.location.y,x_rot,y_rot);
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
  image(I,this.location.x,this.location.y)
};

earth.prototype.update() = function(en_x,en_y) {
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