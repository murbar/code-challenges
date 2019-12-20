// https://www.freecodecamp.org/learn/coding-interview-prep/algorithms/inventory-update

function countItemsInArrays(counts, ...arrs) {
  arrs.forEach(arr => {
    arr.forEach(item => {
      const [qty, name] = item;
      if (counts.hasOwnProperty(name)) {
        counts[name] = counts[name] + qty;
      } else {
        counts[name] = qty;
      }
    });
  });
}

function updateInventory(arr1, arr2) {
  // All inventory must be accounted for or you're fired!
  const counts = {};
  countItemsInArrays(counts, arr1, arr2);
  const result = [];
  for (let [name, qty] of Object.entries(counts)) {
    result.push([qty, name]);
  }
  return result.sort((nameA, nameB) => {
    const a = nameA[1].toLowerCase(),
      b = nameB[1].toLowerCase();
    return a < b ? -1 : a > b ? 1 : 0;
  });
}

// Example inventory lists
var curInv = [
  [21, 'Bowling Ball'],
  [2, 'Dirty Sock'],
  [1, 'Hair Pin'],
  [5, 'Microphone']
];

var newInv = [
  [2, 'Hair Pin'],
  [3, 'Half-Eaten Apple'],
  [67, 'Bowling Ball'],
  [7, 'Toothpaste']
];

updateInventory(curInv, newInv);
