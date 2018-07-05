//annihilation reaction

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



//for beta- decay, releases electron and anti neutrino
//large number of neutrinos, neurtino changes into a proton

class Mover {
  PVector location;
  PVector velocity;
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    
    location = new PVector(x_loc,y_loc);
    velocity = new PVector(x_vel,y_vel);
    
  }
  
  void update() {
    location.add(velocity);
    
  }
    
  void display(int rad, int col) {
    stroke(0);
    //purple positron
    if (col == 0) {
      fill(154, 5, 198);
    }
    //red electron
    else if(col == 1) {
      fill(255,0,0);
    }
    ellipse(location.x,location.y,rad,rad);
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



boolean check_collision(Mover one, Mover two) {
  //take the coordinates of each particle and check if they are the same
  
  if(one.location.x == two.location.x && one.location.y == two.location.y) {
    return true;
  } else {
    return false;
  }
}

//create two movers, a positron and an electron
//have them move to the same position
//from that position, eject two gamma rays

void setup() {
  size(700,200);
  //make two movers
}
// create positron and electron
Mover positron = new Mover(50,50,2.0,0.25);
Mover electron = new Mover(50,150,2.0,-0.25);

//create gamma rays
Gamma g_up = new Gamma(435,100,2.0,-0.75);
Gamma g_down = new Gamma(435,100,2.0,0.75);

// create text for electron
float ex_loc = 25;
float ey_loc = 170;
float ex_vel = 2;
float ey_vel = -0.25;
String e_message = "Electron";
int e_size = 12;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

// create text for positron
float px_loc = 25;
float py_loc = 40;
float px_vel = 2;
float py_vel = 0.25;
String p_message = "Positron";
int p_size = 12;
float[] p_col = {154, 5, 198};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);



int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}


void draw() {
  background(255);
  textSize(20);
  fill(0);
  text("Annihilation Reaction", 250, 25);
  
  textSize(24);
  
  if (x == 0) {
    electron.display(8,1);
    positron.display(8,0);
    elec_text.display(e_message,e_size,e_col);
    posi_text.display(p_message,p_size,p_col);
  } else{
  
    if (check_collision(electron, positron) == true) {
      //draw two gamma rays
      //up
      g_up.update();
      g_up.display(1,330);
    
      ////down
      g_down.update();
      g_down.display(0,20);
    
    
    } else {
      posi_text.update();
      posi_text.display(p_message,p_size,p_col);
      positron.update();
      positron.display(8,0);
    
      elec_text.update();
      elec_text.display(e_message,e_size,e_col);
      electron.update();
      electron.display(8,1);
    }
  }
  
  
  
}
