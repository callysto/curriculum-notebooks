

var nums = ['1','2','3','4','5','6','7','8','9','10','11','12']
function setup() {
    createCanvas(400, 400);
    background(255);
    resetSketch();
	button = select('#button')
	button2 = select('#button2')

	button.mousePressed(dart);
	button2.mousePressed(resetSketch);
}


function draw(){
	
 }


function dart() {

	let p = random(0,200);
	let a = random(0,2*PI);
	let v = createVector(200 + p*cos(a), 200 + p*sin(a));
	let y = v.y;
	let x = v.x;
	stroke(0);
	fill(0);
	let r = 5;
	ellipse(x,y,5,5);
	line(x-r,y+r,x+r,y-r);
	line(x-r,y-r,x+r,y+r);
};


function resetSketch(){

	fill(25,25,200);
	ellipse(200,200,400,400);
	fill(200,25,25);
	ellipse(200,200,200,200);
	for (var i = 0; i <= 6; i ++) {
		line(200,200,200 + 200*cos(i*PI/3), 200 + 200*sin(i*PI/3));
	}
	for (var i = 0; i<=5; i++){
		fill(255);
		stroke(3);
		textSize(24);
		textFont("Georgia");
		textAlign(CENTER);
		text(nums[i], 200 + 50*cos(i*PI/3 + PI/6), 200 - 50*sin(i*PI/3 + PI/6));
		text(nums[i+6], 200 + 150*cos(i*PI/3 + PI/6), 200 + 150*sin(i*PI/3 + PI/6))
	}

}