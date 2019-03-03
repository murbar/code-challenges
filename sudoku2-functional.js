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
const allUnique = arr => arr.length === new Set(arr).size;
const filterOnlyNums = arr => arr.filter(i => !isNaN(i));
const isTrue = v => !!v;
// rows and cols
const groupValid = items => allUnique(filterOnlyNums(items));
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
const subGridOrigins = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]];
const getSubGrid = grid =>
  subGridOrigins.map(([x, y]) => [
    ...grid[x].slice(y, y + 3),
    ...grid[x + 1].slice(y, y + 3),
    ...grid[x + 2].slice(y, y + 3)
  ]);
const subGridsValid = grid => true;

const sudoku2 = grid => rowsValid(grid) && colsValid(grid) && subGridsValid(grid);

// these tests pass but there is a bug here somewhere
console.log('Test 1 passes: ', sudoku2(gridFalse) === false);
console.log('Test 2 passes: ', sudoku2(gridTrue) === true);
