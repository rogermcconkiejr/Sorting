# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    arrA_index = 0
    arrB_index = 0
    merged_arr = []
    # TO-DO: merge the arrays together with their neighbor, comparing the left-most values of each array.
    # Only run WHILE both arrA and arrB lists are not empty.
    while arrA_index < len( arrA ) and arrB_index < len( arrB ):
        #Compare first elements of each array, fill merged_arr with lowest value.
        if arrA[arrA_index] < arrB[arrB_index]:
            merged_arr.append(arrA[arrA_index])
            arrA_index += 1
        else:
            merged_arr.append(arrB[arrB_index])
            arrB_index += 1
    # Fill merged_arr with remaining values of either arrA or arrB if its counterpart is empty.
    merged_arr += arrA[arrA_index:]
    merged_arr += arrB[arrB_index:]
    return merged_arr

test_list = [6,9,2,5,8,0,1,4,3,7]

# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO: take in the array and keep splitting it until only arrays with a length of one are left.
    # base - Return array if length <=1.
    if len(arr) <= 1:
        return arr
    else:
        #If length is greater than 1, split the array into two arrays.
        half = len(arr) // 2
        a = arr[:half]
        b = arr[half:]
        #Run this step repeatedly until all arrays are a length of 1.
        arrA = merge_sort( a )
        arrB = merge_sort( b )
    #Pass these arrays into merge function to be sorted.
    return merge(arrA, arrB)


print(merge_sort(test_list))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
