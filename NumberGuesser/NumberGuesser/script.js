let humanScore = 0;
let computerScore = 0;
let currentRoundNumber = 1;


//Generating a random number
function generateTarget(){
return Math.floor(Math.random()*10);
}

//Comparing the two guesses to see which was closest, returning human if tied.
function compareGuesses(humanGuess, computerGuess, num){
    let comCount = 0;
    let humCount = 0;
    if (humanGuess === num ){
        console.log("Human guessed right.");
        return true;
    } else if (computerGuess === num){
        console.log("Computer guessed right.");
        return false;
    }

    while (humanGuess !== num){
        if(humanGuess > num){
            humanGuess--;
            humCount++;
        } else if (humanGuess < num){
            humanGuess++;
            humCount++;
        }
    }

    while (computerGuess !== num){
        if(computerGuess > num){
            computerGuess--;
            comCount++;
        } else if (computerGuess < num){
            computerGuess++;
            comCount++;
        }
    }

    if(humCount < comCount || humCount === comCount ){
        return true;
    } else {
        return false;
    }
}
//Updating the score for the winner
function updateScore(winner){
    if(winner === "human"){
        humanScore++;
    } else if(winner === "computer"){
        computerScore++;
    }
}
//Advancing the round by one at the end.
function advanceRound(){
    currentRoundNumber++;
}