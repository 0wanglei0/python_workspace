# -*- coding: utf-8 -*-
def majorityElement(nums: list) -> int:
    num_dict = dict()
    for num in nums:
        freq = num_dict.get(num, 0)
        num_dict[num] = freq + 1

    print(num_dict.values())
    print(num_dict.keys())
    max = 0
    max_key = 0
    for key, value in num_dict.items():
        if value > max:
            max = value
            max_key = key

    return max_key

print(majorityElement([3, 2, 3]))
