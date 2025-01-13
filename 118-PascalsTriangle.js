/**
 * @param {number} numRows
 * @return {number[][]}
 */

/*
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


1 <= numRows <= 30
*/
var generate = function(numRows) {
    let sol = [];
    for(let row = 0; row < numRows;row++){
        console.log('row:', row);
        let curRow = [];
        for(let j = 0; j <= row;j++){
            console.log('j:', j);
            if(j === 0 || j === row){
                curRow.push(1);
            }
            else{
                curRow.push(sol[row-1][j-1] + sol[row-1][j])
            }
        }
        sol.push(curRow);
    }
    return sol;
};

console.log(generate(5));