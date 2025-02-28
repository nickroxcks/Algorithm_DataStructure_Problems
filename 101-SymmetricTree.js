/*
Iterative DFS comparing left tree to right tree using additional memory
The idea here is that if we traverse the left tree and then save our visited
nodes in memory in a array, then when we traverse the right tree and visit the child nodes in reverse
order we will have traced the same steps in our original array

O(N) time
O(M) memory
*/
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
 * @return {boolean}
 */

var isSymmetric = function(root) {

    var stack = [];
    var mem = []
    stack.push(root.left);

    // Traverse left tree with iterative DFS
    while(stack.length > 0){
        let node = stack.pop();
        if(!node){
            mem.push(null);
            continue;
        }
        mem.push([node.val]);
        stack.push(node.right);
        stack.push(node.left);
    }
    stack.push(root.right);

    // Traverse right tree with iterative DFT but poping right first
    let index = 0
    while(stack.length > 0){
        let node = stack.pop();

        if(!node){
            if(mem[index] != null){
                return false
            }
            index++;
            continue;
        }
        if(mem[index] != node.val){
            return false;
        }
        index++;
        stack.push(node.left);
        stack.push(node.right);
    }
    return true;
};