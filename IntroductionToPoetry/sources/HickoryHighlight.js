var sequence = [0, 0, 0, 0, 0];

function display1() {
	var timeout;
	var datas = [{
		id: "LightCoral", lastx: 50, tag: 1
		},{		
		id: "LightBlue", lastx: 150, tag: 2
		}];
		
	var svg = d3.select("#Highlight1")
		.append("svg")
		.attr("viewBox", "0 0 650 225");
		
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
		.attr("href", "./images/Hickory.png")
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
		if (d.x <= 225 && d.x >= 215 && d.y <= 55 && d.y >= 45) {
			highlight(this, d.id, group, 219, 48)
			sequence[0] = d.tag;
		}
		if (d.x <= 285 && d.x >= 275 && d.y <= 85 && d.y >= 75) {
			highlight(this, d.id, group, 280, 80)
			sequence[1] = d.tag;
		}
		if (d.x <= 220 && d.x >= 210 && d.y <= 120 && d.y >= 110) {
			highlight(this, d.id, group, 215, 115)
			sequence[2] = d.tag;
		}
		if (d.x <= 212 && d.x >= 202 && d.y <= 150 && d.y >= 140) {
			highlight(d, d.id, group, 207, 145)
			sequence[3] = d.tag;
		}
		if (d.x <= 225 && d.x >= 215 && d.y <= 185 && d.y >= 175) {
			highlight(this, d.id, group, 219, 180)
			sequence[4] = d.tag;
		}
		
		d3.select(this).select("rect")
			.transition()
			.duration(1000)
			.attr("x", d.x = d.lastx)
			.attr("y", d.y = 20);
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

function resetHL1() {
		d3.selectAll("#highlight")
			.remove();
		d3.select("#result")
			.text("");
	}
	
function submit1() {
	function arrayEqual (a) {
		b = [1, 1, 2, 2, 1];
		c = [2, 2, 1, 1, 2];
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
			.text("That's right! This poem's pattern is AABBA")
		console.log(sequence);
	}
	else {
		d3.select("#result")
			.text("Not Quite. Look at the words again. It's about sound and not spelling.")
		console.log(sequence)
		console.log([0, 2, 1, 1, 2]);
	}
}


