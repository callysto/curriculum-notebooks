/* removed the class block and any import statements */
				
// create an array of ball objects
Ball [] theBalls = new Ball[100];

// keep track of how many balls we have already created
int maxBalls = 1000;
int numBalls = 0;
int currentBall = 0;

void setup() 
{
	// general setup
	size (500,500);
	smooth();
}

void draw() 
{
	// clear background
	background(255);
	
	// if the user clicks we should create a ball
	if (mousePressed)
	{
		// create a ball at this position
		theBalls[ currentBall ] = new Ball(this, mouseX, mouseY);
		
		// increase to keep track of the next ball
		currentBall++;
		
		// also increase our total balls used, if necessary
		if (numBalls < theBalls.length)
		{
			numBalls++;
		}
		
		// did we just use our last slot? if so, we can reuse old slots
		if (currentBall >= theBalls.length)
		{
			currentBall = 0;
		}
	}
	
	// move and draw all balls that have been created
	for (int i = 0; i < numBalls; i++)
	{
		theBalls[i].fade();
		theBalls[i].move();
		theBalls[i].display();
	}
}


/* paste additional classes here.  remove the "public" declaration from the class definition and any import statements */

class Ball
{
	// instance vars
	private float x;
	private float y;
	private float size;
	private float myRed;
	private float myGreen;
	private float myBlue;
	private float myAlpha;
	private float speedX;
	private float speedY;
	
	// store a reference to the canvas
	private PApplet canvas;
	
	Ball(PApplet canvas, float x, float y)
	{
		// store a ref to the canvas
		this.canvas = canvas;
	
		// store x and y
		this.x = x;
		this.y = y;
		
		// randomize our size
		size = this.canvas.random(15,35);
		
		// randomize our color
		myRed = this.canvas.random(0,255);
		myGreen = this.canvas.random(0,255);
		myBlue = this.canvas.random(0,255);
		myAlpha = this.canvas.random(0,255);
		
		// randomize our speed
		speedX = this.canvas.random(-5, 5);
		speedY = this.canvas.random(-5, 5);
	}
	
	// move our ball
	void move()
	{
		// update position based on speed
		x += speedX;
		y += speedY;
		
		// bounce
		if (x > width)
		{
			x = width;
			speedX *= -1;
		}
		if (y > height)
		{
			y = height;
			speedY *= -1;
		}
		if (x < 0)
		{
			x = 0;
			speedX *= -1;
		}
		if (y < 0)
		{
			y = 0;
			speedY *= -1;
		}
	}
	
	// display our ball
	void display()
	{
		// use our reference to the canvas to draw our ball
		this.canvas.noStroke();
		this.canvas.fill(myRed, myGreen, myBlue, myAlpha);
		this.canvas.ellipse(x,  y,  size,  size);
	}
	
	// fade method - allows a ball to fade out of existence
	void fade()
	{
		if (myAlpha > 0)
		{
			myAlpha -= 3;
		}
		else
		{
			myAlpha = 0;
		}
	}
	
}