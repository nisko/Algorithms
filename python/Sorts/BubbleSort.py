def bubble_sort(input_list):
    for i in range(len(input_list) - 1):
        for j in range(i + 1, len(input_list)):
            if input_list[i] > input_list[j]:
                input_list[i], input_list[j] = input_list[j], input_list[i]
