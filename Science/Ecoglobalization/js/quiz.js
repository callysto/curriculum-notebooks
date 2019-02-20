function calculate_quiz() {
    d3.json("data/answers.json", function(data) {
        // WATER USES
        let waterSelectQuestions = d3.select("#water-use-questions-container")
                                    .selectAll("select");
        
        let waterScore = 0;
        let waterSelects = data["Water Uses"]["select"];
        for(let i = 0; i < waterSelectQuestions[0].length; ++i) {
            let answer = waterSelectQuestions[0][i].selectedIndex;
            waterScore += waterSelects[i][answer];
        }

        let waterCheckboxQuestions = d3.select("#water-use-questions-container")
                                    .selectAll("input[type=checkbox]");
    
        let waterCheckboxes = data["Water Uses"].checkbox;

        for(let i = 0; i < waterCheckboxQuestions[0].length; ++i) {
            let checked = waterCheckboxQuestions[0][i].checked;
            if(checked)
                waterScore += waterCheckboxes[i];
        }

        d3.select("#water-score").classed("hidden", false)
        d3.selectAll(".water-score-value").text(function() { return waterScore; });

        // FOOD
        let foodInputQuestions = d3.select("#food-use-question-container")
                                        .selectAll("input[type=text]");

        let foodScore = 0;
        let foodModifiers = data["Food"].modifiers;
        
        for(let i = 0; i < foodInputQuestions[0].length; ++i) {
            let input = Number(foodInputQuestions[0][i].value);
            foodScore += input * foodModifiers[i];
        }

        let foodSelectQuestions = d3.select("#food-use-question-container")
                                        .selectAll("select");
        
        let foodSelects = data["Food"].select;
        for(let i = 0; i < foodSelectQuestions[0].length; ++i) {
            let answer = foodSelectQuestions[0][i].selectedIndex;
            foodScore += foodSelects[i][answer];
        }

        d3.select("#food-score").classed("hidden", false)
        d3.selectAll(".food-score-value").text(function() { return foodScore; });

        // TRANSPORTATION
        let transportationScore = Number(d3.select("#transportation-use-question-container")
                                        .select("input")[0][0].value);

        let transportationSelectQuestions = d3.select("#transportation-use-question-container")
                                                .selectAll("select");

        let transportationSelects = data["Transportation"].select;
        for(let i = 0; i < transportationSelectQuestions[0].length; ++i) {
            let answer = transportationSelectQuestions[0][i].selectedIndex;
            transportationScore += transportationSelects[i][answer];
        }

        d3.select("#transportation-score").classed("hidden", false)
        d3.selectAll(".transportation-score-value").text(function() { return transportationScore; });

        // SHELTER
        let shelterSelectQuestions = d3.select("#shelter-use-question-container")
                                        .selectAll("select");

        let shelterSelects = data["Shelter"].select;
        let shelterScore = 0;

        for(let i = 0; i < shelterSelectQuestions[0].length; ++i) {
            let answer = shelterSelectQuestions[0][i].selectedIndex;
            shelterScore += shelterSelects[i][answer];
        }

        let shelterCheckboxQuestions = d3.select("#shelter-use-question-container")
                                            .select("input[type=checkbox]");

        let shelterCheckboxes = data["Shelter"].checkbox;

        for(let i = 0; i < shelterCheckboxQuestions[0].length; ++i) {
            let checked = shelterCheckboxQuestions[0][i].checked;
            if(checked)
                shelterScore += shelterCheckboxes[i];
        }

        d3.select("#shelter-score").classed("hidden", false)
        d3.selectAll(".shelter-score-value").text(function() { return shelterScore; });

        // ENERGY USE
        let energySelectQuestions = d3.select("#energy-use-question-container")
                                        .selectAll("select");

        let energySelects = data["Energy Use"].select;
        let energyScore = 0;
        for(let i = 0; i < energySelectQuestions[0].length; ++i) {
            let answer = energySelectQuestions[0][i].selectedIndex;
            energyScore += energySelects[i][answer];
        }

        d3.select("#energy-score").classed("hidden", false)
        d3.selectAll(".energy-score-value").text(function() { return energyScore; });

        // CLOTHING
        let clothingSelectQuestions = d3.select("#clothing-use-question-container")
                                            .selectAll("select");
        
        let clothingSelects = data["Clothing"].select;
        let clothingScore = 0;
        for(let i = 0; i < clothingSelectQuestions[0].length; ++i) {
            let answer = clothingSelectQuestions[0][i].selectedIndex;
            clothingScore += clothingSelects[i][answer];
        }

        let clothingCheckboxQuestions = d3.select("#clothing-use-question-container")
                                            .selectAll("input[type=checkbox");

        let clothingCheckboxes = data["Clothing"].checkbox;
        for(let i = 0; i < clothingCheckboxQuestions[0].length; ++i) {
            let checked = clothingCheckboxQuestions[0][i].checked;
            if(checked)
                clothingScore += clothingCheckboxes[i];
        }

        d3.select("#clothing-score").classed("hidden", false)
        d3.selectAll(".clothing-score-value").text(function() { return clothingScore; });

        // STUFF
        let stuffSelectQuestions = d3.select("#stuff-use-question-container")
                                        .selectAll("select");

        let stuffSelects = data["Stuff"].select;
        let stuffScore = 0;
        for(let i = 0; i < stuffSelectQuestions[0].length; ++i) {
            let answer = stuffSelectQuestions[0][i].selectedIndex;
            stuffScore += stuffSelects[i][answer];
        }

        let stuffCheckboxQuestions = d3.select("#stuff-use-question-container")
                                            .selectAll("input[type=checkbox]");

        let stuffCheckboxes = data["Stuff"].checkbox;
        for(let i = 0; i < stuffSelectQuestions[0].length; ++i) {
            let checked = stuffCheckboxQuestions[0][i].checked;
            if(checked)
                stuffScore += stuffCheckboxes[i];
        }

        let dollarsSpent = Number(d3.select("#stuff-use-question-container").select("input[type=text]")[0][0].value);
        if(dollarsSpent)
            stuffScore += dollarsSpent;

        d3.select("#stuff-score").classed("hidden", false)
        d3.selectAll(".stuff-score-value").text(function() { return stuffScore; });
        
        // FUN
        let funSelectQuestions = d3.select("#fun-use-question-container")
                                        .selectAll("select");

        let funSelects = data["Fun"].select;
        let funScore = 0;
        for(let i = 0; i < funSelectQuestions[0].length; ++i) {
            let answer = funSelectQuestions[0][i].selectedIndex;
            funScore += funSelects[i][answer];
        }

        d3.select("#fun-score").classed("hidden", false)
        d3.selectAll(".fun-score-value").text(function() { return funScore; });

        // TOTALS
        let grandTotal = waterScore + foodScore + transportationScore + shelterScore + energyScore + clothingScore + stuffScore + funScore;
        d3.selectAll(".grand-total-score-value").text(function() { return grandTotal; });
        let ecologicalFootprint = grandTotal / 100;
        d3.selectAll(".ecological-footprint-value").text(function() { return ecologicalFootprint + " hectares."; });
        buildEcoTable(ecologicalFootprint);
    });
}