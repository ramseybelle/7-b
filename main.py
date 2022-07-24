def reverse_list(list):
    i = 0
    j = len(list) - 1
    while i < j:
        tmp = list[i]
        list[i] = list[j]
        list[j] = tmp
        i += 1
        j -= 1


# Testing
lst = [7, -3, 12, 9]
reverse_list(lst)
print(lst)
