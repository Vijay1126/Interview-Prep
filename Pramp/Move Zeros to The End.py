def moveZerosToEnd(arr):
      zero = -1
      for i in range(len(arr)):
        if arr[i]!=0:
            arr[zero], arr[i] = arr[i], arr[zero]
            zero+=1

      return arr
print(moveZerosToEnd( [1, 10, 0, 2, 8, 3, 0, 0, 6, 4, 0, 5, 7, 0]))
