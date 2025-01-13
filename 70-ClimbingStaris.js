/*My solution
DP with memoization
O(n) time
O(n) memory
*/
/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let cache = {};
    var fib =  function(n)  {
        if (n in cache) {
            return cache[n];
        } else {
            if (n <= 2) {
                return n;
            } else {
                cache[n] = fib(n-1) + fib(n-2);
                return cache[n];
            }
        }
    }
    return fib(n)
}
/*
Fibonacci iterativesolution
O(n) time
O(1) memory
Here you realize this is just a fibonacci problem
Can use the itertaive fib solution to sovle the same problem
*/
var climbStairsFibonacci = function(n) {
    if(n===1){
        return n;
    }

    let first = 1
    let second =2;
    for(let i = 3; i<=n; i++){
        let third = first + second;
        first = second;
        second = third;
    }
    return second;

}

/*
Recursive with no memoization
O(2^n) time
O(1) memory
*/
var climbStairsRecursiveNoMemo = function(n) {
    let numWays = 0;
    var recurseClimbStairs = function(m){
        if(m ==2){
            //2 ways. Either a two step, or one step twice
            numWays = numWays + 2
        }
        else if (m==1){
            numWays = numWays + 1
        }
        else{
            recurseClimbStairs(m-2);
            recurseClimbStairs(m-1);
        }
    }

    recurseClimbStairs(n);
    return numWays;
};