function check_binomial_answers() {
    let answers = [];
    d3.json("data/binomial-coefficient-answers.json", function(data) {
        let jsonKeyLength = Object.keys(data).length;
        for(let i = 0; i < jsonKeyLength; ++i) {
            answers.push(data[(i+1).toString()]);
        }
        
        let correctIndexes = [];
        let correctAnswers = d3.select("#binomial-co-questions-container").selectAll("input[type=text]")
            .filter(function(d, i) {
                if(this.value == answers[i]) {
                    correctIndexes.push(i);
                    return true;   
                }
            });
        console.log(correctIndexes);
        d3.selectAll(".binomial-co-question-feedback")
                    .filter(function(d, i) {
                          if(correctIndexes.includes(i)) {
                              correctIndex = correctIndexes.indexOf(i);
                              correctAnswers[0][correctIndex].style.display = "none";
                              return true;
                          }
                     })
                     .classed("correct", true)
                     .classed("incorrect", false)
                     .classed("hidden", false)
                     .classed("rendered_html", false)
                     .text("Correct!");
        
        let numerator = "?"
        let denominator = "?"
        let answer = "?"
        let numberOfCorrectAnswers = 0;
        
        let question = d3.select("#binomial-co-question").text().slice(44);
        if(question.includes("49!") || correctIndexes.includes(0)) {
            numerator = "49!";
            numberOfCorrectAnswers++;
        }
        
        if(question.includes("6!43!") || correctIndexes.includes(1)) {
            denominator = "6!43!";
            numberOfCorrectAnswers++;
        }
        
        if(question.includes("13983816") || correctIndexes.includes(2)) {
            answer = "13983816";
            numberOfCorrectAnswers++;
        }
        
        d3.select("#binomial-co-question").text("$_nC_r = _{49}C_6 = \\frac{"+numerator+"}{"+denominator+"} = "+answer+"$");
        if(numberOfCorrectAnswers == 3) {
            d3.select("#binomial-coeffient-content-container").classed("hidden", false);
        }
        MathJax.Hub.Queue(["Typeset",MathJax.Hub]);
    });
}

function check_probability_answer() {
   let input = d3.select("#probability-answer");
   let answer = input.property("value");
   let feedback = d3.select("#probability-feedback")
   if(answer == "10.22%") {
       feedback.classed("correct", true)
               .classed("incorrect", false)
               .classed("hidden", false)
               .text("Correct!");
       
       input.classed("hidden", true);
   }
   else {
      input.transition()
           .duration(500)
           .style("background-color", "red")
           .each("end", function() { 
              input.transition()
                  .duration(500)
                  .style("background-color", "white");
           });
   }
}