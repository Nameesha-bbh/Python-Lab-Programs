MIN = -999999
MAX = 9999999
import math
def ab(arr,currDepth,maxDepth,nodeIndex,maxTurn,alpha,beta):
    if maxDepth == currDepth:
        return arr[nodeIndex]
        
    
    if maxTurn:
        best = MIN
        
        for i in range(0,2):
            value = ab(arr,currDepth+1,maxDepth,nodeIndex*2+i,False,alpha,beta)
            best = max(best,value)
            alpha = max(alpha,best)
            
            if alpha >= beta:
                break
        return best
        
    else:
        best = MAX
        
        for i in range(0,2):
            value = ab(arr,currDepth+1,maxDepth,nodeIndex*2+i,True,alpha,beta)
            best = min(best,value)
            beta = min(beta,best)
            
            if alpha >= beta:
                break
        return best

arr = [int(ele) for ele in input().split()]
maxDepth = math.ceil(math.log(len(arr),2))
print(ab(arr,0,maxDepth,0,True,MIN,MAX))