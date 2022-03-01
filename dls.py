graph = {
 'A' : ['B','C'],
 'B' : ['D', 'E'],
 'C' : ['F', 'G'],
 'D' : [],
 'E' : [],
 'F' : [],
 'G' : []
}


def dls(start,currDepth,maxDepth,goal,path):    
    path.append(start)
    if start == goal:
        return path
    if currDepth == maxDepth:
        return False
    for neighbour in graph[start]:
        if dls(neighbour,currDepth+1,maxDepth,goal,path):
            return path
        path.pop()
    return False

print(dls('A',0,2,'G',[]))