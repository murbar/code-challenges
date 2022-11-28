/**
 * - init closest (best candidate) to root of null
 * start at root, compute absolute difference of target, compare with absolute difference
 * of closest and target, which is smaller?
 * - update closest with value that has smaller difference
 * - compare closest to target, equal, smaller, larger?
 * - due to BST, all nodes right of closest are larger, all right are smaller
 * so we can eliminate half of the BST from consideration
 * - continue until we reach the end of branch, return the closest value
 * - edge case: if we reach node where absolute difference is 0, we can stop and return current node
 * O(log n) time
 * O(1) space for iterative solution
 * O(n) space for recursive solution, call stack will be N deep
 * O(n) worst case, when BST has just one branch
 */

const findClosestValueInBSTIterative = function (tree, target) {
  let closest = Number.POSITIVE_INFINITY;
  let currentNode = tree;
  while (currentNode !== null) {
    if (Math.abs(target - closest) > Math.abs(target - currentNode.value)) {
      closest = currentNode.value;
    }
    if (target < currentNode.value) {
      currentNode = currentNode.left;
    } else if (target > currentNode.value) {
      currentNode = currentNode.right;
    } else {
      break;
    }
  }
  return closest;
};

const findClosestValueInBSTRecursive = function (tree, target) {
  function helper(tree, target, closest = Number.POSITIVE_INFINITY) {
    if (!tree) {
      return closest;
    }
    if (Math.abs(target - closest) > Math.abs(target - tree.value)) {
      closest = tree.value;
    }
    if (target < tree.value) {
      return helper(tree.left, target, closest);
    }
    return closest;
  }
  return helper(tree, target);
};

