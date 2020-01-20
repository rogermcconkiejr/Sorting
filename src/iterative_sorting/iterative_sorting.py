# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        unordered_list = range((i + 1), len(arr))
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in unordered_list:
            min(unordered_list)
        # TO-DO: swap
            if arr[j] < arr[smallest_index]:
                arr[i], arr[j] = arr[j], arr[i] 

    return arr

check_list = [0,4,3,6,8,2,9,1,5,7]
selection_sort(check_list)
print(check_list)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Loop through list.
    for i in range(0, len(arr) - 1):
        #Check each number vs right neighbor in list.  If i > right neighbor, switch.
        for j in range(0, len(arr) - 1): 
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

check_list2 = [100,72,36,1,15]
bubble_sort(check_list2)
print(check_list2)

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr