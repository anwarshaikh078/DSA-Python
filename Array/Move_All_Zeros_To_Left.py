
if __name__ == "__main__":
    arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
    n = len(arr)
    j = 0
    for i in range(0, n):
        if arr[i] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            j = j + 1
    print(arr)