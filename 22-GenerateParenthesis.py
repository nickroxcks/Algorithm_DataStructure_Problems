from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sol = []

        '''
        Given an input string with  num_open and num_closed, determine if its complete (length == (n*2)). 
        If not, explore both options to add a open bracket 
        and a closed bracket, while always maintaining the valid parenthesis conditions
        '''
        def backtracking(path: str, num_open, num_close):
            if len(path) == n*2:
                sol.append(path)
                return
            '''
            at this point, we either have the option to add a open or closed bracket
            '''

            #add open bracket if allowed
            if num_open < n:
                backtracking(path + '(',num_open+1,num_close)

            #add close bracket if allowed
            if num_close < num_open:
                backtracking(path + ')',num_open,num_close+1)

        #call backtracking
        backtracking('(', 1, 0)
        return sol