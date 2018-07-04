//this animation shows how the decceleration of a particle can produce gamma rays

// need a large stationary charge -- proton
//need an electron moving in a straight line, then need it to bend into an arc
//at the moment it bends, emit gamma rays
//electron goes off screen

import java.lang.*;

class Mover {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float mass;
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc,y_loc);
    velocity = new PVector(x_vel,y_vel);
    acceleration = new PVector();
  }
  void update() {
    location.add(velocity);
    velocity.add(acceleration);
  }
  
  void applyForce(PVector force) {
    acceleration = force;
  }
 
  PVector attract(Mover m, float G, float m1, float m2) {
    PVector force = PVector.sub(location,m.location);
    float distance = force.mag();

    distance = constrain(distance,5.0,25.0);
 
 
    force.normalize();
    float strength = (G * m1 * m2) / (distance * distance);
    force.mult(strength);
    return force;
}
 
  
  void display(int rad, int col) {
    stroke(0);
    //blue proton
    if (col == 0) {
      fill(12,48,224);
    }
    //red electron
    else if(col == 1) {
      fill(255,0,0);
    }
    ellipse(location.x,location.y,rad,rad);
  }
}

class TextBox {
  PVector location;
  PVector velocity;
  
  TextBox(float x_loc, float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }
  void update() {
    location.add(velocity);
  }
  
  void display(String message, int size, float[] col) {
    textSize(size);
    fill(col[0],col[1],col[2]);
    text(message, location.x, location.y);
  }
}

class Gamma {
  PVector location;
  PVector velocity;
  
  Gamma(float x_loc, float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }
  void update() {
    location.add(velocity);
  }
  
  //creates squiggly lines for a gamma ray
  float[] two_lines(float x_val, float y_val, int i) {
    //upwards gamma
    if (i == 1) {
      // return the coordinates of two perpendicular lines
      float[][] coords = {{x_val,y_val,(x_val + 3),(y_val - 10)}, {(x_val + 3),(y_val - 10),(x_val + 15),(y_val - 12)}};
      line(coords[0][0],coords[0][1],coords[0][2],coords[0][3]);
      line(coords[1][0],coords[1][1],coords[1][2],coords[1][3]);
      float[] end = {coords[1][2],coords[1][3]};
      return end;
    } else {
      float[][] coords = {{x_val,y_val,(x_val + 3),(y_val + 10)}, {(x_val + 3),(y_val + 10),(x_val + 15),(y_val + 8)}};
      line(coords[0][0],coords[0][1],coords[0][2],coords[0][3]);
      line(coords[1][0],coords[1][1],coords[1][2],coords[1][3]);
      float[] end = {coords[1][2],coords[1][3]};
      return end;
    }
  }
  void drawArrow(float cx, float cy, int len, float angle){
    pushMatrix();
    translate(cx, cy);
    rotate(radians(angle));
    line(0,0,len, 0);
    line(len, 0, len - 8, -8);
    line(len, 0, len - 8, 8);
    popMatrix();
  }
  
  void display(int i, int angle) {
    stroke(255,0,0);
    float[] x = two_lines(location.x,location.y,i);
    float[] y = two_lines(x[0],x[1],i);
    float[] z = two_lines(y[0],y[1],i);
    drawArrow(z[0],z[1],10,angle);
    
  }
}




// main function



//create stationary proton
Mover proton = new Mover(350,100,0,0);

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
Mover electron = new Mover(8,30,9,2);

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
  //make two movers
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
