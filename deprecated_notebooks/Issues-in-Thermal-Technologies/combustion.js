var check;
function setup() {
    createCanvas(700, 300);
    fuel = new particle(100,height-50,50)
    heat = new particle(width/2,height-50,90)
    o2 = new particle(600,height-50,50)
    co2 = new particle(width/2,height-50,50)
    h2o = new particle(width/2,height-50,50)
    check = 0;
}


function draw() {
	var v = createVector(1.8,0)
	var v2 = createVector(-1.8,0)
	var v3 = createVector(1.0,-2.0)
	var v4 = createVector(-1.0,-2.0)
    var v0 = createVector(0,0)
	background(255);
	fuel.display(55,55,55,"fuel",251,30,30)
	o2.display(153,247,248,"O\u2082",0,0,0)
	co2.display(174,174,174,"CO\u2082",0,0,0)
	h2o.display(6,125,238,"H\u2082O",0,0,0)
	heat.display(224,72,15,"heat",0,0,0)
	h2o.move()
	o2.move()
	co2.move()
	fuel.move()
	if (mouseIsPressed&&check==0){
		fuel.speed = v
		o2.speed = v2
        check = 1
	}
//     if (mouseIsPressed&&check==1){
//         fuel.speed = v0
//         o2.speed = v0
//         h2o.speed = v0
//         co2.speed = v0
//         co2.location = createVector(width/2,height-50)
//         h2o.location = createVector(width/2,height-50)
//         fuel.location = createVector(100,height-50)
//         o2.location = createVector(600,height-50)
//         check = 0
// 	}
	if (o2.location.x < heat.location.x ){
		o2.location.x = 600
		fuel.location.x = 100
		co2.location = createVector(width/2,height-50)
		h2o.location = createVector(width/2,height-50)
		co2.speed = v3 
		h2o.speed = v4
    }


}



var particle = function(x,y,r) {
	this.location = createVector(x,y)
	this.speed = createVector(0,0)
	this.radius = r
}

particle.prototype.display = function(R,G,B,s,R2,G2,B2){
	fill(R,G,B)
	ellipse(this.location.x,this.location.y,this.radius,this.radius)
	fill(R2,G2,B2)
	textAlign(CENTER, CENTER)
	textStyle(BOLD)
	textSize(15)
	text(s,this.location.x,this.location.y)
}

particle.prototype.move = function(){
	this.location.add(this.speed);
	this.speed.limit(5);
}