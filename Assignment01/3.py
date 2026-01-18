import numpy as np

data = list(range(1, 501))

np.random.shuffle(data)

def insertion_sort(arr):
    steps = 0
    a = arr.copy()
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        steps += 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            steps += 1
        a[j + 1] = key
        steps += 1
    return a, steps

def merge_sort(arr):
    steps = 0

    def merge(left, right):
        nonlocal steps
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            steps += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(a):
        nonlocal steps
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        steps += 1
        left = sort(a[:mid])
        right = sort(a[mid:])
        return merge(left, right)

    sorted_arr = sort(arr.copy())
    return sorted_arr, steps


insertion_sorted, insertion_steps = insertion_sort(data)
merge_sorted, merge_steps = merge_sort(data)

print("Insertion Sort Steps:", insertion_steps)
print("Merge Sort Steps:", merge_steps)
