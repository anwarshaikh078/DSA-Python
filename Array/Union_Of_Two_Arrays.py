
if __name__ == "__main__":
    a = [1,2,3,4,5]
    b = [1,2,4]
    
    universal = list(set(a) | set(b))
    
    print(universal)