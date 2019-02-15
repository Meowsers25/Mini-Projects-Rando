# nums = [2, 5, 78, 8, 32]
# print(sorted(nums))


def sort_me(arr, num):
    new_arr = sorted(arr)
    # return new_arr
    for i in range(len(new_arr)):
        if new_arr[i] > num:
            index = i
            break
    final_arr = new_arr[:i] + [num] + new_arr[i:]
    print(final_arr)
    return f'{num}\'s Location in List is [{index}]'


print(sort_me([56, 23, 2, 30], 44))

# a = [15, 12, 10]
# b = sorted(a)
# print(b)  # --> b = [10, 12, 15]
# c = 13
# for i in range(len(b)):
#     if b[i] > c:
#         index = i
#         break
# d = b[:i] + [c] + b[i:]
# print(d)  # --> d = [10, 12, 13, 15]
