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

function translateCoordsToSubGrid(value) {
  const x = Math.floor(value.row / 3);
  const y = Math.floor(value.col / 3);
  return [x, y];
}

function valueObjectsAreEqual(v1, v2) {
  return v1.value === v2.value && v1.row === v2.row && v1.col === v2.col;
}

function areUniqueInSubGrid(values) {
  const subGrid = [[[], [], []], [[], [], []], [[], [], []]];
  // let areUnique = true;

  values.forEach(v => {
    const [x, y] = translateCoordsToSubGrid(v);
    subGrid[x][y].push(v);
  });

  // for loops so we can return from outer function
  for (const row of subGrid) {
    for (const location of row) {
      if (!location.length > 1) continue;
      for (const value of location) {
        for (const v of location) {
          if (valueObjectsAreEqual(v, value)) continue;
          if (v.value === value.value) return false;
        }
      }
    }
  }

  // subGrid.forEach(row => {
  //   row.forEach(location => {
  //     if (!location.length > 1) return;
  //     location.forEach(value => {
  //       location.forEach(v => {
  //         // abort if testing against self
  //         if (valueObjectsAreEqual(v, value)) return;
  //         if (v.value === value.value) areUnique = !areUnique;
  //       });
  //     });
  //   });
  // });

  // return areUnique;
  return true;
}

function isUniqueInRowAndCol(value, values) {
  return true;
}

function valueIsValid(value) {
  return '123456789'.includes(value);
}

function extractValues(grid) {
  const values = [];
  grid.forEach((row, x) => {
    row.forEach((value, y) => {
      if (valueIsValid(value))
        values.push({
          value: value,
          row: x,
          col: y
        });
    });
  });
  return values;
}

function sudoku2(grid) {
  const values = extractValues(grid);

  if (!areUniqueInSubGrid(values)) return false;

  for (const value of values) {
    if (!isUniqueInRowAndCol(value, values)) return false;
  }

  return true;
}

console.log('Test 1 passes: ', sudoku2(gridFalse) === false);
console.log('Test 2 passes: ', sudoku2(gridTrue) === true);
