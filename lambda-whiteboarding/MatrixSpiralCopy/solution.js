function spiralCopy(inputMatrix) {
  const result = [];
  let topRow = 0;
  let rightCol = inputMatrix[0].length - 1;
  let bottomRow = inputMatrix.length - 1;
  let leftCol = 0;

  while (topRow <= bottomRow && leftCol <= rightCol) {
    // step through to the right
    for (col = 0; col <= rightCol; col++) {
      result.push(inputMatrix[topRow][col]);
    }
    topRow++;
    // to the bottom
    for (row = topRow; row <= bottomRow; row++) {
      result.push(inputMatrix[row][rightCol]);
    }
    rightCol--;
    // to the left
    if (topRow <= bottomRow) {
      for (col = rightCol; col >= leftCol; col--) {
        result.push(inputMatrix[bottomRow][col]);
      }
      bottomRow--;
    }
    // back to the top
    if (leftCol <= rightCol) {
      for (row = bottomRow; row > topRow; row--) {
        result.push(inputMatrix[row][leftCol]);
      }
      leftCol++;
    }
  }

  return result;
}
