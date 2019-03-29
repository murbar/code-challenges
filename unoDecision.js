// It's your turn in a game of Uno. Create a function that takes as its arguments (1) your hand (an array of cards), and (2) the face-up card. In Uno, you are able to play a card from your hand if either:

// One of the card colors in your hand matches the face-up card's color.
// One of the card numbers in your hand matches the face-up card's number.

// Write a function that will return:
// -"Uno!" if after playing your card, you are left with a single card.
// -"You won!" if after playing your card, you are left with zero cards (an empty array).
// -"Keep going..." otherwise.

const decision = (inHand, faceUp) => {
  const [faceUpColor, faceUpNumber] = faceUp.split(' ');

  const inHandAfterPlay = inHand.filter(c => {
    const [inHandColor, inHandNumber] = c.split(' ');
    return faceUpColor !== inHandColor && faceUpNumber !== inHandNumber;
  });

  switch (inHandAfterPlay.length) {
    case 0:
      return 'You won!';
    case 1:
      return 'Uno!';
    default:
      return 'Keep going...';
  }
};

// Examples:
console.log(decision(['yellow 3', 'red 3'], 'red 10')); //"Uno!"

console.log(decision(['blue 1'], 'blue 5')); //"You won!"

console.log(decision(['blue 1', 'green 2', 'yellow 4', 'red 2'], 'blue 5')); //"Keep going..."
