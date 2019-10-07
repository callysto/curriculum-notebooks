
var N = 5; //particle number
var p = [];
var m = 0;
var angle = 0;
var scl = 25;

function setup() {
  createCanvas(400,400,WEBGL);
}

function draw() {

  background(255);

  // strokeWeight(1);
  // line(-width/2 + 3,-height/2 + 3,-width/2,height/2);
  // line(-width/2,-height/2,width/2,-height/2);
  // line(-width/2,height/2,width/2,height/2);
  // line(width/2,-height/2,width/2,height/2);

  let camX = map(mouseX,0,width,-200,200);
  let camY = map(mouseY,0,height,-200,200);
  
  camera(camX,camY, camX + camY ,0,0,scl*N/2,0,1,0);
//Draw Spheres
  translate(0,height/8,0);
  for (var k = 0; k < N; k ++){
    translate(0,0,scl);
    translate(0,-scl*N,0);
    for (var j = 0; j < N; j++){
      translate(0,scl,0); 
      translate(-scl*N,0,0);
      for (var i = 0; i < N; i++){
        translate(scl,0,0);
        normalMaterial();
        sphere(8);
    //     stroke(1);
    //     if (i == N-1){
    //       line(0,0,0,0,-scl,0);
    //       line(0,0,0,-scl,0,0);
    //       line(0,0,0,0,0,0,-scl);
    //     }
    //     if (i != N-1) {
    //       line(0,0,0,0,scl,0);
    //       line(0,0,0,scl,0,0);
    //       line(0,0,0,0,0,0,scl);
    //     }
       }
     } 

  }
  
    angle += 0.02
}





// // particle class
// function particle(x_pos,y_pos,z_pos) {
//   this.x = x_pos;
//   this.y = y_pos;
//   this.z = z_pos;
//   this.diameter = 10;
//   this.speed = 1;

//   // this.move = function() {
//   //   this.x += random(-this.speed, this.speed);
//   //   this.y += random(-this.speed, this.speed);
//   // };

//   this.display = function() {
//   	noStroke();
//   	fill(81,226,235);
//     translate(this.x,this.y,[this.z]);
//     sphere(this.diameter);

//   };
// }