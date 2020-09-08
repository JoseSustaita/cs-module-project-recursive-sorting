
# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = []

    # Start point at the begginning of the arrays
    a = 0
    b = 0

    # While both of them are still in bounds of their respective arrays
    while a < len(arrA) and b < len(arrB):
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1

        else:
            merged_arr.append(arrB[b])
            b += 1
    # All ellements have been merged from one of the arrays

    # check both arrays to see if the pointer is stil in range of array
    if a < len(arrA):
        # 1st array still has leftover elements
        # push them all to the merged array
        merged_arr.extend(arrA[a:])
    if b < len(arrB):
        merged_arr.extend(arrB[b:])

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def merge_sort(arr):
    # base case: stop splitting the arrays in half
    # if length of array is greater than one
    if len(arr) > 1:
        # otherwise keep splitting in half
        # not included in the left side
        left = merge_sort(arr[0: len(arr) // 2])
        # Is included on the right side.. up to the end of the array
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here
#
#
# def merge_sort_in_place(arr, l, r):
#     # Your code here
