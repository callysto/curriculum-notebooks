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


class Mover {
  PVector location;
  PVector velocity;
  PVector acceleration;
  float rad;
  
  
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    
    location = new PVector(x_loc,y_loc);
    velocity = new PVector(x_vel,y_vel);
    acceleration = new PVector();
    rad = 0.02;
  }
  
  void update(int dist) {
    location.x = 350 + sin(rad)*(dist);
    location.y = 100 + cos(rad)*(dist);
    rad = rad + 0.02;
  }
  
  void display(int i, int rad) {
    stroke(0);
    //red
    if (i == 0) {
      fill(255,0,0);
    }else if (i == 1) {
      fill(12,48,224);
    }else if (i == 2) {
      fill(255,255,255);
    }
    ellipse(location.x,location.y,rad,rad);
  }
}

class Photon {
  PVector location;
  PVector velocity;
  
  Photon(float x_loc, float y_loc, float x_vel, float y_vel) {
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


void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

int x = 0;
void setup() {
  size(700,200);
  
}



//create stationary proton
Mover proton = new Mover(350,100,0,0);
//create electron
Mover electron = new Mover(350,50,0,0);

Mover n3 = new Mover(350,100,0,0);
Mover n2 = new Mover(350,100,0,0);

Photon red = new Photon(350,100,2,0.5);



//create text for energy levels

// create text for n = 3
float n3x_loc = 420;
float n3y_loc = 100;
float n3x_vel = 0;
float n3y_vel = 0;
String n3_message = "n = 3";
int n3_size = 12;
float[] n3_col = {0,0,0};
TextBox n3_text = new TextBox(n3x_loc,n3y_loc, n3x_vel, n3y_vel);


// create text for n = 2
float n2x_loc = 375;
float n2y_loc = 100;
float n2x_vel = 0;
float n2y_vel = 0;
String n2_message = "n = 2";
int n2_size = 12;
float[] n2_col = {0,0,0};
TextBox n2_text = new TextBox(n2x_loc,n2y_loc, n2x_vel, n2y_vel);


void draw() {
  background(255);
  textSize(24);
  fill(0);
  text("Electron Transition in Hydrogen Atom", 145, 30);
  
  textSize(24);
  
  if (x == 1) {
    //shift electron to n = 2, emit light
    n3.display(2,120);
    n2.display(2,40);
    n2_text.display(n2_message, n2_size,n2_col);
    proton.display(1,16);
    electron.display(0,8);
    electron.update(20);
    red.display(0,20);
    red.update();
    
  } else {
    //make electron orbit around n = 3
    n3.display(2,120);
    n3_text.display(n3_message, n3_size,n3_col);
    n2.display(2,40);
    proton.display(1,16);
    electron.display(0,8);
    electron.update(60);
  }
    

}
