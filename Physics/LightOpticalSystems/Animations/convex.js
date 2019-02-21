// create an animation where you can change the focal point by altering the shape of the lens
// the lens will be made of two arcs, then two lines on top and bottom
// define its boundaries in order to know when light intersects with it
// incoming light beams will refract at different angles depending on convexity

var m_val = 0;

function setup() {
 createCanvas(400,400);
 angleMode(DEGREES);
 
}

function draw() {
 background(255,255,255);
 text_box('Convex Lens',15,157,165);
 text_box('Concave Lens',15,155,365);
 text_box('Click buttons to change shape of lenses',10,112,200);
 translate(200,200);
 
 fill(41, 239, 31);
 stroke(0);
 ellipse(0,-20,15,15);
 text_box('+',17,-5,-16);
 fill(41, 239, 31);
 stroke(0);
 ellipse(0,20,15,15);
 text_box('-',20,-3,26);
 
 
 vex_lens = new convex(0,0);
 cave_lens = new concave(0,0);
 
 if (m_val == 0){
  vex_lens.draw1();
  cave_lens.draw1();
 } else if (m_val == 1){
  vex_lens.draw2();
  cave_lens.draw2();
 } else if (m_val == 2){
  vex_lens.draw3();
  cave_lens.draw3();
 }
 
}


function convex(x_pos,y_pos){
 //draw a convex lens
 this.location = createVector(x_pos,y_pos);
 var x = this.location.x;
 var y = this.location.y;
 var x1 = x - 10;
 var x2 = x + 10;
 var y1 = y - 150;
 var y2 = y - 50;
 

convex.prototype.draw2 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x2, y1);
 line(x1, y2, x2, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, -25, -120, -25, -80, x1, y2);
 bezier(x2, y1, 25, -120, 25, -80, x2, y2);
 
 rays('vex',2);
 };
 
convex.prototype.draw3 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x2, y1);
 line(x1, y2, x2, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, -30, -120, -30, -80, x1, y2);
 bezier(x2, y1, 30, -120, 30, -80, x2, y2);
 
 rays('vex',3);
 
};

convex.prototype.draw1 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x2, y1);
 line(x1, y2, x2, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, -20, -120, -20, -80, x1, y2);
 bezier(x2, y1, 20, -120, 20, -80, x2, y2);
 
 rays('vex',1);
 
};

}

function concave(x_pos,y_pos){
 //draw a concave lens
 this.location = createVector(x_pos,y_pos);
 var x = this.location.x;
 var y = this.location.y;
 var x1 = x - 20;
 var x2 = x + 20;
 var y1 = y + 50;
 var y2 = y + 150;
 
 
 

concave.prototype.draw2 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x2, y1);
 line(x1, y2, x2, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, -5, 80, -5, 120, x1, y2);
 bezier(x2, y1, 5, 80, 5, 120, x2, y2);

 rays('cave',2);
 };
 
 concave.prototype.draw3 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x + 20, y1);
 line(x1, y2, x + 20, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, 0, 80, 0, 120, x1, y2);
 bezier(x2, y1, 0, 80, 0, 120, x2, y2);
 
 rays('cave',3);
 };
 
 concave.prototype.draw1 = function() {
 
 //draw line on top and bottom
 stroke(0);
 line(x1, y1, x2, y1);
 line(x1, y2, x2, y2);
 //draw the two curves
 noFill();
 bezier(x1, y1, -10, 80, -10, 120, x1, y2);
 bezier(x2, y1, 10, 80, 10, 120, x2, y2);
 
 rays('cave',1);
 };
 
}

function rays(lens,num){
 
 if (lens == 'vex' && num == 1){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = -125;
 var l2 = -100;
 var l3 = -75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l1,190,-100);
 line(q2,l2,190,-100);
 line(q2,l3,190,-100);
 
 } else if(lens == 'vex' && num == 2){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = -125;
 var l2 = -100;
 var l3 = -75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l1,190,-75);
 line(q2,l2,190,-100);
 line(q2,l3,190,-125);
 
 
} else if(lens == 'vex' && num == 3){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = -125;
 var l2 = -100;
 var l3 = -75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l1,190,-50);
 line(q2,l2,190,-100);
 line(q2,l3,190,-150);
 
}



if (lens == 'cave' && num == 1){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = 125;
 var l2 = 100;
 var l3 = 75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l3,150,50);
 line(q2,l2,150,100);
 line(q2,l1,150,150);
 } else if(lens == 'cave' && num == 2){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = 125;
 var l2 = 100;
 var l3 = 75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l3,150,25);
 line(q2,l2,150,100);
 line(q2,l1,150,175);
 
} else if(lens == 'cave' && num == 3){
  //assign values
 var q1 = -150;
 var q2 = 0;
 var l1 = 125;
 var l2 = 100;
 var l3 = 75;
  //draw rays
 stroke(18, 7, 237);
 line(q1,l1,q2,l1);
 line(q1,l2,q2,l2);
 line(q1,l3,q2,l3);
 
 line(q2,l3,150,0);
 line(q2,l2,150,100);
 line(q2,l1,150,200);
}


}

function mousePressed(){
 //change value of m_val
 var d1 = dist(mouseX,mouseY,200,180);
 var d2 = dist(mouseX,mouseY,200,220);
 
 if (d1 < 20 && m_val != 2 ){
  m_val = m_val + 1;
 } 
 
 if (d2 < 20 && m_val != 0){
  m_val = m_val - 1;
 }
}

function text_box(tex,size,x_pos,y_pos){
 //create a text box 
 textSize(size);
 fill(0);
 stroke(0);
 text(tex,x_pos,y_pos);
}