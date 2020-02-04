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
  
  Mover(float x_loc,float y_loc, float x_vel, float y_vel) {
    location = new PVector(x_loc, y_loc);
    velocity = new PVector(x_vel, y_vel);
  }
  
  void update() {
    location.add(velocity);
  }
}

class Gamma extends Mover {
  Gamma(float x_loc, float y_loc, float x_vel, float y_vel) {
    super(x_loc, y_loc, x_vel, y_vel);
  }

  //creates squiggly lines for a gamma ray
  float[] twoLines(float x_val, float y_val, int i) {
    //upwards gamma
    if (i == 1) {
      // return the coordinates of two perpendicular lines
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val-10 },
        { x_val+3, y_val-10, x_val+15, y_val-12 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = { coords[1][2], coords[1][3] };
      return end;
    } else {
      float[][] coords = {
        { x_val, y_val, x_val+3, y_val+10 },
        { x_val+3, y_val+10, x_val+15, y_val+8 }
      };

      line(coords[0][0], coords[0][1], coords[0][2], coords[0][3]);
      line(coords[1][0], coords[1][1], coords[1][2], coords[1][3]);

      float[] end = {coords[1][2], coords[1][3]};
      return end;
    }
  }

  void drawArrow(float cx, float cy, int len, float angle) {
    pushMatrix();
    translate(cx, cy);
    rotate(radians(angle));
    line(0, 0, len, 0);
    line(len, 0, len-8, -8);
    line(len, 0, len-8, 8);
    popMatrix();
  }
  
  void display(int i, int angle) {
    stroke(255, 0, 0);
    float[] x = twoLines(location.x, location.y, i);
    float[] y = twoLines(x[0], x[1], i);
    float[] z = twoLines(y[0], y[1], i);
    drawArrow(z[0], z[1], 10, angle);
  }
}

float[][] position(float x_val, float y_val, float radius) {
  // make it produce the x and y coordinates for the 6 spots around it
  float y_dist = sin(radians(30)) * 2 * radius;
  float x_dist = cos(radians(30)) * 2 * radius;
  
  //coords is a list that contains the new coordinates for 6 circles around one circle
  float[][] coords = {
    { x_val, y_val-(2*radius) },
    { x_val+x_dist, y_val-y_dist },
    { x_val+x_dist, y_val+y_dist },
    { x_val, y_val+(2*radius) },
    { x_val-x_dist, y_val+y_dist },
    { x_val-x_dist, y_val-y_dist }
  };
  
  return coords;
}

boolean isItemInArray(float[][] array, float[] item) {
    for (int i = 0; i < array.length; i++) {
        // This if statement depends on the format of your array
        if (array[i][0] == item[0] && array[i][1] == item[1]) {
            return true;   // Found it
        }
    }
    return false;   // Not found
}
