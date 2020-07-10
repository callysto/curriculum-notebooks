//annihilation reaction

//for beta- decay, releases electron and anti neutrino
//large number of neutrinos, neurtino changes into a proton

class AnnihilationMover extends Mover {
  AnnihilationMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int rad, int col) {
    stroke(0);

    //purple positron
    if (col == 0) {
      fill(154, 5, 198);
    }
    //red electron
    else if (col == 1) {
      fill(255, 0, 0);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

boolean check_collision(AnnihilationMover one, AnnihilationMover two) {
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
}

//make two movers
// create positron and electron
AnnihilationMover positron = new AnnihilationMover(50,50,2.0,0.25);
AnnihilationMover electron = new AnnihilationMover(50,150,2.0,-0.25);

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
  } else {
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
