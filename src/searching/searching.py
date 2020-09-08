# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    # Check base case
    if end >= start:

        mid = (start + end) // 2

        # If element is present at the middle itself
        if arr[mid] == target:
            return mid

        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid-1)

        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(arr, target, mid+1, end)

    else:
        # Element is not present in the array
        return -1


arr = [2, 3, 4, 10, 40]
target = 40

result = binary_search(arr, target, 0, len(arr)-1)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
