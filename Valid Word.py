"""
A word is considered valid if:
It contains a minimum of 3 characters.
It contains only digits (0-9), and English letters (uppercase and lowercase).
It includes at least one vowel.
It includes at least one consonant.
You are given a string word.

Return true if word is valid, otherwise, return false.
Notes:
i am modified by git

'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
A consonant is an English letter that is not a vowel.
Example 1:
Input: word = "234Adas"
Output: true
Explanation:

This word satisfies the conditions.

Example 2:

Input: word = "b3"

Output: false

Explanation:

The length of this word is fewer than 3, and does not have a vowel.
"""

class solution:
    word = ""
    numericals ='0,1,2,3,4,5,6,7,8,9'
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    def validWord(self,word):
        if self.numericals in self.word:
            return True
        else:
            return False 

object = solution()
var = object.validWord("1kif")
print(var)







        



