var nt = {
    containers : [],
    register : function(questionsContainer, solutionsContainer, jsonPath, callback, displayExplaination=true) {
        // Check for correct arguments
        if(!d3.select("#"+questionsContainer)[0][0]) {
            console.error("Container with id " + questionsContainer + " does not exist. Please make an id to store the exercises.");
            return;
        }

        if(typeof(questionsContainer) != "string") {
            console.error("questionsContainer must be the name of the container (div) to put the questions in.");
            return;
        }

        if(typeof(solutionsContainer) != "string") {
            console.error("solutionsContainer must be the name of the container (div) to put the solutions in.");
            return;
        }

        if(typeof(jsonPath) != "string") {
            console.error("jsonPath must be the path to where the json data file is located.");
            return;
        }

        if(typeof(callback) != "function") {
            console.error("callback is not a function. Please provide a callback function.");
            return;
        }

        if(questionsContainer in this.containers) {
            console.warn("container with id " + questionsContainer + " is about to overidden. Did you mean to do that?");
        }

        // Get json and make register it to the object associated with the container
        this.getJson(questionsContainer, jsonPath, callback);
        this.containers[questionsContainer] = 
                                            {
                                                "solutions" : solutionsContainer,
                                                "displayExplaination" : displayExplaination 
                                            }
    },
    registerJson : function(questionsContainer, data, callback) {
        this.containers[questionsContainer].json = data;
        callback();
    },
    getJson : function(questionsContainer, jsonPath, callback) {
        d3.json(jsonPath, function(data) {
            nt.registerJson(questionsContainer, data, callback);
        });
    },
    create_exercises : function(containerId) {
        // Check for correct arguments and that the container has been registered.
        if(typeof(containerId) != "string") {
            console.error("containerId must be the id of the question container!");
            return;
        }
    
        if(!(containerId in this.containers)) {
            console.error("You have no registered container with containerId: " + containerId);
            return;
        }
    
        // Multiple Choice questions
        let mcQuestions = [];
        // Select All questions
        let saQuestions = [];
        // Short Answer questions
        let shaQuestions = [];
        // Types
        let types = [];
        // Questions
        let questions = [];

        let data = this.containers[containerId].json;
        let jsonLength = Object.keys(data).length;
        // Get the types of the questions and the questions
        for(let i = 0; i < jsonLength; ++i) {
            types.push(this.determine_type(data[i+1]));
            if(types[i] == "short-answer") {
                shaQuestions.push([])
                shaQuestions[shaQuestions.length-1].push(data[i+1]);
            }
            else if(types[i] == "multiple-choice") {
                mcQuestions.push(data[i+1]);
            }
            else if(types[i] == "select-all") {
                saQuestions.push(data[i+1]);
            }
            
            questions.push([]);
            questions[i].push(data[(i+1).toString()].question);
        }

        let rootContainer = d3.select("#" + containerId);

        // Make a new div for every question there is in the data.
        let questionDivs = rootContainer.selectAll("div")
                                            .data(questions)
                                                .enter()
                                                    .append("div")
                                                        .classed("question-container", true)
                                                        .attr("class", function(d, i) { return d3.select(this).attr("class") + " " + types[i]; });
        // Display all questions by using the arrays in the multidimensional array given to the question divs                                                
        questionDivs.selectAll("p")
                        .data(function(d) { return d; })
                            .enter()
                                .append("p")
                                    .text(function(d, i, j) { return (j+1) + ") " + d; });

        // Separate all the questions into there respectful spots so they can be processed accordingly
        let shortAnswerQuestions = questionDivs.filter(function(d, i) {
            if(this.classList.contains("short-answer"))
                return true;
        });

        let multipleChoiceQuestions = questionDivs.filter(function(d, i) {
            if(this.classList.contains("multiple-choice"))
                return true;
        });

        let selectAllQuestions = questionDivs.filter(function(d, i) {
            if(this.classList.contains("select-all"))
                return true;
        });

        // Start by creating all the short answer questions
        shortAnswerQuestions.data(shaQuestions)
                    .selectAll("input")
                        .data(function(d) { return d; })
                            .enter()
                                .append("input")
                                .attr("type", "text")
                                .style("width", function(d, i) { 
                                    let answerLength = d.answer.toString().length;
                                    if(answerLength >= 0 && answerLength < 10) {
                                        return "20%";
                                    }

                                    else if(answerLength > 10 && answerLength < 30) {
                                        return "30%"
                                    }

                                    else
                                        return "50%";
                                });
        
        // Create multiple choice questions
        let mcIndex = -1;
        let mclabelEnter = multipleChoiceQuestions.data(mcQuestions)
            .selectAll("span")
                .data(function(d, i) { 
                    return d.options; })
                    .enter()
                        .append("span");
        mclabelEnter.append("input")
                        .attr({
                            "type" : "radio",
                            "name" : function(d, i) {
                                if(i == 0)
                                    ++mcIndex; 
                                return "mc-option" + mcIndex; 
                            }
                        });
        mclabelEnter.append("label")
                        .text(function(d, i) { return d; });

        // Create select all questions
        let salabelEnter = selectAllQuestions.data(saQuestions)
        .selectAll("span")
            .data(function(d) { return d.options; })
                .enter()
                    .append("span");
        salabelEnter.append("input")
                        .attr({
                            "type" : "radio",
                            "name" : function(d, i) { return "selectAll-option" + i; } 
                        });
        salabelEnter.append("label")
                        .text(function(d) { return d; });
        

        questionDivs.append("p")
                        .classed("hidden", true)
                        .classed("question-feedback", true);

        // Create the buttons which all the user to submit questions and display the solutins
        let buttonContainer = rootContainer.append("div")
                                                .classed("button-container", true);
        
        buttonContainer.append("input")
                        .attr("type", "button")
                        .attr("value", "Submit Answers")
                        .attr("onclick", "nt.check_exercises(document.getElementById(\""+containerId+"\").id)")
                        .classed("submit-button", true);

        buttonContainer.append("input")
                        .attr("type", "button")
                        .attr("value", "Show Solutions")
                        .attr("onclick", "nt.display_solutions(document.getElementById(\""+containerId+"\").id)")
                        .classed("show-solutions-button", true)
                        .classed("hidden", true);
    },
    check_exercises : function(containerId) {
        if(typeof(containerId) != "string") {
            console.error("containerId must be the id of the question container!");
            return;
        }
    
        let rootContainer = d3.select("#"+containerId);

        let questionDivs = rootContainer.selectAll(".question-container");

        // Short-answer answer compare
        let shortAnswerQuestions = questionDivs.filter(function() {
            if(this.classList.contains("short-answer"))
                return true;
        });

        let shortAnswerFeedback = shortAnswerQuestions.selectAll(".question-feedback");
        shortAnswerQuestions.selectAll("input")
            .filter(function(d, i, j) {
                if(this.value == d.answer) {
                    d3.select(shortAnswerFeedback[j][i]).classed("correct", true)
                                                        .classed("incorrect", false)
                                                        .classed("hidden", false)
                                                        .text("Correct!");
                    return true;
                }

                else {
                    d3.select(shortAnswerFeedback[j][i]).classed("incorrect", true)
                    .classed("correct", false)
                    .classed("hidden", false)
                    .text("Incorrect.");
                }
            });

        // Multiple-choice answer compare
        let multipleChoiceQuestions = questionDivs.filter(function() {
            if(this.classList.contains("multiple-choice")) {
                return true;
            }
        });

        let multipleChoiceFeedback = multipleChoiceQuestions.selectAll(".question-feedback");
        multipleChoiceQuestions.filter(function(d, i, j) {
            let choices = d3.select(this).selectAll("input")[0];
            let answer = -1;

            // Let's get the answer that the user gave.
            for(let i = 0; i < choices.length; ++i) {
                if(choices[i].checked)
                    answer = i;
            }
            if(d.answer == answer) {
                d3.select(multipleChoiceFeedback[i][j]).classed("hidden", false)
                                                        .classed("correct", true)
                                                        .classed("incorrect", false)
                                                        .text("Correct!");
            }
            else {
                d3.select(multipleChoiceFeedback[i][j]).classed("hidden", false)
                                                        .classed("incorrect", true)
                                                        .classed("correct", false)
                                                        .text("Incorrect.");
            }
        })

        // Select all answer compare
        let selectAllQuestions = questionDivs.filter(function() {
            if(this.classList.contains("select-all")) {
                return true;
            }
        });

        let selectAllFeedback = selectAllQuestions.selectAll(".question-feedback");
        selectAllQuestions.filter(function(d, i, j) {
            let choices = d3.select(this).selectAll("input")[0];
            // Right until proven wrong
            let correct = true;
            // Let's get the answers the user gave.
            for(let i = 0; i < choices.length; ++i) {
                if(choices[i].checked) {
                    if(!d.answer.includes(i)) {
                        correct = false;
                        break;
                    }
                }

                else {
                    if(d.answer.includes(i)) {
                        correct = false;
                        break;
                    }
                }
            }
            if(correct) {
                d3.select(selectAllFeedback[i][j]).classed("hidden", false)
                                                        .classed("correct", true)
                                                        .classed("incorrect", false)
                                                        .text("Correct!");
            }
            else {
                d3.select(selectAllFeedback[i][j]).classed("hidden", false)
                                                        .classed("incorrect", true)
                                                        .classed("correct", false)
                                                        .text("Incorrect.");
                
                // Uncheck all buttons
                for(let i = 0; i < choices.length; ++i) {
                    if(choices[i].checked) {
                        choices[i].checked = false;
                    }
                }
            }
        })
    
        // Unhide the show solutions button.
        if(rootContainer.select(".show-solutions-button").classed("hidden"))
            rootContainer.select(".show-solutions-button").classed("hidden", false);
    },
    display_solutions : function(containerId) {
        if(typeof(containerId) != "string") {
            console.log("containerId must be the id of the question container!");
            return;
        }
    
        let solutionsContainer = d3.select("#"+this.containers[containerId].solutions);
        if(!solutionsContainer[0][0]) {
            console.log("Container with that id does not exist: " + containerId + ". Please try again!");
            return;
        }
    
        let answers = [];
        let data = this.containers[containerId].json;
        let jsonLength = Object.keys(data).length;
        for(let i = 0; i < jsonLength; ++i) {
            answers.push([]);
            console.log(data[i+1]);
            if(this.containers[containerId].displayExplaination && data[i+1].explanation != "") {
                answers[i].push((i+1) + ") " + data[i+1].explanation);
                if(this.determine_type(data[i+1]) == "short-answer")
                    answers[i].push(data[i+1].solution);
            }

            else if(this.determine_type(data[i+1]) == "short-answer")
                answers[i].push((i+1) + ") " + data[(i+1).toString()].solution);
        }

        let rootContainer = d3.select("#"+this.containers[containerId].solutions);

        let solutionContainers = rootContainer.selectAll("div")
                                                .data(answers)
                                                    .enter()
                                                        .append("div")
                                                            .classed("solutions-container", true);


        
        solutionContainers.selectAll("p")
                            .data(function(d) { return d; })
                                .enter()
                                    .append("p")
                                        .text(function(d) { return d; })
                                        .style("margin-left", "10px");
    },
    determine_type : function(obj) {
        if(obj.hasOwnProperty("solution")) {
            return "short-answer";
        }

        else if(obj.hasOwnProperty("options")) {
            if(obj.hasOwnProperty("answer")) {
                if(Array.isArray(obj.answer)) {
                    return "select-all";
                }

                else
                    return "multiple-choice";
            }
        }
    }
}