(function() {
  function buildQuiz() {
    // we'll need a place to store the HTML output
    const output = [];

    // for each question...
    myQuestions.forEach((currentQuestion, questionNumber) => {
      // we'll want to store the list of answer choices
      const answers = [];

      // and for each available answer...
      for (letter in currentQuestion.answers) {
        // ...add an HTML radio button
        answers.push(
          `<label>
            <input type="radio" name="question${questionNumber}" value="${letter}">
            ${letter} :
            ${currentQuestion.answers[letter]}
          </label>`
        );
      }

      // add this question and its answers to the output
      output.push(
        `<div class="question"> ${currentQuestion.question} </div>
        <div class="answers"> ${answers.join("")} </div>`
      );
    });

    // finally combine our output list into one string of HTML and put it on the page
    quizContainer.innerHTML = output.join("");
  }

  function showResults() {
    // gather answer containers from our quiz
    const answerContainers = quizContainer.querySelectorAll(".answers");

    // keep track of user's answers
    let numCorrect = 0;

    // for each question...
    myQuestions.forEach((currentQuestion, questionNumber) => {
      // find selected answer
      const answerContainer = answerContainers[questionNumber];
      const selector = `input[name=question${questionNumber}]:checked`;
      const userAnswer = (answerContainer.querySelector(selector) || {}).value;

      // if answer is correct
      if (userAnswer === currentQuestion.correctAnswer) {
        // add to the number of correct answers
        numCorrect++;

        // color the answers green
        answerContainers[questionNumber].style.color = "green";
      } else {
        // if answer is wrong or blank
        // color the answers red
        answerContainers[questionNumber].style.color = "red";
      }
    });

    if (myQuestions.length % numCorrect === 0) {
        // show number of correct answers out of total
        resultsContainer.innerHTML = `Great! You got ${numCorrect} correct out of ${myQuestions.length}.`;
    } else if (numCorrect === 0) {
        resultsContainer.innerHTML = `Give it another try!`;
    } else {
        resultsContainer.innerHTML = `Well done! Keep it up to get them all.`;
    };
  }

  const quizContainer = document.getElementById("quiz");
  const resultsContainer = document.getElementById("results");
  const submitButton = document.getElementById("submit");
  const myQuestions = [
    {
      question: "In the double convex lens diagram, what happens when the object is far from the lens?",
      answers: {
          a: "The real image gets flipped.",
          b: "The real image gets bigger.",
          c: "The real image gets smaller.",
          d: "The focal length gets shorter."
      },
      correctAnswer: "c"
    },
    {
      question: "In the double convex lens diagram, what happens when the object is close to the lens?",
      answers: {
          a: "The real image gets flipped.",
          b: "The real image gets bigger.",
          c: "The real image gets smaller.",
          d: "The focal length gets shorter."
      },
      correctAnswer: "b"
    },
    {
      question: "Try moving the focal length (the point labeled F) to the other side of the lens. Is the real image upside down anymore?",
      answers: {
          a: "Yes, it is still upside down.",
          b: "No, it got flipped."
      },
      correctAnswer: "b"
    },
    {
      question: "What part of the eye converts light energy to electrical energy?",
      answers: {
        a: "Retina",
        b: "Lens",
        c: "Sclera",
        d: "Ciliary muscles"
      },
      correctAnswer: "a"
    },
    {
      question: "Imagine that we have a refractor and a reflector telescope, both with the same length and diameter.<br>Which of the two types of telescope can see farther?",
      answers: {
        a: "Refractor telescopes see farther.",
        b: "Reflector telescopes see farther.",
        c: "They can both see the same distances."
      },
      correctAnswer: "b"
    },
    {
      question: "What is the purpose of the iris?",
      answers: {
        a: "It controls the size of the pupil and the amount of light that gets into the eye.",
        b: "It bends light to form images on the retina.",
        c: "It looks good.",
        d: "It works as a concave lens and flips images upside down."
      },
      correctAnswer: "a"
    },
    {
      question: "What are some features that animal eyes have to help them see in the dark?",
      answers: {
          a: "They have larger eyes to collect more light.",
          b: "Their retinas have slower photoreceptors to capture more photons than human eyes.",
          c: "Their eyes group receptor cells to limit the detail in the images they see.",
          d: "All of the above."
      },
      correctAnswer: "d"
    },
    {
      question: "What is the purpose of the sclera?",
      answers: {
          a: "It provides a way for light to enter the eye.",
          b: "It converts light energy to electrical energy.",
          c: "It covers, protects, and lubricates the eye.",
          d: "It focuses light onto the retina."
      },
      correctAnswer: "c"
    }
  ];

  // display quiz right away
  buildQuiz();

  // on submit, show results
  submitButton.addEventListener("click", showResults);
})();