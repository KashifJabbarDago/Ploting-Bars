def twoSum():
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = [2,7,11,15]
        target = 9 
        # target = 9 ==  num[0] + num[7] = 9 
        lst = []
        for i in nums:
            for j in nums:
                if j + i  == target:
                       return list(lst[nums.index(i), nums.index(j)])
            return lst
            
twoSum()