


var v1;
var slider;
var s;
var px;
var py;

var particle_num = 100;
var p = [];
function setup() {
    createCanvas(400, 400);
    for (var i = 0; i < particle_num; i++) {
    	p[i] = new particle();
    }
    slider = createSlider(0,100,20);
  
}

function draw() { 
	background(255);
  stroke(0);
  strokeWeight(1);
  line(0,height-55,0,0);
  line(width,0,0,0);
  line(width-2,height-55,0,height-55);
  line(width-1,height-55,width-1,0);

  slider.position(180,370);
  textFont("Helvetica");
  textSize(16);
  textStyle(BOLD);
  text("Temperature", slider.x - 110, 380);
  var temp = str(slider.value()) + "\u00b0 C"; 
  text(temp + "", slider.x + slider.width, 380);
	for (var i = 0; i < p.length; i++){

    px = p[i].velocity.x;
    py = p[i].velocity.y;
    if (slider.value() != s){
      p[i].velocity = createVector(px*(0.01 + slider.value()*0.05)/abs(px),py*(0.01 + slider.value()*0.05)/abs(py));

    }
    if (slider.value() == 0){
      px = 0.1;
      py = 0.1;
    }

    var r = 20 + slider.value()*2.17
    var b = 240 - slider.value()*2.4
		p[i].display(r,b);
		p[i].update();
		p[i].checkEdges();	
		for (var j = 0; j < p.length; j++){
			var d = dist(p[i].location.x,p[i].location.y,p[j].location.x,p[j].location.y);
			if (i != j && d < 10 ){
				v1 = p[i].velocity;
				p[i].velocity = p[j].velocity;
				p[j].velocity = v1
			}
		}
	}
  s = slider.value();
}




var particle = function() {
  this.location = createVector(random(width), random(height));
  this.velocity = createVector(random(-1,1),random(-1,1));
};


  
particle.prototype.update = function() {
  this.location.add(this.velocity);

};

particle.prototype.display = function(r,b) {
  noStroke()
  fill(r,50,b);
  ellipse(this.location.x,this.location.y,10,10);
};



particle.prototype.checkEdges = function() {
  if (this.location.x > width) {
    this.location.x = width;
    this.velocity.x *= -1;

  } else if (this.location.x < 0) {
    this.velocity.x *= -1;
    this.location.x = 0;
  }

  if (this.location.y > height-60) {
    this.velocity.y *= -1;
    this.location.y = height - 60;
  }
  if (this.location.y < 0) {
    this.velocity.y *= -1;
    this.location.y = 0;
  }
};

