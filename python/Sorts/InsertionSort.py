def insertion_sort(input_list):
    for i in range(1, len(input_list)):
        for j in range(0, i):
            if input_list[i] < input_list[j]:
                buf = input_list[i]
                for k in range(i, j, -1):
                    input_list[k] = input_list[k - 1]
                input_list[j] = buf
                break
    return 0
