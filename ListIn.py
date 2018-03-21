#Julian Conneely, 21/03/18
#List In

#explanation 
#nums=[10,9,8,7,6,5] 
#nums[0] is 10
#nums[1]-5 is 9-5=4 
#so,4 condition proved 
#num [3] is 7 
#so 7 replaces 0 element 
#answer is 7


nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
if 4 in nums:
    print(nums[3])
else:
    print(nums[4])