var sequence = [0, 0, 0, 0, 0];

function display() {
	var datas = [{
		id: "LightCoral", lastx: 50, tag: 1
		},{		
		id: "LightBlue", lastx: 150, tag: 2
		}];
		
	var svg = d3.select("#Highlight")
		.append("svg")
		.attr("viewBox", "0 0 600 200");
	
	var group = svg.selectAll('g')
		.data(datas)
		.enter()
		.append("g")
		.attr("transform", "translate(0,0)")
		.call(d3.behavior.drag()
			.on("dragstart", dragstarted)
			.on("drag", dragged)
			.on("dragend", dragended));	
		
	svg.append("image")
		.attr("href", "./images/LittleMissMuffet.png")
		.attr("x", 0)
		.attr("y", 40)
		.attr("width", 400)
		.attr("height", 175);
		
	group.append("rect")
		.attr("width", 60)
		.attr("height", 18)
		.attr("fill", function(d) {return d.id})
		.attr("x", function(d) { return d.lastx})
		.attr("y", 20)
		.style("opacity", 0.5);
		
	function dragstarted(d) {
		d3.select("#result")
			.text("");
	}
		
	function dragged(d) {
		d3.select(this).select("rect")
			.attr("x", d.x = d3.event.x)
			.attr("y", d.y = d3.event.y);
	}
	
	function dragended(d) {
		if (d.x <= 285 && d.x >= 275 && d.y <= 70 && d.y >= 60) {
			highlight(this, d.id, group, 281, 65)
			sequence[0] = d.tag;
		}
		if (d.x <= 235 && d.x >= 225 && d.y <= 95 && d.y >= 85) {
			highlight(this, d.id, group, 231, 91)
			sequence[1] = d.tag;
		}
		if (d.x <= 172 && d.x >= 162 && d.y <= 122 && d.y >= 112) {
			highlight(this, d.id, group, 167, 118)
			sequence[2] = d.tag;
		}
		if (d.x <= 240 && d.x >= 230 && d.y <= 150 && d.y >= 140) {
			highlight(d, d.id, group, 235, 145)
			sequence[3] = d.tag;
		}
		if (d.x <= 295 && d.x >= 285 && d.y <= 180 && d.y >= 170) {
			highlight(this, d.id, group, 292, 175)
			sequence[4] = d.tag;
		}
		
		d3.select(this).select("rect")
			.transition()
			.duration(1000)
			.attr("x", d.x = d.lastx)
			.attr("y", d.y = 20)
	}
	
	function highlight(d, id, group, x, y) {
		group.append("rect")
			.attr("width", 60)
			.attr("height", 18)
			.attr("fill", id)
			.attr("x", x)
			.attr("y", y)
			.style("opacity", 0.5)
			.attr("id", "highlight");
	}	
}

function resetHL() {
		d3.selectAll("#highlight")
			.remove();
		d3.select("#result")
			.text("");
	}
	
function submit() {
    	function arrayEqual (a) {
		b = [0, 1, 2, 2, 1];
		c = [0, 2, 1, 1, 2];
		for (var i = 0; i < a.length; ++i) {
			if (a[i] !== b[i]) {
				for (var i = 0; i < a.length; ++i) {
					if (a[i] !== c[i]) return false;
				}
			}
		}
		return true;
	}
	if (arrayEqual(sequence)){
		d3.select("#result")
			.text("That's right! This poem's pattern is ABCCB");
	}
	else {
		d3.select("#result")
			.text("Not Quite. Look at the words again. Remember not all lines have to rhyme.");
	}
}


