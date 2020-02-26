//for beta- decay, releases electron and anti neutrino
//large number of neutrinos, neurtino changes into a proton

class BetaMinusMover extends Mover {
  BetaMinusMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int i, int rad, int col) {
    stroke(0);

    //red
    if (col == 0) {
      fill(255, 0, 0);
    }
    //green
    else if (col == 1) {
      fill(35, 167, 6);
    }
    //blue
    else if (i % 3 ==0) {
      fill(12, 48, 224);
    } //grey
    else {
      fill(175);
    }

    ellipse(location.x, location.y, rad, rad);
  }
}

BetaMinusMover[] movers = {};

void addMover(float x_loc, float y_loc, float x_vel, float y_vel) {
  movers = (BetaMinusMover[])append(movers, new BetaMinusMover(x_loc, y_loc, x_vel, y_vel));
}

void setup() {
  size(700, 200);
  float[] center = {100.0, 100.0};
  float[][] all_coords = {};
  float[][] orig_coords = position(center[0], center[1], 8.0);
  
  //from the center, make 6 coords
  float[][] coords = position(center[0], center[1], 8.0);

  //make 6 particles
  for (int k = 0; k < 6; k++) {
    //if coords do not yet exist, make the circle, else, don't
    if (!isItemInArray(all_coords, coords[k])) {
      //create the mover
      // add the mover to the movers list
      addMover(coords[k][0], coords[k][1], 0, 0);
      
      //add coords to the list
      all_coords = (float[][])append(all_coords, coords[k]);
    }
  }

  //now change the center and make new circles
  for (int i = 0; i < 6; i++) {
    //redefine the center 
    center[0] = orig_coords[i][0];
    center[1] = orig_coords[i][1];

    //from the center, make 6 coords
    float[][] new_coords = position(center[0], center[1], 8.0);

    //make 6 particles
    for (int k = 0; k < 6; k++) {
      //if coords do not yet exist, make the circle, else, don't
      if (!isItemInArray(all_coords, new_coords[k])) {
        //create the mover
        // add the mover to the movers list
        addMover(new_coords[k][0], new_coords[k][1], 0, 0);

        //add coords to the list
        all_coords = (float[][])append(all_coords, new_coords[k]);
      }
    }
  }
}

BetaMinusMover[] make_betas() {
  // each mouse click, eject an alpha particle
  BetaMinusMover[] betas = {};
  //electron
  betas = (BetaMinusMover[])append(betas, new BetaMinusMover(100.0,100.0,4.0,-0.4));
  //antineutrino
  betas = (BetaMinusMover[])append(betas, new BetaMinusMover(100.0,100.0,4.0,0.4));
  return betas;
}

// create the alpha particle
BetaMinusMover[] betas = make_betas();
int x = 0;

// create text for electron
float ex_loc = 50;
float ey_loc = 120;
float ex_vel = 4;
float ey_vel = -0.4;
String e_message = "Electron";
int e_size = 18;
float[] e_col = {255,0,0};
TextBox elec_text = new TextBox(ex_loc,ey_loc, ex_vel, ey_vel);

// create text for antineutrino
float ax_loc = 50;
float ay_loc = 120;
float ax_vel = 4;
float ay_vel = 0.4;
String a_message = "Antineutrino";
int a_size = 18;
float[] a_col = {35, 167, 6};
TextBox anti_text = new TextBox(ax_loc,ay_loc, ax_vel, ay_vel);

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  textSize(32);
  fill(0);
  text("Beta Minus Decay", 220, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < betas.length; i++) {
      betas[i].update();
      betas[i].display(i,8,i);
    }
    //draw electron text
    elec_text.update();
    elec_text.display(e_message, e_size, e_col);
    //draw anti neutrino text
    anti_text.update();
    anti_text.display(a_message,a_size,a_col);
    
    for (int i = 0; i < (movers.length) - 2; i++) {
      movers[i].update();
      movers[i].display(i,16,2);
    }
    //add a proton
    movers[17].display(3,16,2);
    movers[18].display(3,16,2);
    fill(9, 49, 245);
    text("Protons - 8", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 11", 20, 190);
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i,16,2);
      }
    fill(9, 49, 245);
    text("Protons - 7", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 12", 20, 190);
  }
}
