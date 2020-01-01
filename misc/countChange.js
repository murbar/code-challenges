const coins = [1, 1, 1, 1];

function count(arr) {
  const coinValues = [0.25, 0.1, 0.05, 0.01];

  return arr.reduce((total, count, i) => {
    return total + count * coinValues[i];
  }, 0);
}

console.log(count(coins)); // 0.41
