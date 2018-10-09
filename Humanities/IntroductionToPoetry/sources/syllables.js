function display(question) {
	var data1 = [{
		original: "There", hyphen: "There", xvar: 0, move: 0
		},{		
		original: "is", hyphen: "is", xvar: 55, move: 0
		},{
		original: "an", hyphen: "an", xvar: 73, move: 0
		},{		
		original: "elephant", hyphen: "e-le-phant", xvar: 98, move: 3
		},{		
		original: "in", hyphen: "in", xvar: 180, move: 0
		},{	
		original: "my", hyphen: "my", xvar: 200, move: 0
		},{		
		original: "closet.", hyphen: "clo-set.", xvar: 230, move: 0
		}];
		
	var data2 = [{
		original: "All", hyphen: "All", xvar: 0, move: 0
		},{		
		original: "hippos", hyphen: "hip-pos", xvar: 27, move: 3
		},{
		original: "go", hyphen: "go", xvar: 90, move: 0
		},{		
		original: "swimming", hyphen: "swim-ming", xvar: 115, move: 2
		},{		
		original: "in", hyphen: "in", xvar: 206, move: 0
		},{	
		original: "the", hyphen: "the", xvar: 226, move: 0
		},{		
		original: "summer.", hyphen: "sum-mer.", xvar: 258, move: 0
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
		.attr("font-size", "20px")
		.text(function(d) {return d.original})
		.on("mouseover", handleMouseOver)
		.on("mouseout", handleMouseOut);
	
	function handleMouseOver(d, i) {
		d3.select(this).text(function(d) {return d.hyphen})
			.attr("x", function (d,i) { return d.xvar - d.move })
			.attr("font-size", "18px")
			.attr("fill", "red");
			//.attr("style", "backgroundColor: powderblue");
	}
	
	function handleMouseOut(d, i) {
		d3.select(this).text(function(d) {return d.original})
			.attr("x", function (d,i) { return d.xvar})
			.attr("font-size", "20px")
			.attr("fill", "black");
	}
}