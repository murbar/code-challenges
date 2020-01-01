// function checkFlush(dealt, inHand) {
//   const allCards = [...dealt, ...inHand];

//   const suits = allCards.reduce((counts, card) => {
//     const suit = card[card.length - 1];
//     if (!counts[suit]) counts[suit] = 0;
//     counts[suit]++;
//     return counts;
//   }, {});

//   for (const s in suits) {
//     if (suits[s] >= 5) return true;
//   }

//   return false;
// }

function checkFlush(dealt, inHand) {
  const allCards = [...dealt, ...inHand];

  const suits = allCards.reduce((counts, card) => {
    const suit = card[card.length - 1];
    return { ...counts, [suit]: (counts[suit] || 0) + 1 };
  }, {});

  for (const s in suits) {
    if (suits[s] >= 5) return true;
  }

  return false;
}

// You are the dealer in a game of poker! Create a function that takes in two arrays and determines whether there exists a flush (the cards in your hand and the dealt cards must have a combined 5 cards of the same suit).

// - The first array represents the 5 cards dealt on the table.
// - The second array represents the 2 cards in your hand.
// - Notation: card number and suit (abbreviated as S = Spades, H = Hearts, D = Diamonds, C = Clubs) separated by an underscore.

// Examples:
console.log(checkFlush(['A_S', 'J_H', '7_D', '8_D', '10_D'], ['J_D', '3_D'])); //true (diamonds)

// checkFlush(["10_S", "7_S", "9_H", "4_S", "3_S"], ["K_S", "Q_S"]) //true (spades)

console.log(checkFlush(['3_S', '10_H', '10_D', '10_C', '10_S'], ['3_S', '4_D'])); //false

// Notes:
// Hint: If there aren't at least 3 cards of the same suit on the table, there is zero chance of there being a flush when combined with your hand.
