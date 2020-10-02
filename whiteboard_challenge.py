# Add up and print the sum of the all of the minimum elements of each inner array:
arr1 = [[8, 4], [90, -1, 3], [9, 62], [-7, -1, -56, -6], [201], [76, 18]]
# The expected output is given by:
# 4 + -1 + 9 + -56 + 201 + 18 = 175
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

min_nums = []

for arr in arr1:
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    min_nums.append(min_num)

count = 0
for num in min_nums:
    count = count + num

print(count)
print(min_nums)

# Add up and print the sum of the all of the minimum elements of each inner array. Each array may contain additional arrays nested arbitrarily deep, in which case the minimum value for the nested array should be added to the total.
arr2 = [
    [8, [4]],
    [[90, 91], -1, 3],
    [9, 62],
    [[-7, -1, [-56, [-6]]]],
    [201],
    [[76, 0], 18],
]
# The expected output for the above input is:
# 8 + 4 + 90 + -1 + 9 + -7 + -56 + -6 + 201 + 0 + 18 = 260
# You may use whatever programming language you'd like.
# Verbalize your thought process as much as possible before writing any code. Run through the UPER problem solving framework while going through your thought process.

min_nums2 = []


def get_min(arr):
    for item in arr:
        if isinstance(item, list):
            get_min(item)

        if isinstance(item, int):
            min_num = item
            for num in item:
                if isinstance(num, list):
                    get_min(num)
                if isinstance(num, int):
                    if num < min_num:
                        min_num = num
            min_nums2.append(min_num)

    return min_nums


print(get_min(arr2))
