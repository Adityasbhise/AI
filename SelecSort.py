def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

input_str = input("Enter elements of the array separated by spaces: ")
arr = [int(x) for x in input_str.split()]

sorted_arr = selection_sort(arr)

print("Sorted array:", sorted_arr)

