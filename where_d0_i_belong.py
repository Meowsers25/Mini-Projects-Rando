nums = [2, 5, 78, 8, 32]
print(sorted(nums))


def sort_me(arr, num):
    sorted_arr = sorted(arr)
    print(sorted_arr)
    for i in range(len(sorted_arr)):
        if num <= sorted_arr[i]:
            sorted_arr.insert(sorted_arr[i], num)
            sorted_arr = sorted(sorted_arr)
    print(sorted_arr)


sort_me([56, 23, 2, 30], 8)
