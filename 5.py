def remove_duplicates(my_list):
    new_list = []

    for item in my_list:
        if item not in new_list:
            new_list.append(item)

    return new_list


numbers = [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]

result = remove_duplicates(numbers)

print("Original List:", numbers)
print("List Without Duplicates:", result)
