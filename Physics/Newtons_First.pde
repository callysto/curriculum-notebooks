

Ball m = new Ball(4);
Star[] star = {};

void setup() {
  size(800,300);
  for (int i = 0; i < 500; i++) {
    float x = random(width);
    float y = random(height);
    star = (Star[])append(star, new Star(0.5,x,y));
  }
}

void drawArrow(float x0, float y0, float x1, float y1) {
  line(x0,y0,x1,y1);
  triangle(x1,y1+2,x1,y1-2,x1+5,y1);
  
}



void draw() {
  background(0);
  for (int i = 0; i < star.length; i++) {
    star[i].display();
  }
  strokeWeight(20);
  stroke(180,92,239);

  PVector wind = new PVector(5,0); //<>// //<>//
  if (mousePressed && mouseX>0 && mouseX<70 && mouseY>height/2-10 && mouseY<height/2+10) {
    m.applyForce(wind); //<>//
    drawArrow(0,height/2,50,height/2);
  }
  text("FORCE",10,155);
  m.update();
  //m.checkEdges();
  m.display();

}


class Ball {
  PVector location;
  PVector velocity;
  PVector acceleration;
  
  float mass;
  
  Ball(float ma) {
    location = new PVector(105, 150);
    velocity = new PVector(0,0);
    acceleration = new PVector(0,0);
    mass = ma;
  }

  void applyForce(PVector force) {
    PVector f = PVector.div(force,mass);
    acceleration.add(f);
  }
    
  
  void update() {
    velocity.add(acceleration);
    location.add(velocity);
    acceleration.mult(0);
    velocity.limit(2);
  }
  
  void display() {
    stroke(0);
    strokeWeight(1);

    fill(199,0,57);
    ellipse(location.x,location.y,mass*16,mass*16);

  }

  void checkEdges() {
    if (location.x > width) {
      location.x = width;
      velocity.x *= 1;

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

class Star {
  float x;
  float y;
  float radius;
  
  Star(float r,float X,float Y) {
    x = X;
    y = Y;
    radius = r;
  }

void display() {
    stroke(255,255,255);
    fill(255,255,255);
    ellipse(x,y,radius,radius);
}

}
