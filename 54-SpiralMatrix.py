'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        cur = [0,0]
        lb = 0
        rb = len(matrix[0]) - 1
        ub = 0
        db = len(matrix[0]) - 1
        sol = []
        sol.append(matrix[0][0])
        def isInbound(up,db,lb,rb,cur):
            if ub <= cur[0] and cur[0] <= db and  lb <= cur[1] and cur[1] <= rb:
                return True
            return False
        while ub <= cur[0] and cur[0] <= db and  lb <= cur[1] and cur[1] <= rb :
            #go right
            while lb <= cur[1] and cur[1] < rb:
                cur[1] = cur[1] + 1
                sol.append(matrix[cur[0]][cur[1]])
            print(sol)
            #go down
            while ub <= cur[0] and cur[0] < db:
                cur[0] = cur[0] + 1
                sol.append(matrix[cur[0]][cur[1]])

            #go left
            while lb < cur[1] and cur[1] <= rb:
                cur[1] = cur[1] - 1
                sol.append(matrix[cur[0]][cur[1]])
            #go up
            while ub+1 < cur[0] and cur[0] <= db:
                cur[0] = cur[0] - 1
                sol.append(matrix[cur[0]][cur[1]])
            print(ub,db,lb,rb)
            lb+=1
            rb -=1
            ub+=1
            db-=1
            print(ub,db,lb,rb)
        return sol


'''