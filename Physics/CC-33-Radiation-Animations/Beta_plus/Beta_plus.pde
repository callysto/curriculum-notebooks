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

//for beta+ decay, releases positrion and neutrino
//large number of protons, proton changes into a neutrino
class Mover {
  PVector location;
  PVector velocity;
  PVector acceleration;
  
  
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    
    location = new PVector(x_loc,y_loc);
    velocity = new PVector(x_vel,y_vel);
    
  }
  
  void update() {
    location.add(velocity);
    
  }
    
  void display(int i, int rad, int col) {
    stroke(0);
    //purple positron
    if (col == 0) {
      fill(154, 5, 198);
    }
    //orange neutrino
    else if(col == 1) {
      fill(255, 111, 6);
    }
    //grey neutrons
    else if(((i)%3)==0) {
      fill(175);
    } //blue protons
    else {
      fill(12,48,224);
    }
    ellipse(location.x,location.y,rad,rad);
  }
}


// new function
float[][] position(float x_val, float y_val, float radius) {
  // make it produce the x and y coordinates for the 6 spots around it
  
  float y_dist = (sin(radians(30)))*(2*radius);
  float x_dist = (cos(radians(30)))*(2*radius);
  
  //coords is a list that contains the new coordinates for 6 circles around one circle
  
  
  float[][] coords = {{(x_val),(y_val-(2*radius))}, {(x_val+x_dist),(y_val-y_dist)}, {(x_val+x_dist),(y_val+y_dist)}, {(x_val),(y_val+(2*radius))}, {(x_val-x_dist),(y_val+y_dist)}, {(x_val-x_dist),(y_val-y_dist)}};
  
  return coords;
}

Mover[] movers = {};


//function to check if a coordinate is already used
boolean isItemInArray(float[][] array, float[] item) {
    for (int i = 0; i < array.length; i++) {
        // This if statement depends on the format of your array
        if (array[i][0] == item[0] && array[i][1] == item[1]) {
            return true;   // Found it
        }
    }
    return false;   // Not found
}




void setup() {
  size(700,200);
  float[] center = {100.0,100.0};
  float[][] all_coords = {};
  float[][] orig_coords = position(center[0],center[1],8.0);
  
  //from the center, make 6 coords
  float[][] coords = position(center[0],center[1],8.0);
  //make 6 particles
  for (int k = 0; k < 6; k++) {
    //if coords do not yet exist, make the circle, else, don't
    boolean x = isItemInArray(all_coords, coords[k]);
    if (x == false){
      //create the mover
      // add the mover to the movers list
      movers = (Mover[])append(movers, new Mover(coords[k][0],coords[k][1],0,0));
      
      //add coords to the list
      
      all_coords = (float[][])append(all_coords,coords[k]);
    }
  }
  //now change the center and make new circles
  for (int i = 0; i < 6; i++) {
    //redefine the center 
    center[0] = orig_coords[i][0];
    center[1] = orig_coords[i][1];
    //from the center, make 6 coords
    float[][] new_coords = position(center[0],center[1],8.0);
    //make 6 particles
    for (int k = 0; k < 6; k++) {
      //if coords do not yet exist, make the circle, else, don't
      boolean x = isItemInArray(all_coords, new_coords[k]);
      if (x == false){
        //create the mover
        // add the mover to the movers list
        movers = (Mover[])append(movers,new Mover(new_coords[k][0],new_coords[k][1],0,0));
        //add coords to the list
        all_coords = (float[][])append(all_coords,new_coords[k]);
      }
    }
    
    
    
  }
}

Mover[] make_betas() {
  // each mouse click, eject an alpha particle
  Mover[] betas = {};
  
  betas = (Mover[])append(betas,new Mover(100.0,100.0,4.0,-0.4));
  betas = (Mover[])append(betas,new Mover(100.0,100.0,4.0,0.4));
  return betas;
}


// create the alpha particle
Mover[] betas = make_betas();
int x = 0;


// create text for positron
float px_loc = 50;
float py_loc = 120;
float px_vel = 4;
float py_vel = -0.4;
String p_message = "Positron";
int p_size = 18;
float[] p_col = {154, 5, 198};
TextBox posi_text = new TextBox(px_loc,py_loc, px_vel, py_vel);

// create text for neutrino
float nx_loc = 50;
float ny_loc = 120;
float nx_vel = 4;
float ny_vel = 0.4;
String n_message = "Neutrino";
int n_size = 18;
float[] n_col = {255, 111, 6};
TextBox neut_text = new TextBox(nx_loc,ny_loc, nx_vel, ny_vel);

void mousePressed() {
  if (x == 0) {
    x = 1;
  } 
}



void draw() {
  background(255);
  //title
  textSize(32);
  fill(0);
  text("Beta Plus Decay", 235, 30);
  
  textSize(24);
  
  if (x == 1) {
    for (int i = 0; i < betas.length; i++) {
      betas[i].update();
      
      betas[i].display(i,8,i);
    }
    
    //draw positron text
    posi_text.update();
    posi_text.display(p_message, p_size, p_col);
    //draw neutrino text
    neut_text.update();
    neut_text.display(n_message,n_size,n_col);
    
    for (int i = 0; i < (movers.length) - 2; i++) {
      movers[i].update();
      movers[i].display(i,16,2);
    }
    //add a neutron
    movers[17].display(3,16,2);
    movers[18].display(3,16,2);
    fill(9, 49, 245);
    text("Protons - 11", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 8", 20, 190);
    
  
  } else {
      for (int i = 0; i < movers.length; i++) {
        movers[i].update();
        //movers[i].checkEdges();
        movers[i].display(i,16,2);
      }
    fill(9, 49, 245);
    text("Protons - 12", 20, 170);
    fill(96, 97, 100);
    text("Neutrons - 7", 20, 190);
  }

}
