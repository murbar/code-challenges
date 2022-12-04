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
 * @return {number}
 */
const maxDepth = function (root) {
  let max = 0;
  const stack = [[root, 1]];
  while (stack.length > 0) {
    const [node, depth] = stack.pop();
    if (node === null) {
      continue;
    }
    if (depth > max) {
      max = depth;
    }
    stack.push([node.left, depth + 1]);
    stack.push([node.right, depth + 1]);
  }
  return max;
};

const maxDepthRecursive = function (root) {
  if (root === null) {
    return 0;
  }
  return Math.max(maxDepthRecursive(root.left), maxDepthRecursive(root.right)) + 1;
};
