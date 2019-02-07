class AlphaMover extends Mover {
  AlphaMover(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  void display(int i) {
    stroke(0);

    if (i % 2 == 0) {
      fill(175);
    } else {
      fill(12,48,224);
    }

    ellipse(location.x, location.y, 16, 16);
  }
}

AlphaMover[] movers = {};

void addMover(float x_loc, float y_loc, float x_vel, float y_vel) {
  movers = (AlphaMover[])append(movers, new AlphaMover(x_loc, y_loc, x_vel, y_vel));
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

AlphaMover[] make_alpha() {
  // each mouse click, eject an alpha particle
  AlphaMover[] alphas = {};
  float[] center = {100.0,100.0};
  
  //will use 0, 1, 2
  float[][] coords = position(center[0],center[1],8.0);
  float[][] get_center = position(coords[0][0],coords[0][1],8.0);
  //and this coord
  float[][] center_coord = {{get_center[3][0],get_center[3][1]}};
  
  float[][] alpha_coords = {};
  for (int k = 0; k < 3; k++) {
    alpha_coords = (float[][])append(alpha_coords,coords[k]);
  }
  alpha_coords = (float[][])append(alpha_coords,center_coord[0]);
  
  //alpha coords is now the list of coordinates for the alpha particle
  for (int k = 0; k < 4; k++) {
    alphas = (AlphaMover[])append(alphas,new AlphaMover(alpha_coords[k][0],alpha_coords[k][1],2,0));
  }
  return alphas;
}

// create text for alpha
float ax_loc = 50;
float ay_loc = 135;
float ax_vel = 0.5;
float ay_vel = 0;
String a_message = "Alpha Particle";
int a_size = 18;
float[] a_col = {9,49,245};
TextBox alpha_text = new TextBox(ax_loc,ay_loc, ax_vel, ay_vel);

// create the alpha particle
AlphaMover[] alphas = make_alpha();

int x = 0;
void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}

void draw() {
  background(255);
  textSize(32);
  fill(0);
  text("Alpha Decay", 260, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < alphas.length; i++) {
      alphas[i].update();
      alphas[i].display(i);
      //draw alpha text
      alpha_text.update();
      alpha_text.display(a_message, a_size, a_col);
    }
    for (int i = 0; i < (movers.length - 4); i++) {
      movers[i].update();
      //movers[i].checkEdges();
      movers[i].display(i);
    }
    fill(9, 49, 245);
    text("Protons - 7", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 8", 20, 190);
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i);
      }
    fill(9, 49, 245);
    text("Protons - 9", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 10", 20, 190);
  }
}
