
//Mover m;
void setup() {
  size(640,360);
  m = new Mover();

}

static PVector rotate(float theta, float x,float y,float p, float q) {
  PVector C = new PVector (0,0);
  float x_new = cos(theta)*(x-p) - sin(theta)*(y-q) + p;
  float y_new = sin(theta)*(x-p) + cos(theta)*(y-q) + q;
  C.x = x_new;
  C.y = y_new;
  return C;
}


void draw() {
  background(255);
  PVector wind = new PVector(0.04,-0.04);
  
  float theta = 0;
  
  if (wind.y == 0) {
    theta = 1.0*atan(wind.x/(wind.y+1e-6));
  }
  else if (wind.x == 0 && wind.y > 0) {
    theta = 1.0*atan(wind.x/(wind.y+1e-6)) - 4*atan(1.0);
  }
  else if (wind.x < 0 && wind.y < 0 || wind.x == 0) {
    theta = -1.0*atan(wind.x/(wind.y+1e-6));
  }
  else if (wind.x < 0 && wind.y > 0) {
    theta = 1.0*atan(wind.x/(wind.y+1e-6)) - 2*atan(1.0);
  }
  else {
    theta = 1.0*atan(wind.x/(wind.y+1e-6)) + 2*atan(1.0);
  }
  
  
  PVector gravity = new PVector(0,0.03*m.mass);
  PVector C1 = m.location;
  float b = 8;
  float c = 15;
  float h = sqrt(pow(c,2)-pow(b,2));
  
  if (mousePressed) {
    
    m.applyForce(wind);
    stroke(0);
    strokeWeight(3.5);
    float endpoint_x = C1.x + wind.x*2000;
    float endpoint_y = C1.y + wind.y*2000;
    PVector rot_vert1 = rotate(theta,endpoint_x+b,endpoint_y+h,endpoint_x,endpoint_y);
    PVector rot_vert2 = rotate(theta,endpoint_x-b,endpoint_y+h,endpoint_x,endpoint_y);    
    line(C1.x,C1.y,endpoint_x,endpoint_y);
    strokeWeight(0.5);
    fill(0);
    triangle(endpoint_x,endpoint_y,rot_vert1.x,rot_vert1.y,rot_vert2.x,rot_vert2.y);
    
  }
  
  m.applyForce(gravity);
    
  m.update();
  m.checkEdges();
  m.display();

}


class Mover {
  PVector location;
  PVector velocity;
  PVector acceleration;
  
  float mass;
  
  Mover() {
    location = new PVector(width/2, height/2);
    velocity = new PVector(0,0);
    acceleration = new PVector(0,0);
    mass = 2;
  }
  
  void applyForce(PVector force) {
    PVector f = PVector.div(force,mass);
    acceleration.add(f);
  }
    
  
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    acceleration.mult(0);
  }
  
  void display() {
    stroke(0);
    strokeWeight(1);

    fill(100,218,99);
    ellipse(location.x,location.y,mass*16,mass*16);

  }
  
  void checkEdges() {
    if (location.x > width) {
      location.x = width;
      velocity.x *= -1;
    } else if (location.x < 0) {
      velocity.x *= -1;
      location.x = 0;
    }
    
    if (location.y > height) {
      velocity.y *= -1;
      location.y = height;
    }
    if (location.y < 0) {
      velocity.y *= -1;
      location.y = 0;
    }
  }
}
