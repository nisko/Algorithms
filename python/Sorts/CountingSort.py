def counting_sort(input_list, max_number):
    buf_list = [0 for _ in range(max_number)]
    result_list = [0 for _ in range(len(input_list))]
    for i in range(len(input_list)):
        buf_list[input_list[i]] += 1
    for i in range(1, max_number):
        buf_list[i] += buf_list[i - 1]
    for i in range(len(input_list) - 1, -1, -1):
        result_list[buf_list[input_list[i]] - 1] = input_list[i]
        buf_list[input_list[i]] -= 1
    return result_list
