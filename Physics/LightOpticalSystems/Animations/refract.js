var light;
var m_val = 0;
var x_origin = 250;
var y_origin = 150;

function setup() {
 createCanvas(500,300);
 angleMode(DEGREES);
}

function draw() {
 background(255,255,255);
 text_box('Refraction',23,200,30);
 text_box('Air',16,20,120);
 
 
 //define the new origin
 translate(x_origin,y_origin);
 ref_angle = refract_angle(1.00,1.33,mouse_angle());
 
 //draw the water
 fill(7,189,239);
 noStroke();
 rect(-(width/2),0,width,(height/2));
 text_box('Water',16,-230,30);
 

 //draw angle size
  fill(255,255,255);
  stroke(0);
  if (int(mouse_angle()) < 0 && m_val == 1){
   //draw upper angle
   arc(0,0,70,70,-90,-90 + abs((mouse_angle())));
   //show upper angle
   text_box((nfc(abs((mouse_angle())),1) + '\xB0'),15,35,-50);
   
   //draw lower angle
   fill(7,189,239);
   stroke(0);
   arc(0,0,70,70,90,90 + (abs((ref_angle))));
   //show lower angle
   text_box((nfc((abs((ref_angle))),1) + '\xB0'),15,-45,120);
   
  } else if (int(mouse_angle()) > 0 && m_val == 1){
   //draw upper angle
   arc(0,0,70,70,-90 - abs((mouse_angle())),-90);
   //show upper angle
   text_box((nfc(abs((mouse_angle())),1) + '\xB0'),15,-50,-50);
   //draw lower angle
   fill(7,189,239);
   stroke(0);
   arc(0,0,70,70,90 - (abs(ref_angle)), 90);
   //show lower angle
   text_box((nfc(abs((ref_angle)),1) + '\xB0'),15,15,120);
    
  }
  //draw normal
  fill(0);
  rect(-1,-100,2,200);
  //create the flashlight
  light = new flash(0,-100);
 
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
 var bottom = rect(x-5,y-5,10,5);
 //draw triangle
 var tri = triangle(x-5,y-5,x,y-15,x+5,y-5);
 //draw handle
 var handle = rect(x-2.5,y-30,5,20);
 
};

flash.prototype.shine1 = function(){
 //when the mouse is clicked, turn on the flashlight
 var x = this.location.x;
 var y = this.location.y;
 
 if (m_val == 1) {
  //mouse pressed, show beams
  noStroke();
  fill(239,239,7);
  rect(x-3,y,6,100);
  ellipse(0,0,6);
 }else if(m_val == 0){
 }
 
};

flash.prototype.shine2 = function(){
 //when the mouse is clicked, turn on the flashlight
 var x = this.location.x;
 var y = this.location.y;
 
 if (m_val == 1) {
  //mouse pressed, show beams
  noStroke();
  fill(239,239,7);
  triangle(x-7,y,x,y-7,x+7,y);
  rect(x-3,y,6,100);
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


function refract_angle(n_1,n_2,inc_angle){
    //get the angle of refraction for a given medium, incident angle
    theta = asin((n_1/n_2)*(sin(inc_angle)));
    return theta;
}

function rotations(){
 //rotate the light about the new origin
 rotate(-(mouse_angle()));
 //draw the light
 light.draw();
 

 //shine the light
 light.shine1();
 
 //refract the light
 ref_angle = refract_angle(1.00,1.33,mouse_angle());
 rotate((180 + mouse_angle()) - ref_angle);
 light.shine2();
 //rotate();
 
 
}











