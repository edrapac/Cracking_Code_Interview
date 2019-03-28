#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Given nums = [2, 7, 11, 15], target = 9,

#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].

def twoSum( nums, target):
      
    returnlist = []
    for i in range(len(nums)):
        if (nums[i] < target):
            result = (target - nums[i])
            firstindex = i
            returnlist.append(firstindex)
    
    for i in range(len(nums)):
        result = (target - nums[i])
        if(nums[i] == result):
            secondindex = i
            returnlist.append(secondindex)
    return returnlist

if __name__ == '__main__':
    thelist = [2,7,11,15]
    print(twoSum(nums=thelist,target=9))
