def findDiffHeights(n,k,arr):
    
    arr.sort();
    ans = arr[n-1] - arr[0]
    small = arr[0] + k
    big = arr[n-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(1,n):
        
        substract = arr[i] - k
        add = arr[i] + k
        
        if substract >= small or add <= big:
            continue
        
        if big - substract <= add - small:
            small = substract
        else:
            big = add
        
    return min(ans, big - small)

if __name__ == "__main__":
    n = 3
    k = 2
    arr=[1,2,3]
    print(findDiffHeights(n,k,arr))
    
    