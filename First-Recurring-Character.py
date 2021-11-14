# Dummies Approach
def first_recurring_char(array):
    for i in range(0, len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return array[i]  # O(n^2)


# Pro Approach
def first_recurring_char2(array):
    my_dict = {}
    for i in range(0, len(array)):
        if array[i] in my_dict:
            return array[i]
        else:
            my_dict[array[i]] = i  # O(n)


my_array = [3, 5, 5, 3, 2, 5, 7]
print(first_recurring_char(my_array))
print(first_recurring_char2(my_array))

