var data3D = [ [[0,-1,0],[-1,1,0],[1,1,0]] ];

var triangles3D = d3._3d()
    .scale(100)
    .origin([480, 250])
    .shape('TRIANGLE');

var projectedData = triangles3D(data3D);

init(projectedData);

function init(data){

    var triangles = svg.selectAll('path').data(data);

    // add your logic here...

}