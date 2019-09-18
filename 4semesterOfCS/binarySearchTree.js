// https://en.wikipedia.org/wiki/Binary_search_tree
// https://khan4019.github.io/front-end-Interview-Questions/bst.html

class BSTree {
  constructor(value, left = null, right = null) {
    this.value = value;
    this.left = left;
    this.right = right;
  }

  add(value) {
    if (value < this.value) {
      // go left
      if (this.left) {
        this.left.add(value);
      } else {
        this.left = new BSTree(value);
      }
    } else {
      // go right
      if (this.right) {
        this.right.add(value);
      } else {
        this.right = new BSTree(value);
      }
    }
  }

  inOrderDFTraverse(stack, result = []) {
    if (this.left) this.left.inOrderDFTraverse(result);
    result.push(this.value);
    if (this.right) this.right.inOrderDFTraverse(result);
    return result;
  }

  preOrderDFTraverse() {
    console.log(this.value);
    if (this.left) this.left.preOrderDFTraverse();
    if (this.right) this.right.preOrderDFTraverse();
  }

  postOrderDFTraverse() {
    if (this.left) this.left.postOrderDFTraverse();
    if (this.right) this.right.postOrderDFTraverse();
    console.log(this.value);
  }

  BFTraverse(queue) {
    if (!queue) queue = [this];

    if (!queue.length) return;

    const node = queue.shift();
    console.log(node.value);
    if (node.left) queue.push(node.left);
    if (node.right) queue.push(node.right);
    this.BFTraverse(queue);
  }
}

const tree = new BSTree(40);
tree.add(25);
tree.add(78);
tree.add(10);
tree.add(32);
tree.inOrderDFTraverse();
// console.log('');
// tree.preOrderDFTraverse();
// console.log('');
// tree.postOrderDFTraverse();
// console.log('');
// tree.BFTraverse();
