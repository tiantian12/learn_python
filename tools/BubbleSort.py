def bubbleSort(array):
    array_len=len(array)
    for i in range(0,array_len):
        for j in range(1,array_len-i):
            if array[j-1]>array[j]:
                temp=array[j-1]
                array[j-1]=array[j]
                array[j]=temp

    return array
test_arr=[1,4,11,3,-3,33,-9,333]
result_arr=bubbleSort(test_arr)
print(result_arr)