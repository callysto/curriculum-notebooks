

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

  let camX = map(mouseX,0,width,-200,200);
  let camY = map(mouseY,0,height,-200,200);
  
  camera(camX,camY, camX + camY ,0,0,scl*N/2,0,1,0);
//Draw Spheres
  translate(0,height/8,0);
  for (var k = 0; k < N; k ++){
    translate(0,0,scl + random(-0.2,0.2));
    translate(0,-scl*N,0);
    for (var j = 0; j < N; j++){
      translate(0,scl + random(-0.2,0.2),0); 
      translate(-scl*N,0,0);
      for (var i = 0; i < N; i++){
        translate(scl + random(-0.2,0.2),0,0);
        normalMaterial();
        sphere(8);

       }
     } 

  }
  
}