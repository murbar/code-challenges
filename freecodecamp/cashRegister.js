// Create an array of objects which hold the denominations and their values
let denominations = [
  { name: 'ONE HUNDRED', val: 100.0 },
  { name: 'TWENTY', val: 20.0 },
  { name: 'TEN', val: 10.0 },
  { name: 'FIVE', val: 5.0 },
  { name: 'ONE', val: 1.0 },
  { name: 'QUARTER', val: 0.25 },
  { name: 'DIME', val: 0.1 },
  { name: 'NICKEL', val: 0.05 },
  { name: 'PENNY', val: 0.01 }
];

function checkCashRegister(price, cash, cid) {
  let change = cash - price;

  // Transform CID array into drawer object
  let register = cid.reduce(
    (acc, curr) => {
      const [denom, amt] = curr;
      acc.total += amt;
      acc[demon] = amt;
      return acc;
    },
    { total: 0 }
  );

  if (register.total === change) {
    return { status: 'CLOSED', change: cid };
  }

  if (register.total < change) {
    return { status: 'INSUFFICIENT_FUNDS', change: [] };
  }

  let change_arr = denominations.reduce(function(arr, curr) {
    let value = 0;
    // While there is still money of this type in the drawer
    // And while the denomination is larger than the change remaining
    while (register[curr.name] > 0 && change >= curr.val) {
      change -= curr.val;
      register[curr.name] -= curr.val;
      value += curr.val;

      // Round change to the nearest hundredth deals with precision errors
      change = Math.round(change * 100) / 100;
    }
    // Add this denomination to the output only if any was used.
    if (value > 0) {
      arr.push([curr.name, value]);
    }
    return arr;
  }, []);

  // If there are no elements in change_arr or we have leftover change
  if (change_arr.length < 1 || change > 0) {
    return { status: 'INSUFFICIENT_FUNDS', change: [] };
  }

  return { status: 'OPEN', change: change_arr };
}

// test here
// checkCashRegister(19.5, 20.0, [
//   ['PENNY', 1.01],
//   ['NICKEL', 2.05],
//   ['DIME', 3.1],
//   ['QUARTER', 4.25],
//   ['ONE', 90.0],
//   ['FIVE', 55.0],
//   ['TEN', 20.0],
//   ['TWENTY', 60.0],
//   ['ONE HUNDRED', 100.0]
// ]);
