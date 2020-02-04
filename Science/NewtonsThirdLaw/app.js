/* global d3 */
var svg=d3.select("body")
    .append("svg")
    .style("width","100%");

var nodes = d3.range(20).map(function(d,i) {
  var radius = Math.random()*10+5 + (i<0 ? 55 : 0),
      x=Math.random()*300+radius,
      y=Math.random()*300+radius;
  return {radius:radius,mass:radius**2,x:x,y:y,px:x+Math.random()*2,py:y+Math.random()*2};
});

var ball = svg.selectAll(".ball")
  .data(nodes)
  .enter()
    .append("circle")
    .attr("class","ball")
    .attr("r",function(d) { return d.radius; });

function redraw() {
  ball.attr("cx",function(d) { return d.x; });
  ball.attr("cy",function(d) { return d.y; });
  force.resume();
}
   
var force = d3.layout.force()
    .friction(1)
    .nodes(nodes)
    .charge(0).gravity(0)
    .on("tick.redraw",redraw)
    .start();

ball.call(force.drag);
d3.z.collide(force);


function setBoundary() {
  var w = svg.node().offsetWidth,
      h = (window.innerHeight || document.documentElement.clientHeight || document.body.clientHeight)-20;
  svg.attr("height",h);
  svg.attr("width",w);
  d3.z.deflect(force,0,0,h,h);
}
setBoundary();
window.onresize = setBoundary;