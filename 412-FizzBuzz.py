from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        sol = []
        for i in range(1, n + 1):
            if((i % 15) == 0):
                sol.append('FizzBuzz')
            elif((i%3) == 0):
                sol.append('Fizz')
            elif((i%5)==0):
                sol.append('Buzz')
            else:
                sol.append(str(i))
        return sol

test = Solution()

print(test.fizzBuzz(15))

print(11%10)