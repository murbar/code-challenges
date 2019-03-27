// n, e, s, w
// left or right
// convert to number, increment or decrement, modulo 4, index of directions

/*
Create a function that takes in a starting direction and a sequence of left and right turns, and outputs the final direction faced.

-You face 1 out of the 4 compass directions: N, S, E or W.
-A left turn is a counter-clockwise turn. e.g. N (left-turn) ➞ W.
-A right turn is a clockwise turn. e.g. N (right-turn) ➞ E.

Notes:
-You can only face 1 out of the 4 compass directions: N, S, E or W.
*/

const directions = ['N', 'E', 'S', 'W'];
function finalDirection(currentDirection, turns) {
  currentDirection = directions.indexOf(currentDirection);

  turns.forEach(
    turn =>
      (currentDirection =
        turn === 'R'
          ? currentDirection + 1 > 3
            ? 0
            : ++currentDirection
          : currentDirection - 1 < 0
          ? 3
          : --currentDirection)
  );

  return directions[currentDirection];
}

console.log(finalDirection('N', ['L', 'L', 'L'])); //"E"

console.log(finalDirection('N', ['R', 'R', 'R', 'L'])); //"S"

console.log(finalDirection('N', ['R', 'R', 'R', 'R'])); //"N"

console.log(finalDirection('N', ['R', 'L'])); //"N"
