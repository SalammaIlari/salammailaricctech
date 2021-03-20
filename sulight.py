#Calculate the surface of the building exposed to sunlight 
def Sunlight(arr, n): 
    count = 1 
    curr_max = arr[0] 
    for i in range(1, n): 
        if (arr[i] > curr_max): 
            count += 1
            curr_max = arr[i] 
    return count 
arr = list(map(int,input().split()))
n = len(arr) 
print(Sunlight(arr,n))
