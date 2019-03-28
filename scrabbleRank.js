// Scrabble time! Create a function that takes a string of words and returns the highest scoring word.Each letter of a word scores points according to it's position in the alphabet: a = 1, b = 2, c = 3, etc.

function scrabbleRank(sentence) {
  const words = sentence.split(' ');
  const alpha = 'abcdefghijklmnopqrstuvwxyz';

  const scores = words.map(w => {
    const score = w.split('').reduce((score, char) => {
      return score + alpha.indexOf(char.toLowerCase()) + 1;
    }, 0);
    return { word: w, score };
  });

  const sorted = scores.sort((a, b) => b.score - a.score);

  return sorted[0].word;
}

// Examples:
console.log(scrabbleRank('The quick brown fox.')); //"brown"

console.log(scrabbleRank('Nancy is very pretty.')); //"pretty"

console.log(scrabbleRank('Check back tomorrow, man!')); //"tomorrow"

console.log(scrabbleRank('Wednesday is hump day.')); //"Wednesday"

// Notes:
// -If two words score the same, return the word that appears first in the original string.
// - The returned string should only contain alphabetic characters(a - z).
// - Preserve case in the returned string(see 4th example above).
