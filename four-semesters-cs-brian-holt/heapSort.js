const heapSort = array => {
  array = createMaxHeap(array);
  let heapSize = array.length;
  let temp;
  for (let i = array.length - 1; i > 0; i--) {
    temp = array[0];
    array[0] = array[i];
    array[i] = temp;
    heapSize--;
    heapify(array, 0, heapSize);
  }
  return array;
};

const createMaxHeap = array => {
  for (let i = Math.floor(array.length / 2); i >= 0; i--) {
    heapify(array, i, array.length);
  }
  return array;
};

const heapify = (array, index, heapSize) => {
  const left = 2 * index + 1;
  const right = 2 * index + 2;

  let largestValueIndex = index;

  if (heapSize > left && array[largestValueIndex] < array[left]) {
    largestValueIndex = left;
  }

  if (heapSize > right && array[largestValueIndex] < array[right]) {
    largestValueIndex = right;
  }

  if (largestValueIndex !== index) {
    const temp = array[index];
    array[index] = array[largestValueIndex];
    array[largestValueIndex] = temp;
    heapify(array, largestValueIndex, heapSize);
  }
};

const unsorted = [2, 5, 3, 8, 10, 6, 4, 7, 9, 1];
const sorted = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
console.assert(JSON.stringify(heapSort(unsorted)) === JSON.stringify(sorted));
