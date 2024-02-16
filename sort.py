#use an array nums
#create the first function that sorts the data
#loop through while removing the duplicate numbers in the array
#print out the array with the removed duplicates.
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

    return nums            
def removeDuplicates(nums):
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return nums[:i+1]
sorted=bubble_sort([1,1,2,2,3,3,4,4,5,6,5,4])
print(removeDuplicates(sorted))
    