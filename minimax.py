import math

def minimax(arr,depth):
    maxTurn = bool(depth%2)
    for i in range(depth):
        zipped = zip(arr[::2],arr[1::2])
        print(arr[::2],arr[1::2])
        
        if maxTurn:
            arr = [max(a,b) for a,b in zipped]
        else:
            arr = [min(a,b) for a,b in zipped]
        
        maxTurn = not maxTurn
    return arr

arr = [int(ele) for ele in input().split()]
depth = math.ceil(math.log(len(arr),2))
print(minimax(arr,depth))