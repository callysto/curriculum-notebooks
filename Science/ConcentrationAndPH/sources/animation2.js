function display(pH) {
	var datas = [{
		id: "Red", fade: "./images/RedLitmus2.png", lastx: 450
		},{		
		id: "Blue", fade: "./images/BlueLitmus2.png", lastx: 500
		}];
		
		
	var svg = d3.select("#animation")
		.append("svg")
		.attr("viewBox", "0 0 1000 320");
		
	svg.append("image")
		.attr("href", "./images/Beaker.png")
		.attr("x", 175)
		.attr("y", 20)
		.attr("width", 250)
		.attr("height", 300);
		
	
	svg.append("text")
		.attr("x", 50)
		.attr("y", 20)
		.attr("font-size", "20px")
		.attr("font-family", "serif")
		.text("Untested");
		
	svg.append("text")
		.attr("x", 450)
		.attr("y", 20)
		.attr("font-size", "20px")
		.attr("font-family", "serif")
		.text("Tested");
	
	var group = svg.selectAll('g')
		.data(datas)
		.enter()
		.append("g")
		.attr("transform", "translate(0,0)")
		.call(d3.behavior.drag()
			.on("drag", dragged)
			.on("dragend", dragended));
		
	var defs = svg.append("defs");
		
	defs.selectAll("pattern")
		.data(datas)
		.enter()
		.append("pattern")
		.attr("id", function(d) { return d.id; })
		.attr("height", "100%")
		.attr("width", "100%")
		.attr("patternContentUnits", "objectBoundingBox")
		.append("image")
		.attr("height", 1)
		.attr("width", 1)
		.attr("preserveAspectRatio", "none")
		.attr("href", function(d) { return d.fade; });		
		
	group.append("rect")
		.attr("width", 20)
		.attr("height", 200)
		.attr("fill", function(d) {return d.id})
		.attr("x", function(d,i) { return 50 + i*50 })
		.attr("y", 50);
		
	function dragged(d) {
		d3.select(this).select("rect")
			.attr("x", d.x = d3.event.x)
			.attr("y", d.y = d3.event.y);
	}
	
	function dragended(d) {
		if (d.x <= 375 && d.x >= 200 && d.y <=95 && d.y >= 0) {
			d3.select(this).select("rect")
				.transition()
				.duration(1000)
				.attr("x", d.x = d.lastx)
				.attr("y", d.y = 50);
			if (pH > 7) {
				if (d.id == "Red") {
					d3.select(this).select("rect")
						.transition()
						.delay(1000)
						.duration(1500)
						.style("fill", function(d) {return "url(#" + d.id + ")"});					
				}
			}
			if (pH < 7) {
				if (d.id == "Blue") {
					d3.select(this).select("rect")
						.transition()
						.delay(1000)
						.duration(1500)
						.style("fill", function(d) {return "url(#" + d.id + ")"});
				}
			}
		}
	}
		
	 
}