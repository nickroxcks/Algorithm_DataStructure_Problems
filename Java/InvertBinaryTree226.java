import java.util.ArrayDeque;
import java.util.Queue;
/*
Iterative BFS with Que, swapping nodes each iteration with temp nodes
O(n) time for visiting each node once
O(n) memory for worst case que size
 */
public class InvertBinaryTree226 {

        public TreeNode invertTree(TreeNode root) {
        Queue<TreeNode> queue = new ArrayDeque<>();
        if (root == null){
            return root;
        }
        queue.offer(root);

        while(!queue.isEmpty()){

            TreeNode curr = queue.poll();
            TreeNode currLeft = curr.left;
            TreeNode currRight = curr.right;

            curr.left = currRight;
            curr.right = currLeft;

            if(currLeft != null){
                queue.offer(currLeft);
            }
            if(currRight != null){
                queue.offer(currRight);
            }
        }
        return root;
    }
}
