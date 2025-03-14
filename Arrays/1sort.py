## Move all the one's to the end and do this in O(1) space

arr = [3,1,2,3,4,1,6,7,1,1,2,9,9,1,1]


arr = [3,1,1,2,3,4,1]


def sort1(arr):
    i = 0
    j = len(arr) - 1
    counter = 0
    while (i<=j):
        # print(f"counter {counter} i{i} , j{j} , arr, {arr}")
        if arr[i] != 1:
            i = i+1
        if arr[j] == 1:
            ## Already in right position move on
            j = j-1
        
        elif arr[i] == 1:
            if arr[j]!=1:
                arr[i] = arr[j]
                arr[j] = 1
                j = j-1
            else:
                j = j-1
        # print(f"counter {counter} i{i} , j{j} , arr, {arr}")
        counter+=1
        
    print(arr , len(arr))
    
def one_sort(nums):
    i, j = 0, len(nums) - 1
    while i <= j:
        # print("Inside while with arr ", nums , i , j)
        if nums[i] != 1:
            i += 1
        elif nums[i] == 1:
            if nums[j] == 1:
                j -= 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
                
    # print(nums)
    return nums
        

nums = one_sort(arr)
print(nums)
                
            
            