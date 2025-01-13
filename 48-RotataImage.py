from typing import List
'''
leetcode solution
O(N) time
O(1) memory
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix[0])
        for i in range(n // 2 + n % 2):
            for j in range(n // 2):
                tmp = matrix[n - 1 - j][i]
                matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
                matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
                matrix[j][n - 1 - i] = matrix[i][j]
                matrix[i][j] = tmp


class Solution2:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        top_left = (0, 0)
        top_right = (0, len(matrix) - 1)
        bottom_left = (len(matrix) - 1, 0)
        bottom_right = (len(matrix) - 1, len(matrix) - 1)
        i = 0
        while top_left[1] < top_right[1]:
            j = 0
            tl = top_left
            tr = top_right
            bl = bottom_left
            br = bottom_right
            while j < len(matrix) - 1:
                # flip corners
                tlc = matrix[tl[0]][tl[1]]
                trc = matrix[tr[0]][tr[1]]
                brc = matrix[br[0]][br[1]]
                blc = matrix[bl[0]][bl[1]]
                # print(tlc,trc,brc,blc)
                matrix[tl[0]][tl[1]] = blc
                matrix[tr[0]][tr[1]] = tlc
                matrix[br[0]][br[1]] = trc
                matrix[bl[0]][bl[1]] = brc

                tl = (tl[0], tl[1] + 1)
                tr = (tr[0] + 1, tr[1])
                br = (br[0], br[1] - 1)
                bl = (bl[0] - 1, bl[1])
                # print(tl,tr,br,bl)
                j += 1
            top_left = (top_left[0] + 1, top_left[1] + 1)
            bottom_left = (bottom_left[0] - 1, bottom_left[1] + 1)
            top_right = (top_right[0] + 1, top_right[1] - 1)
            bottom_right = (bottom_right[0] - 1, bottom_right[1] - 1)


test = Solution()
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
#print(matrix[4][1:5])


test.rotate(matrix)