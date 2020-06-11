var items = ["Increased standard of living","Climate change","Production of greenhouse gases","Mining and resource extraction","National economic growth","Increased job availability","Promotion of research in renewable energy"]
var T = []
var C = []
var pos = []
var c = 0
var tx
var ty = 0
var value = 0
var green = []
var red = []
var cbutton
var gc = [0,9,9,9,4,5,6]
var check = 0

function setup() {
    createCanvas(900, 300);
    cbutton = new check(width/2-50,30,60)
    for (var i = 0; i < items.length; i++){
    	tx = 35
    	ty += 40
        green[i] = new choice(tx-25,ty-6.5,0,205,6)
        red[i] = new choice(tx-8.5,ty-6.5,205,0,0)
    	T[i] = new tbox(tx,ty,items[i],50,50,50)
        if (i == gc[i]) {
            var a1 = 0
            var a2 = 205
            var a3 = 6          
        }
        else {
            var a1 = 205
            var a2 = 0
            var a3 = 0
        }
        C[i] = new tbox(tx+450,ty,items[i],a1,a2,a3)
    }
}

function draw() {
	background(255);
    cbutton.display("check")
	for (var j = 0; j < T.length; j++){
		T[j].display();
        red[j].display();
        green[j].display();
        var d1 = dist(mouseX,mouseY,red[j].location.x,red[j].location.y)
        var d2 = dist(mouseX,mouseY,green[j].location.x,green[j].location.y)
        var d3 = dist(mouseX,mouseY,cbutton.location.x,cbutton.location.y)
        if (d1 <= 12 && mouseIsPressed){
            T[j].R = 205
            T[j].G = 0
            T[j].B = 0
        }
        if (d2 <= 12 && mouseIsPressed){
            T[j].R = 0
            T[j].G = 205
            T[j].B = 6
        }
        if (d3 <= cbutton.r && mouseIsPressed) {
            check = 1
        }
        if (check == 1) {
            C[j].display()
        } 
    }
}

function tbox(x,y,item,r,g,b) {
    this.X = x;
    this.Y = y;
    this.string = item
    this.R = r
    this.G = g
    this.B = b

tbox.prototype.display = function() {
    fill(this.R,this.G,this.B);
    noStroke();
    textSize(20)
    textStyle(BOLD)
    textAlign(LEFT)
    text(this.string,this.X,this.Y)
};
};

var choice = function(x,y,r,g,b) {
    this.location = createVector(x,y)
    this.R = r
    this.G = g
    this.B = b
}
choice.prototype.display = function(){
    noStroke();
    fill(this.R,this.G,this.B)
    ellipse(this.location.x,this.location.y,12,12)
}

var check = function(x,y,radius) {
    this.location = createVector(x,y)
    this.r = radius
}
check.prototype.display = function(string1) {
    fill(56,0,169)
    noStroke()
    ellipse(this.location.x,this.location.y,this.r,this.r)
    fill(255)
    textSize(12)
    textStyle(BOLD)
    textAlign(CENTER,CENTER)
    text(string1,this.location.x,this.location.y)
}