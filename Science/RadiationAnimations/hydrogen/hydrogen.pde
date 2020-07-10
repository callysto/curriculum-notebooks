class HydrogenMover extends Mover {
  float rad;
  
  HydrogenMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
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
      fill(255, 0, 0);
    } else if (i == 1) {
      fill(12, 48, 224);
    } else if (i == 2) {
      fill(255, 255, 255);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

// Implementations are identical so using inheritance to "alias" Gamma
class Photon extends Gamma {
  Photon(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }
}

int x = 0;

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void setup() {
  size(700,200);
}

//create stationary proton
HydrogenMover proton = new HydrogenMover(350,100,0,0);
//create electron
HydrogenMover electron = new HydrogenMover(350,50,0,0);

HydrogenMover n3 = new HydrogenMover(350,100,0,0);
HydrogenMover n2 = new HydrogenMover(350,100,0,0);

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
