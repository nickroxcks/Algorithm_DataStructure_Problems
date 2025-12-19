from typing import List

'''
My Solution: Number + delimiter

Build a string where the begining of each element contains :
1. A number representing the number of characters in the upcomming element
2. A delimiter which is '#'

Since we know every element contains this pattern, it doesn't matter if the array contains multiple delimiters, as we know
the first delimiter will always mark the start and we know how big the upcoming element is

list = ['fo#od', '#i#s', 'yummy']
str_encoded = '5#fo#od4##i#s5#yummy'

O(n) time goes through each element
O(k) memory where k is the longest word and we need to store the word/strings we build
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encodedString = ''
        for word in strs:
            encodedString = encodedString + str(len(word)) + '#'+ word
        return encodedString

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """

        sol = []

        # variables
        currWord = ''
        currNum = -1
        currNumStr = ''

        for letter in s:
            if currNum == -1:
                if letter == '#':
                    currNum = int(currNumStr)
                    if currNum == 0:
                        sol.append('')
                        # reset variables
                        currNum = -1
                        currNumStr = ''
                        currWord = ''
                else:
                    currNumStr = currNumStr + letter
            else:
                currWord = currWord + letter
                if currNum == 1:
                    sol.append(currWord)
                    # reset variables
                    currNum = -1
                    currNumStr = ''
                    currWord = ''
                else:
                    currNum = currNum - 1

        return sol
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))