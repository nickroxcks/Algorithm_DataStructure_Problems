/*
My solution
O(n) time
O(n) extra memory tehcnically
Iterate through each node and mark as visited. If we find a ndoe we already visited, return true.
If we find a null value at the next node, return false. 
*/
/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function (head) {
  let curNode = head;
  while (curNode) {
    //if there is no next node, clearly no loop so we are done
    if (curNode.next === undefined) {
      return false;
    }

    //A next node existed. If we've never visitied current node, mark visited and move on
    if (curNode.checked === undefined) {
      curNode.checked = true;
      curNode = curNode.next;
    } else {
      return true;
    }
  }
  return false;
};

/* Leetcode solution
O(n) time
O(1) memory
Floyd's Cycle Finding Algorithm

*/

var hasCycleLeetcode = function (head) {
    let fast = head;
     while (fast && fast.next) {
       head = head.next;
       fast = fast.next.next;
       if (head === fast) return true;
     }
     return false;
   };
/*
Solution 2: use hash map to mark visited nodes. Can use memory adress 
O(n) time 
O(n) memory
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        nodes_seen = set()
        while head is not None:
            if head in nodes_seen:
                return True
            nodes_seen.add(head)
            head = head.next
        return False
*/
