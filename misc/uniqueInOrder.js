const uniqueInOrder = str => {
  const els = str.split('');
  const elsUnique = els.reduce((result, el) => {
    if (result[result.length - 1] !== el) {
      return [...result, el];
    } else {
      return result;
    }
  }, []);
  return elsUnique.join('');
};

console.log(uniqueInOrder('AAABBBCCCDDDAASSSS'));
