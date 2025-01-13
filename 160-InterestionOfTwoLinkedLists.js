/**INCOMPLETE SOLUTION
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    let map = {}
    let i = 0;
    while(headA.next != undefined || headB.next != undefined){
        if(headA != undefined && (map[headA] === undefined)){
            console.log('adding headA: ', headA)
            map[headA] = true
            headA = headA.next;
        }
        else if(map[headA]){
            console.log('found at headA: ', headA)
            return headA
        }
        if(headB != undefined && (map[headB] === undefined)){
            console.log('adding headB: ', headB)
            map[headB] = true
            headB = headB.next
        }
        else if(map[headB]){
            console.log('found at headB: ', headB)
            return headB
        }
        console.log('iteration ', i);
        i++;
    }

    return null;
};