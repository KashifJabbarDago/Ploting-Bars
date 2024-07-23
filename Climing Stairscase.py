"""
giving staircase you need to count each the steps required to reach at the top 
Example:
input: 2
output: 2
Explanation:
Case 1:
1 --> 1 step + 1 step = 2
2 --> direct two returns 2 

Example
input = 3 
output = 3
Explanation
1 step + 1 step + 1 step = 3
1 step + 2 step = 3 
2 step + 1 step = 3 
files 
"""

def stairCase(n):
    if (n <= 1):
        return 1
    operation1 = (n -1)
    operation2 = (n - 2)
    return operation1        + operation2

print(stairCase(50))
