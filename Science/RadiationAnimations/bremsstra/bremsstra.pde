//this animation shows how the decceleration of a particle can produce gamma rays

// need a large stationary charge -- proton
//need an electron moving in a straight line, then need it to bend into an arc
//at the moment it bends, emit gamma rays
//electron goes off screen

import java.lang.*;

class BremsstraMover extends Mover {
  PVector acceleration;

  BremmstraMover(float x_loc,float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
    acceleration = new PVector();
  }

  void update() {
    location.add(velocity);
    velocity.add(acceleration);
  }
  
  void applyForce(PVector force) {
    acceleration = force;
  }
 
  PVector attract(BremsstraMover m, float G, float m1, float m2) {
    PVector force = PVector.sub(location, m.location);
    float distance = force.mag();

    distance = constrain(distance, 5.0, 25.0);
 
    force.normalize();
    float strength = (G * m1 * m2) / (distance * distance);
    force.mult(strength);
    return force;
  }
  
  void display(int rad, int col) {
    stroke(0);

    //blue proton
    if (col == 0) {
      fill(12, 48, 224);
    }
    //red electron
    else if(col == 1) {
      fill(255, 0, 0);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

// main function

//create stationary proton
BremmstraMover proton = new BremmstraMover(350,100,0,0);

// create text for positron
float px_loc = 305;
float py_loc = 120;
float px_vel = 0;
float py_vel = 00;
String p_message = "Positive Charge";
int p_size = 12;
float[] p_col = {12,48,224};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);

//create moving electron 
BremmstraMover electron = new BremmstraMover(8,30,9,2);

// create text for electron
float ex_loc = 8;
float ey_loc = 50;
float ex_vel = 9;
float ey_vel = 2;
String e_message = "Electron";
int e_size = 12;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

//create gamma rays
Gamma g_up = new Gamma(350,100,4.0,-1.0);
Gamma g_down = new Gamma(350,100,4.0,1.0);

int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void setup() {
  size(700,200);
  frameRate(35);
}

void draw() {
  background(255);
  textSize(20);
  fill(0);
  text("Bremsstrahlung Radiation", 230, 25);
  
  if (x == 0) {
    proton.display(16,0);
    electron.display(8,1);
    posi_text.update();
    posi_text.display(p_message,p_size,p_col);
    elec_text.display(e_message,e_size,e_col);
  } else{
    posi_text.update();
    posi_text.display(p_message,p_size,p_col);
    proton.display(16,0);
    PVector grav = proton.attract(electron, -9, 5.0, 2);
    electron.applyForce(grav);
    electron.update();
    electron.display(8,1);
  
    //emit gamma rays when it deccelerates
    if (electron.location.x > 288) {
      //draw two gamma rays
      //up
      g_up.update();
      g_up.display(1,330);
      ////down
      g_down.update();
      g_down.display(0,20);
    }
  }
}
