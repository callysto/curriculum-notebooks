/* global d3 */

/*
Newtonian collision checking  (draft)
based on the paper: http://www.vobarian.com/collisions/2dcollisions2.pdf
ziggy.jonsson.nyc@gmail.com
*/

if (typeof d3.z != "object") d3.z = {};

(function() {

// Initiates fully elastic collision 

  d3.z.collide = function(force) {
    force.on("tick.collide", function() {
      var candidates = force.nodes().filter(function(d) { return d.radius && (d.mass > 0 || d.fixed);}),  // Fixed nodes are always candidates
          q = d3.geom.quadtree(candidates),
          i = 0,
          n = candidates.length,
          node;
                   
      while (++i < n) {
        node = candidates[i];
        if (node.mass >0) q.visit(d3.z.check_collision(node));
      }
    });
  };

  d3.z.deflect = function(force,x1,y1,x2,y2) {
    force.on("tick.deflect", function() {
      var nodes = force.nodes(),n=nodes.length,i=0;
      
      while(++i<n) {
        var node = nodes[i],radius = node.radius || 0,newpos,speed;
        if ( (node.x-radius < x1 && ((newpos = x1+radius) || true))   ||  (node.x+radius > x2 && ((newpos = x2-radius) || true))) {
          speed = node.x - node.px;
          node.x = newpos;
          node.px = newpos + speed;
        }
        if ( (node.y-radius < y1 && ((newpos = y1+radius) || true))   ||  (node.y+radius > y2 && ((newpos = y2-radius) || true))) {
          speed = node.y - node.py;
          node.y = newpos;
          node.py = newpos + speed;
        }
      }
    });
  };

  var Vector = function(x,y) {
    this.x = x;
    this.y = y;
  };

  Vector.prototype.add = function(d) {
    return (typeof d == "object") ? new Vector(this.x+d.x,this.y+d.y) : new Vector(this.x+d,this.y+d);
  };

  Vector.prototype.subtract = function(d) {
    return (typeof d == "object") ? new Vector(this.x-d.x,this.y-d.y) : new Vector(this.x-d,this.y-d);
  };

  Vector.prototype.mult = function(d)  {
    return (typeof d == "object") ? new Vector(this.x*d.x,this.y*d.y) : new Vector(this.x*d,this.y*d);
  };
  
  Vector.prototype.dot = function(d)  {
    return (typeof d == "object") ? this.x*d.x+this.y*d.y : this.x*d+this.y*d;
  };
  
  Vector.prototype.length = function() {
    return Math.sqrt(this.dot(this));
  };
  
  Vector.prototype.norm = function() {
    var length = this.length();
    return new Vector(this.x/length,this.y/length);
  };
  
  Vector.prototype.tangent = function() {
    return new Vector(this.y,-this.x);
  };
  
  Vector.prototype.change = function(d,x,y) {
    d[x ? x : "x"] = this.x;
    d[y ? y : "y"] = this.y;
  };


  d3.z.check_collision = function(node) {
    var radius = node.radius,
        nx1 = node.x - radius,
        nx2 = node.x + radius,
        ny1 = node.y - radius,
        ny2 = node.y + radius;
  
    return function(quad, x1, y1, x2, y2) {
      if (quad.point && (quad.point !== node)) {
        var b1 = node,
            b2 = quad.point,
            r = b1.radius+b2.radius,
            _p1 = new Vector(b1.x,b1.y),
            _p2 = new Vector(b2.x,b2.y),
            _n = _p2.subtract(_p1),
            l = _n.length();
        
        if (l < r) {
          var m1 = b1.fixed ? 1e99 : b1.mass,
              m2 = b2.fixed ? 1e99 : b2.mass,
              totalmass = m1+m2,
               mT = _n.norm().mult(r-l),
         
              _v1 = new Vector(b1.x-b1.px,b1.y-b1.py),
              _v2 = new Vector(b2.x-b2.px,b2.y-b2.py),
                  
              _un = _n.norm(),
              _ut = new Vector(-_un.y,_un.x),
              
              v1n = _un.dot(_v1),
              v1t = _ut.dot(_v1),
              
              v2n = _un.dot(_v2),
              v2t = _ut.dot(_v2),
              
              
              V1n = (v1n * (m1-m2) + 2*m2 * v2n ) / (totalmass),
              V2n = (v2n * (m2-m1) + 2*m1 * v1n ) / (totalmass),
              
              _V1 = _un.mult(V1n).add(_ut.mult(v1t)),
              _V2 = _un.mult(V2n).add(_ut.mult(v2t));
          
          _p1 = _p1.subtract(mT.mult(m2/totalmass));
          _p2 = _p2.add(mT.mult(m1/totalmass));
      
          b1.x = _p1.x;
          b1.y = _p1.y;
          b2.x = _p2.x;
          b2.y = _p2.y;
          
          b1.px = b1.x - _V1.x;
          b1.py = b1.y - _V1.y;
          b2.px = b2.x - _V2.x;
          b2.py = b2.y - _V2.y;
        }
      }
      return  x1 > nx2 ||
        x2 < nx1 ||
        y1 > ny2 ||
        y2 < ny1;
    };
  };
})();