def quick_sort(input_list):
    if len(input_list) < 2:
        return input_list
    mid = input_list.pop(len(input_list) // 2)
    left = [item for item in input_list if item < mid]
    right = [item for item in input_list if item >= mid]
    return quick_sort(left) + [mid] + quick_sort(right)
