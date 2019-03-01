// https://app.codesignal.com/interview-practice/task/SKZ45AF99NpbnvgTn

// Sudoku is a number - placement puzzle.The objective is to fill a 9 × 9 grid with numbers in such
// a way that each column, each row, and each of the nine 3 × 3 sub - grids that compose the grid
// all contain all of the numbers from 1 to 9 one time.

// Implement an algorithm that will check whether the given grid of numbers represents a valid
// Sudoku puzzle according to the layout rules described above.Note that the puzzle represented by
// grid does not have to be solvable.

const gridTrue = [
  ['.', '.', '.', '1', '4', '.', '.', '2', '.'],
  ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
  ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
  ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
  ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
  ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
  ['.', '.', '.', '5', '.', '.', '.', '7', '.']
];

const gridFalse = [
  ['.', '.', '.', '.', '2', '.', '.', '9', '.'],
  ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
  ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
  ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
  ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
  ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
  ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
  ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
  ['.', '2', '.', '.', '3', '.', '.', '.', '.']
];

function areUniqueInSubGrid(values) {
  return true;
}

function isUniqueInRowAndCol(value, values) {
  return true;
}

function sudoku2(grid) {
  const values = [];
  grid.forEach((row, x) => {
    row.forEach((value, y) => {
      if ('123456789'.includes(value))
        values.push({
          value: value,
          row: x,
          col: y
        });
    });
  });

  if (!areUniqueInSubGrid(values)) return false;

  values.forEach(value => {
    if (!isUniqueInRowAndCol(value, values)) return false;
  });

  return true;
}

console.log('Test 1 passes: ', sudoku2(gridFalse) === false);
console.log('Test 2 passes: ', sudoku2(gridTrue) === true);
