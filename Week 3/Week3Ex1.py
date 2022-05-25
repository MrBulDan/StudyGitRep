def more_than_five(nums: list):
    new_list = []
    for num_ind in range(len(nums)):
        if abs(nums[num_ind]) > 5:
            new_list.append(nums[num_ind])
    return new_list


print(more_than_five([-11, 4, -2, 90, 400, 0, -5]))
print(more_than_five([-2, 2, 3, 4, 0, -1]))
print(more_than_five([70, -900, 41, 0]))
