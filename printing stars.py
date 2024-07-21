class Star:
    def printStar(self):
        for i in range(1,13):
            if ( i == 3 or i == 6 or i == 9 or i == 12 ):
                print("*")
            else:
                print("*",end="")
        return i
#obj = Star()
#print(obj.printStar())


nums = [3,2,4]
target = 6
l = []
"""

class A:
    ls = []
    target =0
    def method(self,ls,target):
        ls = []
        for i in range(len(ls)):
           for j in range(i+1,len(ls)): #i=0andj=1 [9],1.1 = [14], 
              print(i,j)
             #print(i,j)
              plus = nums[i] + nums[j]
              if ( plus == target ):
                 return [i,j]
              else:
                 print("else")
                 return []
        print(ls)
obj = A()
obj.ls = [2,3,4]
obj.target = 0
print(obj.method(ls=[2,3,4],target=9))"""
"""
class lister:
    def __init__(self,data_list,target) -> None:
        self.data_list = data_list
        self.target = target
    
    def adds(self):
        self.data_list = [2,3,4]
        self.target = 6
        for i in range(0,len(self.data_list)):
            for j in range(i+1,len(self.data_list)): 
                value = i + j 
                print(value) 
                if ( i + j  == self.target):
                    return [self.data_list.index(i),self.data_list.index(i)]
                else:
                    print('else printed')
                    return [self.data_list.index(i),self.data_list.index(i)]

obj = lister([2,3,4],6)
obj.data_list=[2,3,4]
print(obj.adds())
        
"""
nums = [2,4,3]
dic = {}
target = 6
"""One Pass Approach , try each element until finds result through single loop, we minues each value by target and add it to the 
dictionary and if there value exists already we simply return the result if not then we add current subtracted item to it, One Pass"""
for i , v in enumerate(nums):
    
    if ( target - v in dic):
        dic[target - v] = i

    dic[v] = i
        
print(nums)
print(dic)