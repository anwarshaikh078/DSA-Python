if __name__ == "__main__":
    arr = [1,2,3,4,5]
    last = arr[len(arr) - 1]
    for i in range(last - 1,0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last
    print(arr)