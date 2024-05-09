def bubble_sort_2D(arr):
    n = len(arr)
    m = len(arr[0])
    total_elements = n * m 

for i in range(total_elements - 1):

    for j in range(total_elements - 1 - i ):
        row1 = j // m
        col1 = j % m

        row2 = (j + 1)//m
        col2 = (j + 1)% m 

        if arr[row1][col1] > arr[row2][col2]:
            arr[row1][col1], arr[row2][col2] = arr[row2][col2], arr[row1][col1]


arr = [9, 2, 3],
    


    

