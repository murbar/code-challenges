/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 *
 * DFS
 * Sum node values, stop at leaf node
 * O(N) time, visiting each node
 * O(N) space
 */

// iterative with stack
var hasPathSum = function (root, targetSum) {
  if (root === null) {
    return false;
  }
  const stack = [[root, root.val]];
  while (stack.length) {
    const [node, val] = stack.pop();
    if (node.left === null && node.right === null && val === targetSum) {
      return true;
    }
    if (node.right !== null) {
      stack.push([node.right, node.right.val + val]);
    }
    if (node.left !== null) {
      stack.push([node.left, node.left.val + val]);
    }
  }
  return false;
};

// recursive - can't get it to work, will try iterative with a queue
var hasPathSumRecursive = function (root, targetSum) {
  let found = false;
  function dfs(node, sum) {
    if (node === null) return;

    // forgot 'const' here, couldn't figure out the bug! TS linting to the rescue
    const newSum = sum + node.val;

    if (node.left === null && node.right === null) {
      if (newSum === targetSum) {
        found = true;
      }
      return;
    }

    dfs(node.left, newSum);
    dfs(node.right, newSum);
  }
  dfs(root, 0);
  return found;
};
