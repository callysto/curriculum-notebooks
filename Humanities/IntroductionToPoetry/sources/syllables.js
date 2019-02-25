requirejs.config({
    paths: { 
        'd3': 'https://d3js.org/d3.v3.min', 
    },                                       
});


function display(question) {
    require(['d3'], function(d3) { 
        var data1 = [{
            original: "There", hyphen: "There", xvar: 0
            },{		
            original: "is", hyphen: "is", xvar: 55
            },{
            original: "an", hyphen: "an", xvar: 73
            },{		
            original: "elephant", hyphen: "e-le-phant", xvar: 98
            },{		
            original: "in", hyphen: "in", xvar: 180
            },{
            original: "my", hyphen: "my", xvar: 200
            },{		
            original: "closet.", hyphen: "clo-set.", xvar: 230
            }];

        var data2 = [{
            original: "All", hyphen: "All", xvar: 0
            },{		
            original: "hippos", hyphen: "hip-pos", xvar: 27
            },{
            original: "go", hyphen: "go", xvar: 90
            },{		
            original: "swimming", hyphen: "swim-ming", xvar: 115
            },{		
            original: "in", hyphen: "in", xvar: 206
            },{	
            original: "the", hyphen: "the", xvar: 226
            },{		
            original: "summer.", hyphen: "sum-mer.", xvar: 258
            }];

        if (question == 1) {
            var datas = data1
            console.log(question);
        } 
        if (question == 2) {
            var datas = data2
            console.log(question);
        }

        var svg = d3.select("#sentence"+question)
            .append("svg")
            .attr("viewBox", "0 0 350 30");

        //	<text x="20" y="20" font-family="sans-serif" font-size="20px" fill="red">Hello!</text>

        /*svg.append("text")
            .attr("x", 50)
            .attr("y", 20)
            .attr("font-size", "20px")
            .attr("font-family", "serif")
            .text("Untested");*/

        var group = svg.selectAll('text')
            .data(datas)
            .enter()
            .append("text")
            .attr("x", function(d,i) { return d.xvar})
            .attr("y", 20)
            .attr("font-size", "19px")
            .text(function(d) {return d.original})
            .on("mouseover", handleMouseOver)
            .on("mouseout", handleMouseOut);

        function handleMouseOver(d, i) {
            d3.select(this).text(function(d) {return d.hyphen})
                //.attr("x", function (d,i) { return d.xvar })
                .attr("font-size", "17px")
                .attr("fill", "red");
                //.attr("style", "backgroundColor: powderblue");
        }

        function handleMouseOut(d, i) {
            d3.select(this).text(function(d) {return d.original})
                .attr("x", function (d,i) { return d.xvar})
                .attr("font-size", "19px")
                .attr("fill", "black");
        }
    })
    }