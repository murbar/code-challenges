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

  return true;
}

function rowsAreEqual(v1, v2) {
  return v1.row === v2.row;
}

function colsAreEqual(v1, v2) {
  return v1.col === v2.col;
}

function valuesAreEqual(v1, v2) {
  return v1.value === v2.value;
}

function isUniqueInRowAndCol(value, values) {
  for (const v of values) {
    if (valueObjectsAreEqual(v, value)) continue;
    if ((rowsAreEqual(v, value) || colsAreEqual(v, value)) && valuesAreEqual(v, value))
      return false;
  }

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

// console.log('Test 1 passes: ', sudoku2(gridFalse) === false);
// console.log('Test 2 passes: ', sudoku2(gridTrue) === true);

/* 
Alternative algo:
functional style
list all coords for each num element in grid
  get list of all nums in rows
  get list of all nums in cols
  get list of all nums in each subgrid
  check length list length equals set(list) length
  if so, all valid

*/

// helpers
const areAllUnique = numsArr => numsArr.length === new Set(numsArr).size;
const filterOnlyNums = arr => arr.filter(i => !isNaN(i));
const isTrue = v => !!v;
// rows and cols
const groupValid = row => areAllUnique(filterOnlyNums(row));
const rowsValid = grid => grid.map(groupValid).every(isTrue);
const getCol = (_, i, grid) => grid.map(row => row[i]);
// const getCols = grid => grid.map(getCol);
const colsValid = grid =>
  grid
    .map(getCol)
    .map(groupValid)
    .every(isTrue);

// subgrid
// stub
const subGridsValid = grid => true;

const puzzleValid = grid => rowsValid(grid) && colsValid(grid) && subGridsValid(grid);

// function sudoku2(grid) {
//   return puzzleValid(grid);
// }

// console.log(gridTrue));
// const mapper = (a, b, c, d) => console.log(a, b, c, d);
// const ar = [1, 2, 3, 4];

// console.log(getCols(gridTrue, 2));
console.log(rowsAndColsAreValid(gridTrue));
// console.log(ar.map(mapper));
