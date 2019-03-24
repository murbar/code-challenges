// https://emberigniter.com/transform-any-data-structure-with-javascript-reduce/

// This is the anatomy of a reduce:

array.reduce(function(acc, value, index, array) {
  // ...
  return acc;
}, initialValue);

/* 
The supplied function will be called once per element in the array:
  - value is the content of the current element of the array, and index… well, its index
  - acc is what I call the “accumulator”.It is the object that carries data around.Like loading a truck with data.For the first element of the array, acc will take the value supplied in initialValue.For the remaining elements, it will take the value returned in the previous invocation of the function.
*/

// It can sum an array(from Array to Number):
[1, 2, 3].reduce(function(acc, value) {
  return acc + value;
}, 0);
// => 6

// or find a max:
[1, 2, 7, 3].reduce(function(acc, value) {
  if (acc < value) acc = value;
  return acc;
}, -Infinity);
// => 7

// It can flatten nested objects(from Array or Object to Array):
const nested = {
  id: 1,
  children: [
    { id: 2 },
    {
      id: 3,
      children: [{ id: 5 }, { id: 6 }]
    },
    { id: 4 }
  ]
};
const flatten = function(obj) {
  const array = Array.isArray(obj) ? obj : [obj];
  return array.reduce(function(acc, value) {
    acc.push(value);
    if (value.children) {
      acc = acc.concat(flatten(value.children));
      delete value.children;
    }
    return acc;
  }, []);
};
flatten(nested);
// => [ { id: 1 }, { id: 2 }, { id: 3 }, { id: 5 }, { id: 6 }, { id: 4 } ]

// It can implement map:
const map = function(array, fn) {
  return array.reduce(function(acc, value) {
    value = fn.call(this, value);
    acc.push(value);
    return acc;
  }, []);
};
// add 1 to each number
map([1, 2], function(n) {
  return n + 1;
});
// => [2, 3]

// ...or filter:
const filter = function(array, fn) {
  return array.reduce(function(acc, value) {
    const ok = fn.call(this, value);
    if (!!ok) acc.push(value);
    return acc;
  }, []);
};
// return only even numbers
filter([1, 2, 5, 7, 8, 10, 104, 1189], function(n) {
  return n % 2 === 0;
});
// => [ 2, 8, 10, 104 ]

// It can join strings:
['hello', 'this', 'is', 'awesome'].reduce(function(acc, value) {
  if (acc) acc = acc.concat(' ');
  acc = acc.concat(value);
  return acc;
}, '');
// => 'hello this is awesome'

// And even call promises serially:
var models = [model1, model2, model3];
models.reduce(function(previous, model) {
  return previous.then(function() {
    return model.save();
  });
}, RSVP.resolve());
