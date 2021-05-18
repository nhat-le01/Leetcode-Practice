'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 
        print(nums)
        n = len(nums)
        for i in range(n):
            #avoid duplicate
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            #assume that the element nums[i] is the first element of the triplets,
            #we perform a standrad bi-directoinal sweeping for the rest of the array
            #to check if there are two elements that together with nums[i] add up to 0
            low = i + 1
            high = n - 1
            while low < high:
                if nums[low] + nums[high] == -nums[i]:
                    result.append([nums[low], nums[high], nums[i]])
                    low += 1
                    high -= 1
                    while low < high and nums[low] == nums[low - 1]:
                        low += 1
                    while low < high and nums[high] == nums[high + 1]:
                        high -= 1
                elif nums[low] + nums[high] < -nums[i]:
                    low += 1
                else:
                    high -= 1
        return result
                    
            
