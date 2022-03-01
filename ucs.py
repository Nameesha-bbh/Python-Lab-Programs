def ucs(start,stop):
    
    queue = []
    queue.append([0,start])
    
    visited = {}
    
    answer = 10**8
    
    while len(queue) > 0:
        
        queue = sorted(queue)
        print(queue)
        
        p = queue[-1]
        del queue[-1]
        p[0] *= -1
        
        if p[1] == stop:
            
            return p[0]
        
        if p[1] not in visited:
            
            for i in range(len(graph[p[1]])):
                
                queue.append( [ (p[0] + cost[p[1] , graph[p[1]][i] ])*-1 , graph[p[1]][i]  ] )
        visited[p[1]] = True
  
graph = [[] for i in range(10)]
graph[0].append(1)
graph[0].append(2)
graph[0].append(3)
graph[1].append(3)
graph[1].append(4)
graph[2].append(3)
graph[2].append(5)
graph[3].append(4)
graph[3].append(6)
graph[3].append(5)
graph[4].append(6)
graph[5].append(6)
cost = {}
cost[(0,1)] = 1 
cost[(0,2)] = 2
cost[(0,3)] = 8
cost[(1,3)] = 3
cost[(1,4)] = 4
cost[(2,3)] = 2
cost[(2,5)] = 7
cost[(3,4)] = 2
cost[(3,5)] = 2
cost[(3,6)] = 10
cost[(4,6)] = 2
cost[(5,6)] = 7

print(ucs(0,5))