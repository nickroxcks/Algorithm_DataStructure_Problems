/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function (list1, list2) {

    if(!list1&&!list2){
        return null;
    }
  let ans = new ListNode();  //ans head node
  let ptr = ans;  //ptr to keep track of where we are in our answers list


  while (list1|| list2) {
    let nextNode = new ListNode();
    //next 4 if cases

    //both pointers exist and list1 smaller
    if (list1 && list2 && list1.val <= list2.val) {
      ptr.val = list1.val;
      list1 = list1.next;
    } 
    //both pointers exist and list2 smaller
    else if (list1 && list2 && list2.val < list1.val) {
      ptr.val = list2.val;
      list2 = list2.next;
    } 
    //list 1 exists and list 2 is done
    else if (list1 && !list2) {
      ptr.val = list1.val;
      list1 = list1.next;
    } 
    //list 2 exists and list1 is done
    else if (list2 && !list1) {
      ptr.val = list2.val;
      list2 = list2.next;
    }

    //check if need a new node at the end or if we are done
    if(list1 ||list2 ){
    ptr.next = nextNode;
    ptr = nextNode;
    }
  }
  return ans;
};