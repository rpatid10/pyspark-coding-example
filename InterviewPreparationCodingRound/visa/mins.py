def find_nums(nums):
    if not nums:
        return None

    min_value=nums[0]

    for num in nums[1:]:
        if num<min_value:
            min_value=num

    return min_value

print(find_nums([1,2,3,4,5,6,7,8,0]))

