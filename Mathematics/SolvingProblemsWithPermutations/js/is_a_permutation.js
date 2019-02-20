function isAPermutation() {
    var answerKey = {    
                        "0": 1,
                        "1": 0,
                        "2": 0,
                        "3": 1,
                    };
    
    var feedback = [ 
                            [ 
                "1. Incorrect. It matters which order you put you passcode in. Take the passcode 1234. If you put 4321, does it open your phone?",
        "2. Incorrect. Let's take John, Sue, Mary, Philip, and James as the people we choose to go to dinner with. It doesn't matter the order we call them in, we are still going to go to dinner with the same people.",
        "3. Incorrect. Let's take cranberries, apples, mango, and strawberries as the fruits we want to put in our salad. It doesn't matter what order we put them in our salad, it will still end up being the same salad.",
        "4. Incorrect. It matters what order the cars are in line because it is a queue. It should be first come first serve. Therefore, if you go to the drivethru before someone else, you should get your items first."
                            ],
                            [
        "1. Correct. Typing in 1234 is different than putting in 4321.",
        "2. Correct. It doesn't matter the order in which you choose which friends to go to dinner with you.",
        "3. Correct. It doesn't matter the order you put cranberries, apples, mangos, and strawberries into your salad.",
        "4. Correct. A Tim Horton's drive thru is a queue. If you order first, you should get your items before anyone behind you."
                            ]
                    ];
    var answeredIndexes = [];
    d3.selectAll(".booleanInput").filter(function(d,i) {
           if(this.checked && answerKey[i.toString()] == 1)
               answeredIndexes.push(1);
           else if(this.checked && answerKey[i.toString()] == 0)
               answeredIndexes.push(0);
           else if(!this.checked && answerKey[i.toString()] == 0)
               answeredIndexes.push(1);
           else
               answeredIndexes.push(0);
    });
    
    var data = [];
    for(var i = 0; i < answeredIndexes.length; ++i) {
         data.push(feedback[answeredIndexes[i]][i]);
    }
    
    var feedbackContainer = d3.select("#is-permutation-feedback-container")
    .style("display", "block")
    .selectAll("p")
        .data(data)
            .enter()
                .append("p")
                    .text(function(d, i) {
                        return d;
                    });
    
    d3.select("#is-permutation-feedback-container")
    .style("display", "block")
    .selectAll("p")
        .data(data)
             .text(function(d, i) {
                  return d;
              });
}
