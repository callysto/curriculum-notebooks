function display2(pH) {
	var datas = [{
		id: "Red", image: "./images/dropper2.png", lastx: 450
		}];
		
	var svg = d3.select("#beaker")
		.append("svg")
		.attr("viewBox", "0 0 1000 500");
		
	var slider = d3.select("#slider")
		.append("input")
		.attr("type", "range")
		.attr("min", "0")
		.attr("max", "14")
		.attr("value", "7")
		.attr("class", "slider")
		.attr("id", "pHslider");
		
	d3.select("#slider")
		.append("p")
		.text("pH: ")
		.append("span")
		.attr("id", "output");
		
	var defs = svg.append("defs");
		
	defs.selectAll("pattern")
		.data(datas)
		.enter()
		.append("pattern")
		.attr("id", "dropper")
		.attr("height", "100%")
		.attr("width", "100%")
		.attr("patternContentUnits", "objectBoundingBox")
		.append("image")
		.attr("height", 1)
		.attr("width", 1)
		.attr("preserveAspectRatio", "none")
		.attr("href", "./images/dropper2.png");
		
	svg.append("image")
		.attr("href", "./images/BeakerEmpty.png")
		.attr("x", 175)
		.attr("y", 100)
		.attr("width", 250)
		.attr("height", 300);
		
	svg.append("rect")
		.attr("x", 197)
		.attr("y", 230)
		.attr("width", 200)
		.attr("height", 150)
		.attr("rx", 5)
		.attr("ry", 5)
		.attr("fill", "LightSteelBlue")
		.attr("id", "Liquid")
	
	var group = svg.selectAll('g')
		.data(datas)
		.enter()
		.append("g")
		.attr("transform", "translate(0,0)")
		.call(d3.behavior.drag()
			.on("drag", dragged)
			.on("dragend", dragended));		
		
	group.append("rect")
		.attr("width", 80)
		.attr("height", 200)
		.attr("fill", "url(#dropper)")
		.attr("x", 50)
		.attr("y", 50)
		.attr("id", "Dropper");
		
	function dragged(d) {
		d3.select(this).select("rect")
			.attr("x", d.x = d3.event.x)
			.attr("y", d.y = d3.event.y);
	}
	
	function dragended(d) {
		if (d.x <= 335 && d.x >= 174 && d.y <=40) {
			d3.select(this).select("rect")
				.transition()
				.duration(1000)
				.attr("x", d.x = d.lastx)
				.attr("y", d.y = 50)
			d3.select("#Liquid")
				.transition()
				.delay(1000)
				.duration(3000)
				.style("fill", function(data3) {
						if (pH <= 4.4) {return "DarkRed";}
						if (pH > 4.4 && pH <= 5.4) {return "DarkOrange";}
						if (pH > 5.4 && pH <= 6.4) {return "Yellow";}
						if (pH > 6.4 && pH <= 7.4) {return "LimeGreen";}
						if (pH > 7.4 && pH <= 8.4) {return "DarkGreen";}
						if (pH > 8.4 && pH <= 9.4) {return "MediumBlue";}
						if (pH > 9.4) {return "Indigo";}
					});
		}
	}
	
	sliderin = document.getElementById("pHslider");
	output = document.getElementById("output");
	
	output.innerHTML = sliderin.value;
	sliderin.oninput = function() {
		output.innerHTML = this.value;
		pH = this.value;
	}
}

function reset_liquid(){
	d3.select("#Liquid")
		.style("fill", "LightSteelBlue");
}

