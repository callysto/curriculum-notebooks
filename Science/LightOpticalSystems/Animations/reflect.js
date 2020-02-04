
var light;
var m_val = 0;
var x_origin = 250;
var y_origin = 250;

function setup() {
 createCanvas(500,275);
 angleMode(DEGREES);
}

function draw() {
 background(255,255,255);
 text_box('Reflection',23,200,30);
 text_box('Normal', 14,230,70);
 
 //define the new origin
 translate(x_origin,y_origin);
 
 //draw angle size
  fill(255,255,255);
  stroke(0);
  if (mouse_angle() != 0 && m_val == 1){
   arc(0,0,70,70,-90 - abs(mouse_angle()),-90 + abs(mouse_angle()));
   //show angle
  text_box((nfc(abs((mouse_angle())),1) + '\xB0'),15,-50,-50);
  text_box((nfc(abs((mouse_angle())),1) + '\xB0'),15,35,-50);
  }
  
  //draw the reflective surface
 fill(7,189,239);
 stroke(0);
 rect(-150,0,300,10);
 
  
 //draw normal
 fill(0);
 rect(-1,-170,2,170);
 //create the flashlight
 light = new flash(0,-150);
 
 rotations();
 
 
 
 
 
}


function flash(x_pos,y_pos){
 //create a flashlight
 this.location = createVector(x_pos,y_pos);
 
}
 //draw the flashlight
flash.prototype.draw = function() {
 var x = this.location.x;
 var y = this.location.y;
 //draw bottom
 noStroke(0);
 fill(0);
 var bottom = rect(x-10,y-10,20,10);
 //draw triangle
 var tri = triangle(x-10,y-10,x,y-30,x+10,y-10);
 //draw handle
 var handle = rect(x-5,y-60,10,40);
 
};

flash.prototype.shine1 = function(){
 //when the mouse is clicked, turn on the flashlight
 var x = this.location.x;
 var y = this.location.y;
 
 if (m_val == 1) {
  //mouse pressed, show beams
  noStroke();
  fill(239,239,7);
  
  rect(x-3,y,6,150);
  ellipse(0,0,6);
 }else if(m_val == 0){
 }
 
};

flash.prototype.shine2 = function(){
 //when the mouse is clicked, turn on the flashlight
 var x = this.location.x;
 var y = this.location.y;
 
 if (m_val == 1) {
  //mouse pressed, show beam
  noStroke();
  fill(239,239,7);
  triangle(x-7,y,x,y-7,x+7,y);
  rect(x-3,y,6,150);
  ellipse(0,0,6);
 }else if(m_val == 0){
  
 }
 
};

function mousePressed(){
 //change value of m_val
 if (m_val == 0){
  m_val = 1;
 }else if(m_val == 1){
  m_val = 0;
 }
 
}


function mouse_angle(){
 
 //return the angle that the mouse makes with the origin
 
 theta = atan((mouseX-x_origin)/(mouseY-y_origin));
 if (abs(theta) <= 90){
  return theta;
 }else{
  return 90;
 }
}

function text_box(tex,size,x_pos,y_pos){
 //create a text box 
 textSize(size);
 fill(0);
 text(tex,x_pos,y_pos);
}


function rotations(){
 //rotate the light about the new origin
 rotate(-(mouse_angle()));
 //draw the light
 light.draw();
 

 //shine the light
 light.shine1();
 rotate(2*(mouse_angle()));
 light.shine2();
 rotate();
 
 
}











